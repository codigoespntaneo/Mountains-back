from src.mountains.domain.valid_object import MountainImg

class Mountain:
    def __init__(self, id: int, name: str, height: int, country: str,  img: MountainImg | None = None):
        self._id = id 
        self._name = name
        self._height = height
        self._country = country
        self._img = img
    @classmethod
    def create(cls, name:str, state:str, img:str)->"Mountain":
        return cls(name, state, img)