from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from application.logging_config import configure_logging



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../rag.db'
db = SQLAlchemy(app)

logger = configure_logging()

@app.route('/test', methods=['GET'])
def test():
    return "Hello World!"

def start_app():
    app.run(host="0.0.0.0", port=8080, debug=True)


if __name__ == "__main__":
    start_app()
