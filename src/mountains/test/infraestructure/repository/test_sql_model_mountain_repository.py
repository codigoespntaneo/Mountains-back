import pytest
from sqlmodel import SQLModel, select, Session

from src.mountains.domain.models import Mountain
from src.mountains.domain.valid_object import MountainImg
from src.mountains.infraestructure.repository import SQLModelMountainRepository, engine, MountainModel


class TestSQLModelMountainRepository:

    @pytest.fixture(autouse=True)
    def cleanup_database(self):
        SQLModel.metadata.create_all(engine)
        yield
        SQLModel.metadata.drop_all(engine)
            
    def test_saves_mountain_to_database(self) -> None:

        repository = SQLModelMountainRepository()

        saved = repository.save(Mountain(
            name="Monte Everest",
            country="Nepal / China",
            height=8849,
            img=MountainImg(value="https://example.com/everest.jpg")
        ))

        assert saved.id() is not None
        with Session(engine) as session:
            mountain = session.get(MountainModel, saved.id())
            assert mountain is not None
            assert mountain.name == "Monte Everest"
            assert mountain.country == "Nepal / China"
            assert mountain.height == 8849
            assert mountain.img == "https://example.com/everest.jpg"

    def test_all_returns_all_mountains(self) -> None:
        with Session(engine) as session:
            session.add(MountainModel(
                name="Monte Everest",
                country="Nepal / China",
                height=8849,
                img="https://example.com/everest.jpg"
            ))
            session.commit()

        mountains = SQLModelMountainRepository().all()

        assert len(mountains) == 1
        assert mountains[0].name() == "Monte Everest"
        assert mountains[0].country() == "Nepal / China"
        assert mountains[0].height() == 8849
        assert mountains[0].img() == MountainImg(value="https://example.com/everest.jpg")