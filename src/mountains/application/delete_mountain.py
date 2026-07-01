from dataclasses import dataclass
from src.mountains.domain.repository import MountainRepository

@dataclass
class DeleteMountainCommand:
    id: int

class DeleteMountain:
    def __init__(self, mountain_repository: MountainRepository):
        self._mountain_repository = mountain_repository
    
    def execute(self, command: DeleteMountainCommand) -> bool:
        return self._mountain_repository.delete(command.id)