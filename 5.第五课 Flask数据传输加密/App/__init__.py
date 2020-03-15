from flask import Flask
from App.views import blue
from App.ext import init_ext
from App.settings import envs


def create_app(env):
    app = Flask(__name__)
    app.register_blueprint(blue)
    app.config.from_object(envs.get(env))
    init_ext(app=app)
    return app
