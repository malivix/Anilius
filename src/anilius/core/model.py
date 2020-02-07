import uuid

from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func

from anilius.core.db import Model, db_session
from anilius.model.uuid import UUID
from anilius.utils.uuid import validate_uuid4


class BaseModel(Model):
    __abstract__ = True

    id = Column(UUID(), primary_key=True, default=uuid.uuid4)
    created_on = Column(DateTime, default=func.now())
    updated_on = Column(DateTime, default=func.now(), onupdate=func.now())

    @classmethod
    def create(cls, commit=True, **entity_properties):
        entity = cls(**entity_properties)
        db_session().add(entity)

        if commit:
            db_session.commit()

        return entity

    @classmethod
    def get(cls, entity_id):
        if not validate_uuid4(entity_id):
            raise ValueError("entity id should be uuid4")

        entity = db_session().query(cls).get(entity_id)
        return entity

    @classmethod
    def list(cls, condition_dict):
        entity = db_session().query(cls).filter(*condition_dict).all()
        return entity
