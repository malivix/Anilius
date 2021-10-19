import uuid
from typing import Dict

from anilius.db.db import Model
from anilius.db.db_session import DBSession
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func

from anilius.model.uuid import UUID
from anilius.utils.uuid import validate_uuid4


class BaseModel(Model):
    __abstract__ = True

    id = Column(UUID(), primary_key=True, default=uuid.uuid4)
    created_on = Column(DateTime, default=func.now())
    updated_on = Column(DateTime, default=func.now(), onupdate=func.now())

    @classmethod
    def create(cls, commit=True, close=True, **entity_properties):
        entity = cls(**entity_properties)
        with DBSession(commit=commit, close=close) as session:
            session.add(entity)

        return entity

    @classmethod
    def get(cls, *entity_id):
        for enttid in entity_id:
            if not validate_uuid4(enttid):
                raise ValueError("entity id should be uuid4")
        with DBSession(commit=False) as session:
            entities = [session.query(cls).get(enttid) for enttid in entity_id]
        return tuple(entities)

    @classmethod
    def list(cls, condition_dict):
        with DBSession(commit=False) as session:
            entity = session.query(cls).filter(*condition_dict).all()
        return entity

    @classmethod
    def delete(cls, **entity_properties) -> None:
        """deletes the given entry from database table"""

        with DBSession(commit=False) as session:
            entity = session.query(cls).filter_by(**entity_properties).first()
            session.delete(entity)
        return

    @classmethod
    def update(cls, entity_id: "UUID", new_fields: Dict) -> None:
        """updates the model given the new fields

        Args:
            entity_id (UUID): id of the entry to be updated
            new_fields (Dict): fields with the updated values

        Raises:
            ValueError: raised when the given id is not uuid4
        """

        if not validate_uuid4(entity_id):
            raise ValueError("entity id should be uuid4")
        with DBSession(commit=True, close=True) as session:
            entity = session.query(cls).get(entity_id)
            entity.update(new_fields)
        return
