from flask import Blueprint, render_template
# 这里注意要导入models中的models，而不是刚刚注册的ext中的models
from App.models import *
import hashlib


# 申明一个蓝图对象
blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    #渲染模板和传参 {{ msg }}
    return render_template('index.html', msg="今天天气好")


@blue.route('/adduser')
def adduser():
    user = User()
    h = hashlib.md5()
    h.update('123456'.encode())
    print(h.hexdigest())
    user.username = 'root'
    user.password = h.hexdigest()
    models.session.add(user)
    models.session.commit()
    print(models.session)
    print(type(models.session))
    return '添加成功'


@blue.route('/addusers')
def addusers():
    users = []
    for i in range(5):
        user = User()
        user.username = 'bili%d'% i
        user.password = '123456'
        users.append(user)
    models.session.add_all(users)
    models.session.commit()
    return '添加多条成功'


@blue.route('/deleteuser')
def deleteuser():
    user = User.query.first()
    models.session.delete(user)
    models.session.commit()
    return '删除数据成功'


@blue.route('/updateuser')
def updateuser():
    user = User.query.first()
    user.username = 'root'
    # 修改数据后重新保存
    models.session.add(user)
    models.session.commit()
    return '修改数据成功'


@blue.route('/addanimal')
def addanimal():
    dog = Dog()
    dog.u_name = '阿拉斯加2'
    cat = Cat()
    cat.u_name = '加菲猫2'
    models.session.add(dog)
    models.session.add(cat)
    models.session.commit()
    return "添加成功"


@blue.route('/getcat')
def getcat():
    #cats = Cat.query.filter(Cat.id.__gt__(2)).all()
    #cats = Cat.query.filter(Cat.id == (5)).all()
    #cats = Cat.query.filter(Cat.u_name.contains('猫')).all()
    #cats = Cat.query.filter(Cat.id.in_([1, 5, 6])).all()
    #cats = Cat.query.order_by(Cat.id.desc()).all()
    # offset和limit不区分顺序，怎么写都按offset先跳过在限制
    #cats = Cat.query.offset(1).limit(2).all()
    #cats = Cat.query.order_by("id").offset(1).limit(2).all()
    # BaseQuery的__str__方法, 会把它转为sql语句
    #cats = Cat.query.order_by("id").offset(1).limit(2).all()
    cats = Cat.query.filter_by(id=5).all()
    print(cats)
    print(type(cats))
    #render_template('cat.html', cat=cats)
    return "成功"


@blue.route('/getdog')
def getdog():
    from flask import request
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 4, type=int)
    dogs = Dog.query.offset(per_page * (page - 1)).limit(per_page)
    print(dogs)
    print(type(dogs))
    return "成功"


@blue.route('/getdogwithpage/')
def getdogwithpage():
    #dogs = Dog.query.paginate().items
    #render_template('dog.html', dog=cdogs)
    # 传分页器过去而不是数据过去
    pagination = Dog.query.paginate()
    render_template('dog.html', pagination=pagination)


@blue.route('/addcustomer')
def add_customer():
    import random
    costumer = Customer()
    costumer.c_name = '剁手党%d' % random.randrange(1000)
    models.session.add(costumer)
    models.session.commit()
    return "添加成功"


@blue.route('/addaddress')
def add_address():
    import random
    address = Address()
    address.a_position = '上海%d' % random.randrange(1000)
    address.a_customer_id = Customer.query.order_by(Customer.id.desc()).first().id
    models.session.add(address)
    models.session.commit()
    return "添加成功"


@blue.route('/get_customer')
def get_customer():
    # 获取id=1的地址的客户
    address = Address.query.get_or_404(1)
    customer = Customer.query.get(address.a_customer_id)
    return customer.c_name


@blue.route('/get_addr/')
def get_addr():
    # 客户1的所有地址
    customer = Customer.query.get(1)
    #addresses = Address.query.filter_by(a_customer_id=customer.id)
    # relationship 通过customer直接获取得到一个列表
    addresses = customer.address
    print(addresses)
    for addr in addresses:
        print(addr.a_position)
    return '获取成功'


from .ext import cache
@blue.route('/get_addrwithconn/')
@cache.cached(timeout=60)
def get_addrwithconn():
    from sqlalchemy import not_,  or_
    addresses = Address.query.filter(not_(or_(Address.a_customer_id.__eq__(1), Address.a_position.endswith('5'))))
    print(addresses)
    print('从数据库中查询')
    for addr in addresses:
        print(addr.a_position)
    #return render_template('Address.hmtl', addresses=addresses)
    return '获取成功'