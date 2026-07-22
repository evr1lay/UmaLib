from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.horse import HorseSchema, HorseCreateSchema, HorseUpdateSchema
from app.services.horse import HorseNotFound, HorseService
from app.api.dependencies import get_horse_service

router = APIRouter(prefix="/horses")

@router.get("")
def get_horses(horse_service: HorseService = Depends(get_horse_service)) -> list[HorseSchema]:
    return horse_service.list_horses()
    
@router.post("", status_code=status.HTTP_201_CREATED)
def create_horse(payload: HorseCreateSchema, horse_service: HorseService = Depends(get_horse_service)) -> HorseSchema:
    return horse_service.create_horse(payload)

@router.patch("")
def update_horse(horse_id: str, payload: HorseUpdateSchema, horse_service: HorseService = Depends(get_horse_service)) -> HorseSchema:
    try:
        return horse_service.update_horse(horse_id, payload)
    except HorseNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Horse with id {horse_id} not found")
    
@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def delete_horse(horse_id: str, horse_service: HorseService = Depends(get_horse_service)) -> None:
    try:
        return horse_service.delete_horse(horse_id)
    except HorseNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Horse with id {horse_id} not found")