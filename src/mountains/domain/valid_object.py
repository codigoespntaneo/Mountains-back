from dataclasses import dataclass
import validators
from src.mountains.domain.exception import MountainImgNotValid

@dataclass(frozen=True, kw_only=True)
class MountainImg:
    value:str

    def __post_init__(self)-> None:
        if not validators.url(self.value):
            raise MountainImgNotValid