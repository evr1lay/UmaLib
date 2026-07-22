from pydantic import BaseModel, ConfigDict
from typing import Optional

class HorseSchema(BaseModel):
    id: str
    name: str
    description: str
    birthday: str
    height: int
    
    model_config = ConfigDict(from_attributes=True)
    
class HorseCreateSchema(BaseModel):
    name: str
    description: str
    birthday: str
    height: int
    
class HorseUpdateSchema(BaseModel):
    name: Optional[str] | None = None
    description: Optional[str] | None = None
    birthday: Optional[str] | None = None
    height: Optional[int] | None = None