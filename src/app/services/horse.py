from sqlalchemy.orm import Session

from app.repositories.horse import HorseNotFound, HorseRepository
from app.schemas.horse import HorseCreateSchema, HorseSchema, HorseUpdateSchema

class HorseService:
    def __init__(self, db: Session):
        self.db = db
        self.horse_repository = HorseRepository(db=db)
        
    def list_horses(self) -> list[HorseSchema]:
        horses_orm = self.horse_repository.get_all()
        return [HorseSchema.model_validate(horse) for horse in horses_orm]
    
    def get_horse(self, horse_id: str) -> HorseSchema:
        horse_orm = self.horse_repository.get_by_id(horse_id)
        return HorseSchema.model_validate(horse_orm)
    
    def create_horse(self, payload: HorseCreateSchema) -> HorseSchema:
        horse_orm = self.horse_repository.create(payload)
        return HorseSchema.model_validate(horse_orm)
    
    def update_horse(self, horse_id: str, payload: HorseUpdateSchema) -> HorseSchema:
        try:
            updated_orm = self.horse_repository.update(horse_id, payload)
            return HorseSchema.model_validate(updated_orm)
        except Exception:
            raise HorseNotFound("Horse not found")
    
    def delete_horse(self, horse_id: str) -> None:
        try:
            self.horse_repository.delete(horse_id)
        except Exception:
            raise HorseNotFound("Horse not found")