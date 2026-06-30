from sqlmodel import SQLModel, Field, create_engine, Session, select
from src.mountains.domain.valid_object import MountainImg
from src.mountains.domain.models import Mountain
from src.mountains.domain.repository import MountainRepository


class MountainModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    country: str
    height: int
    img: str

engine = create_engine("sqlite:///mountains.db")
SQLModel.metadata.create_all(engine)


class SQLModelMountainRepository(MountainRepository):
    def all(self) -> list[Mountain]:
        with Session(engine) as session:
            mountain_model = session.exec(select(MountainModel)).all()
        return [
            Mountain(
                name=mountain_model.name,
                country=mountain_model.country,
                height=mountain_model.height,
                img=MountainImg(value=mountain_model.img),
            )
            for mountain_model in mountain_model
        ]
    
    def save(self, mountain: Mountain) -> None:
        mountain_model = MountainModel(
            name=mountain.name(),
            country=mountain.country(),
            height=mountain.height(),
            img=mountain.img().value
        )
        with Session(engine) as session:
            session.add(mountain_model)
            session.commit()