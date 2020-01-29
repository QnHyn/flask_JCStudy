from flask import Blueprint, render_template, redirect, url_for, request, make_response, Response, abort, session
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


# 传 整型参数
@blue.route('/users/<int:id>/')
def users(id):
    # 将参数约束为数值类型, 浏览器写其他参数报错
    print(id)
    return 'Get Int %s' % str(id)


# 传 字符串参数 不设约束时默认(string).
# 传空或者参数中有/ 。报错找不到。
@blue.route('/getinfo/<string:token>/')
@blue.route('/getuuid/<uuid:token>/')
def getinfo(token):
    print(token)
    return 'Get String Success %s' % (token)


# 传 路径参数
# 这里同样不能传空
@blue.route('/getpath/<path:address>/')
def getpath(address):
    print(address)
    return 'Get PATH Successs {}'.format(address)


# 传 UUID参数
@blue.route('/getuuid/<uuid:uu>/')
def getuuid(uu):
    # 网上找一个uuid测试:d6132fce-910d-4261-85c3-e537ce055e05
    print(uu)
    return 'Get UUID Success {}'.format(uu)


# 传 any参数 穷举(只能选a或b)
@blue.route('/getany/<any(a,b):an>')
def getany(an):
    print(an)
    return 'Get Any Success {}'.format(an)


@blue.route('/getnotice/<string:notice>/')
@blue.route('/getnotice/<uuid:notice>/')
def getnotice(notice):
    # 一个函数上面可以映射多个路由。
    # 可以出现相同的两个路由不报错。访问时以第一个路由为主。
    print(notice)
    return 'Get notice Success %s' % (notice)


# 重定向函数
@blue.route('/redirect/')
def red():
    # 这种属于 硬编码
    return redirect('/')


@blue.route('/redirect1/')
def red1():
    # 这种属于 反向解析
    # 有蓝图 蓝图 + 函数
    # 没有蓝图 直接路由函数
    return redirect(url_for('blue.index'))


@blue.route('/redirect2/')
def red2():
    # 反向路由传参
    return redirect(url_for('blue.getany', an='a'))


# Request对象由Flask框架生成
@blue.route('/getrequest/')
def get_request():
    print(request.host)
    print(request.url)
    if request.method == 'GET':
        print('GET')
    return 'Get request Success '


# args 接收GET请求参数
# http://127.0.0.1:5000/sendrequest/?user=Rock&password=rock1204
@blue.route('/sendrequest/')
def send_request():
    # 列表下把参数变为元组
    print(request.args) #ImmutableMultiDict([('user', 'Rock'), ('password', 'rock1204')])
    print(type(request.args))
    return 'Send request Success '


# form接收POST参数
# 用PostMan模拟请求
@blue.route('/sendrequest1/', methods=['GET', 'POST'])
def send_request1():
    # POST方式时GET的的参数也能获取到
    print(request.args)
    print(type(request.args))
    print(request.form)
    print(type(request.form))
    print(request.headers)
    return 'Send request Success '


# Response 对象
@blue.route('/getresponse/')
def get_response():
    # return 'Hello sleeping ', 404  # 返回状态码404
    # result = render_template('HelloURL.html')
    # print(result)
    # print(type(result))
    # return result
    # response = make_response('<h1>帅吗？</h1>')
    # print(response, type(response)) #<Response 18 bytes [200 OK]> <class 'flask.wrappers.Response'>
    abort(404) #终止请求
    response = Response('自己造一个Response')
    return response


@blue.errorhandler(404)
def handler_error(error):
    print(error)
    print(type(error))
    return 'What'


@blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        response = Response('登录成功%s' % username)
        # 设置Cookie
        #response.set_cookie('username', username)
        # 设置Session
        # 报错The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
        session['username'] = username
        return response


# 获取cookie中的信息
@blue.route('/mine/')
def mine():
    username = session.get('username')
    return '欢迎回来'


@blue.route('/students/')
def students():
    student_list = [i for i in range(10)]
    return render_template('Students.html', student_list=student_list, a=5, b=5)


@blue.route('/user_register')
def user_register():
    return render_template('user/user_register.html', title='用户注册')


@blue.route('/user_register2')
def user_register2():
    return render_template('user/user_register2.html', title='用户注册2')


@blue.route('/index')
def index1():
    return render_template('index.html')
