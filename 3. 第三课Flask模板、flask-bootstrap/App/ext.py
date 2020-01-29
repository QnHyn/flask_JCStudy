from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from flask_bootstrap import Bootstrap

models = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    # 懒加载模型
    models.init_app(app=app)
    migrate.init_app(app, models)
    Session(app)
    Bootstrap(app)

