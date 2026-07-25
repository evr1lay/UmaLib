from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.horse import HorseORM
from app.schemas.horse import HorseCreateSchema, HorseUpdateSchema

class HorseNotFound(Exception):
    """Horse not found"""

class HorseRepository:
    def __init__(self, db: Session) -> None:
        self.db = db
        
    def get_all(self):
        return self.db.scalars(select(HorseORM)).all()
    
    def get_by_id(self, horse_id: str) -> HorseORM:
        horse_by_id = self.db.get(HorseORM, horse_id)
        if not horse_by_id:
            raise HorseNotFound("Horse not found")
        return horse_by_id
    
    def create(self, payload: HorseCreateSchema):
        new_horse = HorseORM(id=str(uuid4()), **payload.model_dump())
        self.db.add(new_horse)
        self.db.commit()
        self.db.refresh(new_horse)
        return new_horse
    
    def update(self, horse_id: str, payload: HorseUpdateSchema):
        horse_for_update = self.db.get(HorseORM, horse_id)
        if not horse_for_update:
            raise HorseNotFound("Horse not found")
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(horse_for_update, key, value)
            
        self.db.commit()
        self.db.refresh(horse_for_update)
        
        return horse_for_update
    
    def delete(self, horse_id: str):
        horse_for_delete = self.db.get(HorseORM, horse_id)
        if not horse_for_delete:
            raise HorseNotFound("Horse not found")
        
        self.db.delete(horse_for_delete)
        self.db.commit()
