from typing import List

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from models.ingredient import Ingredient

class Recipe(Base):
    __tablename__ = 'recipe'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    duration: Mapped[int] = mapped_column()
    difficulty: Mapped[int] = mapped_column()
    ingredients: Mapped[List['RecipeIngredientAssociation']] = relationship()
    steps: Mapped[List['RecipeStep']] = relationship(
        order_by='RecipeStep.position', 
        collection_class=ordering_list('position', count_from=1)
    )

    def serialize(self, full_detail: bool = True) -> dict:
        result = {
            'id': self.id,
            'name': self.name,
            'duration': self.duration,
            'difficulty': self.difficulty
        }
        if full_detail:
            result['ingredients'] = [i.serialize() for i in self.ingredients]
            result['steps'] = [s.serialize() for s in self.steps]
        return result

class RecipeStep(Base):
    __tablename__ = 'recipe_step'
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipe.id"), primary_key=True)
    position: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    def serialize(self) -> dict:
        return {
            'position': self.position,
            'name': self.name, 
            'description': self.description
        }

class RecipeIngredientAssociation(Base):
    __tablename__ = 'recipe_ingredient'
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipe.id"), primary_key=True)
    ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredient.id"), primary_key=True)
    quantity: Mapped[int] = mapped_column()
    ingredient: Mapped['Ingredient'] = relationship()

    def serialize(self) -> dict:
        result = self.ingredient.serialize()
        result['quantity'] = self.quantity
        return result
