from src.mountains.domain.models import Mountain
from src.mountains.domain.repository import MountainRepository

class GetMountainById:
    def __init__(self, mountain_repository: MountainRepository):
        self._mountain_repository = mountain_repository
    
    def execute(self, id: int) -> Mountain | None:
        return self._mountain_repository.get_by_id(id)