from flask import Blueprint, render_template
from App.models import db


# 申明一个蓝图对象
blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    #渲染模板和传参 {{ msg }}
    #return render_template('index.html', msg="今天天气好")
    return 'Hello Flask'


@blue.route('/createdb')
def createdb():
    db.create_all()
    return '创建数据表成功'