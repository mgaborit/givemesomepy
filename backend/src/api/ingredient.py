import json
from flask import Blueprint, request

from models.ingredient import IngredientModel
from schemas.ingredient import IngredientSchema
from database import db_session

ingredient_bp = Blueprint('ingredient_bp', __name__, url_prefix='/api/ingredients')

@ingredient_bp.route('', methods=['GET'])
def find_ingredients():
    schema = IngredientSchema(many=True)
    return schema.dump(IngredientModel.query.all())

@ingredient_bp.route('', methods=['POST'])
def add_ingredient():
    schema = IngredientSchema()
    data = json.loads(request.data)
    ingredient = schema.load(data, session=db_session)
    db_session.add(ingredient)
    db_session.commit()
    return 'OK'

@ingredient_bp.route('<int:ingredient_id>', methods=['GET'])
def find_ingredient_by_id(ingredient_id):
    sedchema = IngredientSchema()
    return schema.dump(IngredientModel.query.get(ingrient_id))

@ingredient_bp.route('<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient_by_id(ingredient_id):
    IngredientModel.query.filter(IngredientModel.id == ingredient_id).delete()
    db_session.commit()
    return 'OK'
