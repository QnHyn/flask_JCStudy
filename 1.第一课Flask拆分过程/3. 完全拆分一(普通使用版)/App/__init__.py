from flask import Flask
from App.views import blue
from App.ext import init_ext


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blue)
    # uri数据库+驱动://用户 名:密码@主机:端口/具体哪一个库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask_test'
    # 保持兼容性
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_ext(app=app)
    return app
