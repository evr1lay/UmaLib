from app.models.base import Base
from sqlalchemy.orm import Mapped

class HorseORM(Base):
    __tablename__ = "Horses"
    
    name: Mapped[str]
    description: Mapped[str]
    birthday: Mapped[str]
    height: Mapped[int]