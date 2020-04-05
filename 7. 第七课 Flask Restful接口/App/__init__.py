from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.middleware import load_middleware
from App.settings import envs


def create_app(env):
    app = Flask(__name__)

    app.config.from_object(envs.get(env))

    init_ext(app)
    # 只要路由相关的 都写在__init__.py中 不要卸载ext中
    init_api(app=app)

    load_middleware(app)

    return app