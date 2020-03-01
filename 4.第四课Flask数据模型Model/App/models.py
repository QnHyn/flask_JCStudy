from App.ext import models


# 会员数据模型
class User(models.Model):
    # 修改表名
    __tablename__ = 'UserModel'
    id = models.Column(models.Integer, primary_key=True)  # 编号
    username = models.Column(models.String(100), unique=True)  # 昵称
    password = models.Column(models.String(100))  # 密码
    desc = models.Column(models.String(128), nullable=True)


# 如果继承类，只生成一张Animal表。不生成dog和cat表。dog和cat的字段集成在Animal表中。
class Animal(models.Model):
    # Django 中可以把类变成抽象类处理，这里也把类变为抽象类
    __abstract__= True
    id = models.Column(models.Integer, primary_key=True)
    u_name = models.Column(models.String(100), unique=True)


class Dog(Animal):
    d_tags = models.Column(models.Integer, default=4)


class Cat(Animal):
    c_tags = models.Column(models.String(32), default='fish')


class Customer(models.Model):
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    c_name = models.Column(models.String(16))
    address = models.relationship('Address', backref='customer', lazy=True)


class Address(models.Model):
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    a_position = models.Column(models.String(20))
    a_customer_id = models.Column(models.Integer, models.ForeignKey(Customer.id))