import base64

from flask import Blueprint, render_template
from App.models import db, News
import random


# 申明一个蓝图对象
blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    return 'Hello Flask'


@blue.route('/createdb')
def createdb():
    db.create_all()
    return '创建数据表成功'


@blue.route('/addnews/')
def add_news():
    news = News()
    news.n_title = "小搞怪 %d" % random.randrange(1000)
    news.n_content = "社会福利 %d" % random.randrange(100)
    db.session.add(news)
    db.session.commit()
    return '添加新闻列表成功'


@blue.route('/getnews/')
def get_news():
    news_list = News.query.all()
    news_content = render_template("news_content.html", news_list=news_list)
    # 字符串转二进制 加密后成二进制在转成字符串
    encode_content = base64.standard_b64encode(news_content.encode("utf-8")).decode("utf-8")
    print(encode_content)
    # 拼串 加入和前端约定好的前后字符串
    add_content_encode_content = "CHKa2GFL1twhMDhEZVfDfU2DoZHCLZk" + encode_content + "pOq3kRIxs26rmRtsUTJvBn9Z"
    print(add_content_encode_content)
    encode_content_twice = base64.standard_b64encode(add_content_encode_content.encode("utf-8")).decode("utf-8")
    print(encode_content_twice)
    return render_template('news_list.html', news_content=news_content, encode_content_twice=encode_content_twice)



@blue.route('/getshow/')
def get_show():
    import os, time
    from flask import request
    from App.settings import BASE_DIR
    # 接收前端的时间参数
    t = request.args.get("t")
    print(t)
    # python中以秒为计数单位，其他语言以毫秒计数单位
    c = time.time() * 1000
    # 捕获异常(防止手动乱输入)
    try:
        t = int(t)
    except:
        return "2"
    # 1秒之内请求可以正常返回js
    if c > t and c - t < 1000:
        with open(os.path.join(BASE_DIR, "static\js\show.js"), 'r') as file:
            js_content = file.read()
            print(js_content)
        return js_content
    else:
        return "1"