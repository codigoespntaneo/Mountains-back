import pytest
from src.mountains.application.get_all_mountain import GetAllMountains
from src.mountains.domain.models import Mountain
from src.mountains.domain.repository import MountainRepository
from src.mountains.domain.valid_object import MountainImg

class FakeMountainRepository(MountainRepository):
    def __init__(self):
        self._mountains = []
    
    def save(self, mountain: Mountain) -> None:
        self._mountains.append(mountain)

    def all(self) -> list[Mountain]:
        return list(self._mountains)
    
    def get_by_id(self, id: int) -> Mountain | None:
        return None
    
    def update(self, id: int, mountain: Mountain) -> Mountain | None:
        return None
    
    def delete(self, id: int) -> bool:
        return True


class TestGetAllMountains:
    def test_get_all_returns_all_mountains(self) -> None:
        mountain_repository = FakeMountainRepository()
        
        mountain1 = Mountain(
            name="Monte Everest",
            country="Nepal / China",
            height=8849,
            img=MountainImg(value="https://example.com/everest.jpg")
        )
        mountain2 = Mountain(
            name="Monte Fuji",
            country="Japan",
            height=3776,
            img=MountainImg(value="https://example.com/fuji.jpg")
        )
        mountain_repository.save(mountain1)
        mountain_repository.save(mountain2)
        
        result = GetAllMountains(mountain_repository).execute()
        
        assert len(result) == 2
        assert result[0].name() == "Monte Everest"
        assert result[1].name() == "Monte Fuji"
    
    def test_get_all_returns_empty_list(self) -> None:
        mountain_repository = FakeMountainRepository()
        
        result = GetAllMountains(mountain_repository).execute()
        
        assert len(result) == 0