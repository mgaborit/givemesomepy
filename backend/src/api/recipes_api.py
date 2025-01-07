from flask import Blueprint

from models.recipe import Recipe

recipes_bp = Blueprint('recipes_bp', __name__, url_prefix='/recipes')

@recipes_bp.route('', methods=['GET'])
def get_recipes():
    return [r.serialize(full_detail=False) for r in Recipe.query.all()]

@recipes_bp.route('', methods=['POST'])
def add_recipe():
    return Recipe.query.get(4).serialize()

@recipes_bp.route('<int:recipe_id>', methods=['GET'])
def find_recipe(recipe_id):
    return Recipe.query.get(recipe_id).serialize()
