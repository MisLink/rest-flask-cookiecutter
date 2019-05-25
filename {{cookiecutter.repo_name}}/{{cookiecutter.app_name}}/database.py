from __future__ import annotations

from datetime import datetime
from functools import wraps
from typing import Callable
from typing import Optional
from typing import Union

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Query
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import Session
from sqlalchemy.util import safe_reraise

from {{cookiecutter.app_name}}.extensions import db


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class _Actives(Query):
    def __new__(cls, *args, **kwargs):
        query = super().__new__(cls)
        if len(args) > 0:
            super(_Actives, query).__init__(*args, **kwargs)
            return query.filter_by(deleted=False)
        return query

    def __init__(self, *args, **kwargs):
        pass


class SoftDeleteMixin:
    deleted_at = Column(DateTime, default=None)
    actives = db.session.query_property(query_cls=_Actives)

    @hybrid_property
    def deleted(self):
        return self.deleted_at is not None

    @deleted.setter  # type: ignore
    def deleted(self, status):
        self.deleted_at = datetime.now() if status else None

    @deleted.expression  # type: ignore
    def deleted(self):
        return self.deleted_at.isnot(None)


class ActiveRecordMixin:
    def save(self):
        db.session.add(self)
        db.session.flush()
        return self

    @classmethod
    def create(cls, **kwargs):
        return cls(**kwargs).save()

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save()

    def delete(self):
        db.session.delete(self)
        db.session.flush()


class PrimaryKey:
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"


class Model(db.Model, ActiveRecordMixin):
    __abstract__ = True


class _Atomic:
    def __init__(self, session: Union[scoped_session, Session]):
        self.session = session

    def __enter__(self) -> _Atomic:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.transaction(None)
        else:
            self.session.rollback()

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return self.transaction(func, *args, **kwargs)

        return wrapper

    def transaction(self, func: Optional[Callable], *args, **kwargs):
        try:
            if func is None:
                result = None
            else:
                result = func(*args, **kwargs)
            self.session.commit()
        except BaseException:
            with safe_reraise():
                self.session.rollback()
        else:
            return result


# TODO: Support savepoint
def atomic(session: Union[scoped_session, Session, Callable, None] = None):
    """
    with atomic():  # None
        pass

    with atomic(session):  # Session
        pass

    @atomic  # Callable
    def x():
        pass

    @atomic(session):  # Session
    def x():
        pass
    """
    if not isinstance(session, (scoped_session, Session)) and callable(session):
        return _Atomic(db.session)(session)
    return _Atomic(session if session is not None else db.session)
