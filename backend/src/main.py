from flask import Flask
from flask_cors import CORS

from database import db_session, init_db
from api.recipes_api import recipes_bp

# create the app
app = Flask(__name__)
app.register_blueprint(recipes_bp)

CORS(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)