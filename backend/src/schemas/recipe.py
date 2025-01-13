from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
from marshmallow import post_load

from models.recipe import RecipeModel, RecipeStepModel, RecipeIngredientModel
from schemas.ingredient import IngredientSchema

class RecipeIngredientSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RecipeIngredientModel
        include_relationships = True
        load_instance = True

    ingredient = fields.Nested(IngredientSchema)

class RecipeStepSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RecipeStepModel
        include_relationships = True
        load_instance = True

class RecipeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RecipeModel
        include_relationships = True
        load_instance = True
        
    steps = fields.Nested(RecipeStepSchema, many=True)
    ingredients = fields.Nested(RecipeIngredientSchema, many=True)
