import enum

from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """Defining Animals Types"""

    DOG = "DOG"
    CAT = "CAT"
    FISH = "FISH"
    TURTLE = "TURTLE"


class Pets(Base):
    """Pets Entity"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pet [name={self.name}, specie={self.specie}, user_id={self.user_id}]"
