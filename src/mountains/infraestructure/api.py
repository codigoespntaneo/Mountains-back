from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.mountains.domain.models import Mountain
from src.mountains.application.create_character import CreateMountain, CreateMountainCommand
from src.mountains.infraestructure.repository import SQLModelMountainRepository

router = APIRouter()

class MountainPayload(BaseModel):
    name: str
    country: str
    height: int
    img: str
    
class MountainResponse(BaseModel):
    id: int | None
    name: str
    country: str
    height: int
    img: str
    
    @classmethod
    def from_domain(cls, mountain: Mountain) -> "MountainResponse":
        return cls(
            name=mountain.name(),
            country=mountain.country(),
            height=mountain.height(),
            img=mountain.img().value
        )

@router.post("/mountains/")
def create_mountain(payload: MountainPayload) -> MountainResponse:
    mountain = CreateMountain(SQLModelMountainRepository()).execute(
        CreateMountainCommand(
            name=payload.name,
            country=payload.country,
            height=payload.height,
            img=payload.img
        )
    )
    return MountainResponse.from_domain(mountain)
