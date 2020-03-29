from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
cache = Cache(
    config={
        "CACHE_TYPE":"redis"
    }
)


def init_ext(app):
    # 懒加载模型
    db.init_app(app=app)
    migrate.init_app(app, db)
    mail.init_app(app=app)
    cache.init_app(app=app)

