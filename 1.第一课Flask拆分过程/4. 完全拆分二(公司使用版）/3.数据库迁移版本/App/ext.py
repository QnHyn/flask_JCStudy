from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

models = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    # 懒加载模型
    models.init_app(app=app)
    migrate.init_app(app, models)

