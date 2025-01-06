from flask import Flask
from flask_cors import CORS

from database import db_session
from api.recipes_api import recipes_bp

# create the app
app = Flask(__name__)
app.register_blueprint(recipes_bp)

CORS(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
