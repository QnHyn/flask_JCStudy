from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
from flask_caching import Cache

models = SQLAlchemy()
migrate = Migrate()
cache = Cache(config={
    "CACHE_TYPE": "simple"
})


def init_ext(app):
    # 懒加载模型
    models.init_app(app=app)
    migrate.init_app(app, models)
    DebugToolbarExtension(app=app)
    cache.init_app(app=app)


