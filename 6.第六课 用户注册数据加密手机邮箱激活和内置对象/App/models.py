from App.ext import db

# 新闻数据模型
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    n_title = db.Column(db.String(32))
    n_content = db.Column(db.String(256))


from werkzeug.security import check_password_hash, generate_password_hash


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(15), unique=True)
    # 把s_password变成私有属性
    _s_password = db.Column(db.String(256))
    s_phone = db.Column(db.String(32), unique=True)

    @property
    def s_password(self):
        raise Exception("Error Action Password Cant be access")

    @s_password.setter
    def s_password(self, value):
        self._s_password = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self._s_password, password)