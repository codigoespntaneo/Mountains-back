from src.mountains.domain.valid_object import MountainImg

class Mountain:
    def __init__(self, id: int, name: str, height: int, country: str,  img: MountainImg | None = None):
        self._id = id 
        self._name = name
        self._height = height
        self._country = country
        self._img = img
    @classmethod
    def create(cls, name:str, country:str, height:int, img:str)->"Mountain":
        return cls(
            id=None,
            name=name,
            country=country,
            height=height,
            img=MountainImg(value=img),
        )
    
    def name(self) -> str:
        return self._name

    def country(self) -> str:
        return self._country

    def img(self) -> "MountainImg":
        return self._img
    
    def height(self) -> int:
        return self._height
    
    def id(self) -> int | None:
        return self._id