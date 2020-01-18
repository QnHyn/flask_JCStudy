from App.ext import models


# 会员数据模型
class User(models.Model):
    id = models.Column(models.Integer, primary_key=True)  # 编号
    username = models.Column(models.String(100), unique=True)  # 昵称
    password = models.Column(models.String(100))  # 密码
