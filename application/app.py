from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from application.config import appConfig, configure_logging

app = Flask(__name__)
app.config.from_object(appConfig)
db = SQLAlchemy(app)

# logging
logger = configure_logging()
logger.info(f'Config: {str(appConfig)}')

# configuration

# Import the models

# Create the database and tables

def init_db(app: Flask, db: SQLAlchemy):
    from application.models import Setting, ChatQuery, ChatResponse
    with app.app_context():
        db.create_all()
        db.session.commit()


from application.ollamallm import OllamaLLM
from ollama import chat




@app.route('/test', methods=['GET'])
def test():
    messages = [  {
        'role': 'user',
        'content': 'Why is the sky blue?',
        },
    ]
    response = chat('llama3.1', messages=messages)
    res = response['message']['content']
    print(response['message']['content'])
    logger.info(res)
    return res

def start_app():
    init_db(app, db)
    app.run(host="0.0.0.0", port=8080, debug=True)


if __name__ == "__main__":
    start_app()
