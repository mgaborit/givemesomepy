from flask import Flask
from flask_cors import CORS
from markupsafe import escape
import sqlalchemy as db

app = Flask(__name__)
CORS(app)

engine = db.create_engine("postgresql://postgres:secret@db:5432/postgres")

@app.route('/recipes')
def get_recipes():
    try:
        conn = engine.connect()
        try:
            cur = conn.execute(db.text("SELECT * FROM recipe;"))
            result = []
            for record in cur.fetchall():
                result.append({'name': record[1]})
        finally:
            conn.close()
    except Exception as e:
        return str(e)
    return result

if __name__ == "__main__":
    app.run(debug=True)