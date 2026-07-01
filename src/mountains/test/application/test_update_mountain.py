import pytest
from src.mountains.application.update_mountain import UpdateMountain, UpdateMountainCommand
from src.mountains.domain.models import Mountain
from src.mountains.domain.repository import MountainRepository
from src.mountains.domain.valid_object import MountainImg

class FakeMountainRepository(MountainRepository):
    def __init__(self):
        self._mountains = []
        self._next_id = 1
    
    def save(self, mountain: Mountain) -> None:
        self._mountains.append(mountain)

    def all(self) -> list[Mountain]:
        return list(self._mountains)
    
    def get_by_id(self, id: int) -> Mountain | None:
        for m in self._mountains:
            if id == self._next_id:
                return m
        return None
    
    def update(self, id: int, mountain: Mountain) -> Mountain | None:
        if 0 < id <= len(self._mountains):
            self._mountains[id - 1] = mountain
            return mountain
        return None
    
    def delete(self, id: int) -> bool:
        return True


class TestUpdateMountain:
    def test_update_mountain_success(self) -> None:
        mountain_repository = FakeMountainRepository()

        original = Mountain(
            name="Monte Everest",
            country="Nepal / China",
            height=8849,
            img=MountainImg(value="https://example.com/everest.jpg")
        )
        mountain_repository.save(original)

        result = UpdateMountain(mountain_repository).execute(
            UpdateMountainCommand(
                id=1,
                name="Monte Everest",
                country="Nepal / China",
                height=8849,
                img="https://example.com/everest-v2.jpg"
            )
        )

        assert result is not None
        assert result.name() == "Monte Everest"
        assert result.country() == "Nepal / China"
        assert result.height() == 8849

    def test_update_mountain_not_found(self) -> None:
        mountain_repository = FakeMountainRepository()

        result = UpdateMountain(mountain_repository).execute(
            UpdateMountainCommand(
                id=999,
                name="Monte Everest",
                country="Nepal / China",
                height=8849,
                img="https://example.com/everest.jpg"
            )
        )
        
        assert result is None