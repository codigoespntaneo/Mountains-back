import pytest
from src.mountains.application.delete_mountain import DeleteMountain, DeleteMountainCommand
from src.mountains.domain.models import Mountain
from src.mountains.domain.repository import MountainRepository
from src.mountains.domain.valid_object import MountainImg

class FakeMountainRepository(MountainRepository):
    def __init__(self):
        self._mountains = {}
        self._next_id = 1
    
    def save(self, mountain: Mountain) -> None:
        self._mountains[self._next_id] = mountain
        self._next_id += 1

    def all(self) -> list[Mountain]:
        return list(self._mountains.values())
    
    def get_by_id(self, id: int) -> Mountain | None:
        return self._mountains.get(id)
    
    def update(self, id: int, mountain: Mountain) -> Mountain | None:
        if id in self._mountains:
            self._mountains[id] = mountain
            return mountain
        return None
    
    def delete(self, id: int) -> bool:
        if id in self._mountains:
            del self._mountains[id]
            return True
        return False


class TestDeleteMountain:
    def test_delete_mountain_success(self) -> None:
        mountain_repository = FakeMountainRepository()
        
        mountain = Mountain(
            name="Monte Everest",
            country="Nepal / China",
            height=8849,
            img=MountainImg(value="https://example.com/everest.jpg")
        )
        mountain_repository.save(mountain)
        
        result = DeleteMountain(mountain_repository).execute(
            DeleteMountainCommand(id=1)
        )
        
        assert result is True
    
    def test_delete_mountain_not_found(self) -> None:
        mountain_repository = FakeMountainRepository()
        
        result = DeleteMountain(mountain_repository).execute(
            DeleteMountainCommand(id=999)
        )
        
        assert result is False