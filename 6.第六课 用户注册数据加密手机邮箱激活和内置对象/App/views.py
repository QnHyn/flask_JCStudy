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


# 统计、做反扒、优先级、频率反扒、用户登录的判断
from flask import request
from flask import current_app
# 这里直接导入的config, 并不是四大内置对象的config.
# 从flask 中导入 request
@blue.before_request
def before():
    conf = current_app.config
    keys = conf.keys()
    for key in keys:
        print(key, conf[key])
    print(request.url)


# 界面统一的动态加载、DebugToBar
@blue.after_request
def after(res):
    print("after", res)
    print(type(res))
    return res


from App.models import Student
from flask import redirect, url_for, flash


@blue.route('/student/register/', methods=['GET', 'POST'])
def student_register():
    if request.method == "GET":
        return render_template("student_register.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # hash_pwd = generate_password_hash(password)
        # 前端输入验证码
        code = request.form.get("code")
        # 缓存中的验证码
        cache_code = cache.get(username)
        if code != cache_code:
            return "验证失败"
        student = Student()
        student.s_name = username
        student.s_password = password
        db.session.add(student)
        db.session.commit()
        return "注册成功"


@blue.route('/student/login/', methods=['GET', 'POST'])
def student_login():
    if request.method == "GET":
        return render_template("Student_Login.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        student = Student.query.filter(Student.s_name.__eq__(username)).first()
        # if student and check_password_hash(student.s_password, password):
        #     return "Login Success"
        # 把密码检测定义到models中
        if student and Student.check_password(password):
            return "Login Success"
        flash("用户名或密码错误")
        return redirect(url_for("blue.student_login"))


from flask_mail import Message
from App.ext import mail


@blue.route("/sendmail/")
def send_mail():
    msg = Message("FLask Email", recipients=["18855953229@163.com", ])
    msg.body = "哈哈 FLask不过如此"
    msg.html = "<h2>我靠 我真是天才呀</h2>"
    mail.send(message=msg)
    return "邮件发送成功！！"


from App.utils import send_verify_code
from App.ext import cache
from flask import jsonify


@blue. route('/sendcode/')
def send_code():
    phone = request.args.get("phone")
    username = request.args.get("username")
    resp = send_verify_code(phone)
    print(resp.json())
    result = resp.json()
    if result.get("code") == 200:
        obj = result.get("obj")
        cache.set(username, obj)
        data = {
            "msg": "ok",
            "status": 200
        }
        return jsonify(data)
    data = {
        "msg": "fail",
        "status": 400
    }
    return jsonify(data)