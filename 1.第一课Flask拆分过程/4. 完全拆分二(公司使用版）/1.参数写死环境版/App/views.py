from flask import Blueprint, render_template
# 这里注意要导入models中的models，而不是刚刚注册的ext中的models
from App.models import models


# 申明一个蓝图对象
blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    #渲染模板和传参 {{ msg }}
    #return render_template('index.html', msg="今天天气好")
    return 'Hello Flask'


@blue.route('/createdb')
def createdb():
    models.create_all()
    return '创建数据表成功'