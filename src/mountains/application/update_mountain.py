from dataclasses import dataclass
from src.mountains.domain.valid_object import MountainImg
from src.mountains.domain.models import Mountain
from src.mountains.domain.repository import MountainRepository

@dataclass
class UpdateMountainCommand:
    id: int
    name: str
    country: str
    height: int
    img: str

class UpdateMountain:
    def __init__(self, mountain_repository: MountainRepository):
        self._mountain_repository = mountain_repository

    def execute(self, command: UpdateMountainCommand) -> Mountain | None:
        mountain_img = MountainImg(value=command.img)
        mountain = Mountain(
            id=None,
            name=command.name,
            country=command.country,
            height=command.height,
            img=mountain_img
        )
        return self._mountain_repository.update(command.id, mountain)