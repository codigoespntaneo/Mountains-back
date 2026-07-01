import pytest
from src.mountains.application.create_mountain import CreateMountain, CreateMountainCommand
from src.mountains.domain.models import Mountain
from src.mountains.domain.repository import MountainRepository

class FakeMountainRepository(MountainRepository):
    def __init__(self):
        self._mountains = []

    def save(self, mountain: Mountain) -> Mountain:
        self._mountains.append(mountain)
        return mountain

    def all(self)->list[Mountain]: 
        return list(self._mountains)

    def get_by_id(self, id: int) -> Mountain | None:
        return None

    def update(self, id: int, mountain: Mountain) -> Mountain | None:
        return None

    def delete(self, id: int) -> bool:
        return False

class TestCreateMountain:
    def test_create_mountain(self) -> None:
        mountain_repository = FakeMountainRepository()

        CreateMountain(mountain_repository).execute(
            CreateMountainCommand(
                name = "Monte Everest",
                country= "Nepal / China",
                height= 8849,
                img = "https://example.com/everest.jpg"
            )
        )
        mountains = mountain_repository.all()
        assert len(mountains) == 1

    def test_create_mountain_fails_with_invalid_url(self)->None:
        mountain_repository = FakeMountainRepository()
        
        with pytest.raises(Exception):
            CreateMountain(mountain_repository).execute(
                CreateMountainCommand(
                    name="Monte Everest",
                    country="Nepal / China",
                    height= 8849,
                    img="invalid_img"
                )
            )
        mountains= mountain_repository.all()
        assert len(mountains) == 0