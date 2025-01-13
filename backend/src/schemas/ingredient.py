from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.ingredient import IngredientModel

class IngredientSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = IngredientModel
        include_relationships = True
        load_instance = True