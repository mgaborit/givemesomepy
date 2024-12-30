import re
from datetime import datetime

from flask import Flask
from flask_cors import CORS

from database import db_session, init_db
from models.recipe import Recipe

# create the app
app = Flask(__name__)

CORS(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/recipes')
def get_recipes():
    return [r.as_dict() for r in Recipe.query.all()]

if __name__ == "__main__":
    init_db()
    app.run(debug=True)