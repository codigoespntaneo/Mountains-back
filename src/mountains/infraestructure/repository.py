from sqlmodel import SQLModel, Field, create_engine, Session,select
from src.mountains.domain.valid_object import MountainImg
from src.mountains.domain.models import Mountain
from src.mountains.domain.repository import MountainRepository

class MountainModel(SQLModel, table=True):
        id: int | None = Field(default=None, primary_key=True, sa_column_kwargs={"autoincrement": True})
        name: str
        country: str
        height: int
        img: str


engine = create_engine("sqlite:///mountains.db")

SQLModel.metadata.create_all(engine)

class SQLModelMountainRepository(MountainRepository):

    def all(self)-> list[Mountain]:
        with Session(engine) as session:
            mountain_models= session.exec(select(MountainModel)).all()
        return [
            Mountain(
                name=mountain_model.name,
                country=mountain_model.country,
                height=mountain_model.height,
                img=MountainImg(value=mountain_model.img),
                id=mountain_model.id
            )
            for mountain_model in mountain_models
        ]

    def get_by_id(self, id: int) -> Mountain | None:
        with Session(engine) as session:
            mountain_model = session.get(MountainModel, id)
            if mountain_model is None:
                return None
            return Mountain(
                name=mountain_model.name,
                country=mountain_model.country,
                height=mountain_model.height,
                img=MountainImg(value=mountain_model.img),
                id=mountain_model.id
            )

    def update(self, id: int, mountain: Mountain) -> Mountain | None:
        with Session(engine) as session:
            mountain_model = session.get(MountainModel, id)
            if mountain_model is None:
                return None
            mountain_model.name = mountain.name()
            mountain_model.country = mountain.country()
            mountain_model.height = mountain.height()
            mountain_model.img = mountain.img().value
            session.add(mountain_model)
            session.commit()
            return Mountain(
                name=mountain_model.name,
                country=mountain_model.country,
                height=mountain_model.height,
                img=MountainImg(value=mountain_model.img),
                id=mountain_model.id
            )

    def save(self, mountain: Mountain) -> Mountain:
        with Session(engine) as session:
            mountain_model = MountainModel(
                name=mountain.name(),
                country=mountain.country(),
                height=mountain.height(),
                img=mountain.img().value,
            )
            session.add(mountain_model)
            session.commit()
            session.refresh(mountain_model)
        return Mountain(
            name=mountain_model.name,
            country=mountain_model.country,
            height=mountain_model.height,
            img=MountainImg(value=mountain_model.img),
            id=mountain_model.id,
        )

    def delete(self, id: int) -> bool:
        with Session(engine) as session:
            mountain_model = session.get(MountainModel, id)
            if mountain_model is None:
                return False
            session.delete(mountain_model)
            session.commit()
            return True 
            