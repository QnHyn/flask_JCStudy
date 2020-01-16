from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_model(app):
    db.init_app(app=app)


# 会员数据模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 编号
    username = db.Column(db.String(100), unique=True)  # 昵称
    password = db.Column(db.String(100))  # 密码
