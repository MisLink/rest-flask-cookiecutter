from datetime import datetime

from sqlalchemy import Column, DateTime

from .extensions import db


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


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


class Model(ActiveRecordMixin, db.Model):
    __abstract__ = True
