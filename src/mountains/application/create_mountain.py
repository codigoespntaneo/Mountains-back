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
        mountain_img = MountainImg(value=command.img)
        mountain = Mountain.create(
            name=command.name,
            country=command.country,
            height=command.height,
            img=mountain_img
        )
        
        return self._mountain_repository.save(mountain)