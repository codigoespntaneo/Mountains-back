from src.mountains.domain.models import Mountain
from src.mountains.domain.repository import MountainRepository

class GetAllMountains:
    def __init__(self, mountain_repository: MountainRepository):
        self._mountain_repository = mountain_repository
    
    def execute(self) -> list[Mountain]:
        return self._mountain_repository.all()