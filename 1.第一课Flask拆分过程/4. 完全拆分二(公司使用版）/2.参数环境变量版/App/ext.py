from flask_sqlalchemy import SQLAlchemy

models = SQLAlchemy()


def init_ext(app):
    # 懒加载模型
    models.init_app(app=app)

