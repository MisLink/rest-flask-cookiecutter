from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.hybrid import hybrid_property

from .extensions import db


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SoftDeleteMixin:
    deleted_at = Column(DateTime, default=None)

    @hybrid_property
    def deleted(self):
        return self.deleted_at is not None

    @deleted.expression
    def deleted(self):
        return self.deleted_at.isnot(None)

    @deleted.setter
    def deleted(self, status):
        self.deleted_at = datetime.utcnow() if status else None


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


class Model(db.Model, ActiveRecordMixin):
    __abstract__ = True
