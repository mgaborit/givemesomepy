from flask import Flask
from flask_cors import CORS
from markupsafe import escape
import sqlalchemy as db

app = Flask(__name__)
CORS(app)

engine = db.create_engine("postgresql://postgres:postgres@localhost:5432/test_db")

@app.route('/recipes')
def get_recipes():
    conn = engine.connect()
    try:
        cur = conn.execute(db.text("SELECT * FROM recipe;"))
        result = []
        for record in cur.fetchall():
            result.append({'name': record[1]})
    finally:
        conn.close()
    return result
