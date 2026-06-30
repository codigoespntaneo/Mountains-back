from dataclasses import dataclass
from src.mountains.domain.models import Mountain
from src.mountains.domain.repository import MountainRepository
from src.mountains.domain.valid_object import MountainImg

@dataclass
class CreateMountainCommand:
    name: str
    country: str
    height: int
    img: str

class CreateMountain:
    def __init__(self, mountain_repository: MountainRepository):
        self._mountain_repository = mountain_repository
        
    def execute(self, command: CreateMountainCommand) -> Mountain:
        mountain = Mountain(
            name=command.name,
            country=command.country,
            height=command.height,
            img=MountainImg(value=command.img)
        )
        self._character_repository.save(mountain)
        return mountain