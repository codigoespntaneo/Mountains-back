from src.characters.domain.valid_object import CharacterImg

class Character:
    def __init__(self, name: str, state: str,  img: CharacterImg | None = None):
        self._name = name
        self._state = state
        self._img = img
    @classmethod
    def create(cls, name:str, state:str, img:str)->"Character":
        return cls(name, state, img)