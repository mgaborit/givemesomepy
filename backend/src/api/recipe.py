import json
from flask import Blueprint, request

from database import db_session

from models.recipe import RecipeModel
from schemas.recipe import RecipeSchema

recipes_bp = Blueprint('recipes_bp', __name__, url_prefix='/api/recipes')

@recipes_bp.route('', methods=['GET'])
def find_recipes():
    schema = RecipeSchema(many=True)
    return schema.dump(RecipeModel.query.all())

@recipes_bp.route('', methods=['POST'])
def add_recipe():
    schema = RecipeSchema()
    data = json.loads(request.data)
    recipe = schema.load(data, session=db_session)
    db_session.add(recipe)
    db_session.commit()
    return 'OK'

@recipes_bp.route('<int:recipe_id>', methods=['GET'])
def find_recipe_by_id(recipe_id):
    schema = RecipeSchema()
    return schema.dump(RecipeModel.query.get(recipe_id))

@recipes_bp.route('<int:recipe_id>', methods=['PUT'])
def update_ingredient(recipe_id):
    schema = RecipeSchema()
    data = json.loads(request.data)
    schema.load(data, session=db_session, instance=RecipeModel.query.get(recipe_id))
    db_session.commit()
    return 'OK'

@recipes_bp.route('<int:recipe_id>', methods=['DELETE'])
def delete_ingredient_by_id(recipe_id):
    RecipeModel.query.filter(RecipeModel.id == recipe_id).delete()
    db_session.commit()
    return 'OK'
