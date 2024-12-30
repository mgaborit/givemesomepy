from flask import Blueprint

from models.recipe import Recipe

recipes_bp = Blueprint('recipes_bp', __name__, url_prefix='/recipes')

@recipes_bp.route('')
def get_recipes():
    return [r.as_dict() for r in Recipe.query.all()]
