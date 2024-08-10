from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from application.config import appConfig, configure_logging
from application.service import response
from application.settings import load_setting, save_setting
from application.database import db
from application.utils import get_user_message

from ollama import chat

app = Flask(__name__)
app.config.from_object(appConfig)

# logging
logger = configure_logging()
logger.info(f"Config: {str(appConfig)}")


def init_db(app: Flask, db: SQLAlchemy):
    from application.models import Setting, ChatQuery, ChatResponse

    with app.app_context():
        db.create_all()
        db.session.commit()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["GET", "POST"])
def get_response():
    user_msg = get_user_message(request.form["msg"])
    model = app.config.get("OLLAMA_MODEL")
    logger.info(f'Using model: {model} user msg; {user_msg}')
    return response(model, user_msg)


@app.route("/settings/<key>", methods=["GET"])
def get_setting(key):
    value = load_setting(key)
    if value:
        return jsonify({key: value}), 200
    else:
        return jsonify({"error": "Setting not found"}), 404


@app.route("/settings/<key>", methods=["POST"])
def update_setting(key):
    value = request.json.get("value")
    if value:
        save_setting(key, value)
        return jsonify({"message": "Setting saved"}), 200
    else:
        return jsonify({"error": "Value is required"}), 400


@app.route("/test", methods=["GET"])
def test():
    messages = get_user_message("Why is the sky blue?")
    print(str(messages))
    response = chat("llama3.1", messages=messages)
    res = response["message"]["content"]
    logger.info(res)
    return res


def start_app():
    init_db(app, db)
    app.run(host="0.0.0.0", port=8080, debug=True)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


if __name__ == "__main__":
    start_app()
