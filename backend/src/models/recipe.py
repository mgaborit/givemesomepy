from typing import List

from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, db_engine
from models.ingredient import IngredientModel

class RecipeIngredientModel(Base):
    __tablename__ = 'recipe_ingredient'
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipe.id"), primary_key=True)
    ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredient.id"), primary_key=True)
    quantity: Mapped[int] = mapped_column()
    ingredient: Mapped['IngredientModel'] = relationship()

class RecipeModel(Base):
    __tablename__ = 'recipe'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    duration: Mapped[int] = mapped_column()
    difficulty: Mapped[int] = mapped_column()
    ingredients: Mapped[List['RecipeIngredientModel']] = relationship()
    steps: Mapped[List['RecipeStepModel']] = relationship(
        order_by='RecipeStepModel.position', 
        collection_class=ordering_list('position', count_from=1)
    )

class RecipeStepModel(Base):
    __tablename__ = 'recipe_step'
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipe.id"), primary_key=True)
    position: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
