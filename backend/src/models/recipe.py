from typing import List

from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database import Base

class Recipe(Base):
    __tablename__ = 'recipe'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    duration: Mapped[int] = mapped_column()
    difficulty: Mapped[int] = mapped_column()
    steps: Mapped[List['RecipeStep']] = relationship()

    def as_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'duration': self.duration,
            'difficulty': self.difficulty,
            'steps': [s.as_dict() for s in self.steps]
        }

class RecipeStep(Base):
    __tablename__ = 'recipe_step'
    id: Mapped[int] = mapped_column(primary_key=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipe.id"))
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    def as_dict(self) -> dict:
        return {'id': self.id, 'name': self.name, 'description': self.description}