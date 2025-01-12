import json
from flask import Blueprint, request

from models.ingredient import IngredientModel

ingredient_bp = Blueprint('ingredient_bp', __name__, url_prefix='/ingredients')

@ingredient_bp.route('', methods=['GET'])
def find_ingredients():
    return [i.serialize() for i in IngredientModel.query.all()]

@ingredient_bp.route('', methods=['POST'])
def add_ingredient():
    data = json.loads(request.data)
    ingredient = IngredientModel(**data)
    return ingredient.serialize()

@ingredient_bp.route('<int:ingredient_id>', methods=['GET'])
def find_ingredient_by_id(ingredient_id):
    return IngredientModel.query.get(ingredient_id).serialize()