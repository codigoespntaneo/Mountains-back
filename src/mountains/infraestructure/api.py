from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.mountains.domain.models import Mountain
from src.mountains.application.create_mountain import CreateMountain, CreateMountainCommand
from src.mountains.infraestructure.repository import SQLModelMountainRepository
from src.mountains.application.get_all_mountain import GetAllMountains
from src.mountains.application.get_mountain_by_id import GetMountainById
from src.mountains.application.update_mountain import UpdateMountain, UpdateMountainCommand
from src.mountains.application.delete_mountain import DeleteMountain, DeleteMountainCommand


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
        img = mountain.img()
        return cls(
            id=mountain.id(),
            name=mountain.name(),
            country=mountain.country(),
            height=mountain.height(),
            img=img.value if img is not None else "",
        )

@router.get("/mountains/")
def get_all_mountains() -> list[MountainResponse]:
    mountains = GetAllMountains(SQLModelMountainRepository()).execute()
    return [MountainResponse.from_domain(c) for c in mountains]

@router.get("/mountains/{id}")
def get_mountain_by_id(id: int) -> MountainResponse:
    mountain = GetMountainById(SQLModelMountainRepository()).execute(id)
    if mountain is None:
        raise HTTPException(status_code=404, detail="Mountain not found")
    return MountainResponse.from_domain(mountain)

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

@router.put("/mountains/{id}")
def update_mountain(id: int, payload: MountainPayload) -> MountainResponse:
    mountain = UpdateMountain(SQLModelMountainRepository()).execute(
        UpdateMountainCommand(
            id=id,
            name=payload.name,
            country=payload.country,
            height=payload.height,
            img=payload.img
        )
    )
    if mountain is None:
        raise HTTPException(status_code=404, detail="Mountain not found")
    return MountainResponse.from_domain(mountain)

class DeleteResponse(BaseModel):
    message: str

@router.delete("/mountains/{id}")
def delete_mountain(id: int) -> DeleteResponse:
    deleted = DeleteMountain(SQLModelMountainRepository()).execute(
        DeleteMountainCommand(id=id)
    )
    if not deleted:
        raise HTTPException(status_code=404, detail="Mountain not found")
    return DeleteResponse(message="Mountain deleted successfully")