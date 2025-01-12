import json
from flask import Blueprint, request

from models.recipe import RecipeModel

recipes_bp = Blueprint('recipes_bp', __name__, url_prefix='/recipes')

@recipes_bp.route('', methods=['GET'])
def find_recipes():
    return [r.serialize(full_detail=False) for r in RecipeModel.query.all()]

@recipes_bp.route('', methods=['POST'])
def add_recipe():
    data = json.loads(request.data)
    recipe = RecipeModel(**data)
    return recipe.serialize()

@recipes_bp.route('<int:recipe_id>', methods=['GET'])
def find_recipe_by_id(recipe_id):
    return RecipeModel.query.get(recipe_id).serialize()
