from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.horse import HorseService

def get_horse_service(db: Session = Depends(get_db)):
    """Dependency injection function HorseService"""
    return HorseService(db)