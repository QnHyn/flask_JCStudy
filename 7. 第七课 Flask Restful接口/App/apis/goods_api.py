from flask import request
from flask_restful import Resource, fields, marshal_with, marshal, abort, reqparse

from App.models import Goods

goods_fields = {
    "id": fields.Integer,
    "name": fields.String(attribute='g_name'),
    "g_price": fields.Float,
    'uri': fields.Url('single_goods', absolute=True)
}

single_goods_fields = {
    "data": fields.Nested(goods_fields),
    "status": fields.Integer,
    "msg": fields.String,
}

multi_goods_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(goods_fields)),
    "desc": fields.String(default='success'),
    "number":fields.Integer
}


parser = reqparse.RequestParser()
parser.add_argument("g_name", type=str, required=True, help="please input g_name")
parser.add_argument("g_price", type=float, help="please input number")
parser.add_argument("mu", action="append")
parser.add_argument('rname', dest="name")
parser.add_argument("OUTFOX_SEARCH_USER_ID_NCOO", dest="lo", action="append", location=["cookies", "args"])
parser.add_argument("User-Agent",dest="ua", location="headers")


class GoodsListResource(Resource):

    # @marshal_with(multi_goods_fields)
    def get(self):
        args = parser.parse_args()
        print(args.get("lo"))
        print(args.get("ua"))
        goods_list = Goods.query.all()

        data = {
            "status": 200,
            "msg": "ok",
            "data": goods_list,
            'desc': "Get Ok"
        }

        return marshal(data, multi_goods_fields)

    @marshal_with(single_goods_fields)
    def post(self):
        # g_name = request.form.get('g_name')
        # g_price = request.form.get('g_price')
        args = parser.parse_args()
        g_name = args.get('g_name')
        g_price = args.get('g_price')
        print(args.get('mu'))
        print(args.get('name'))
        goods = Goods()
        goods.g_name = g_name
        goods.g_price = g_price
        if not goods.save():
            abort(400)
        """
            JSON
                Response
                
            格式
                单个对象
                
                {
                    "status": 200,
                    "msg"   : "ok",
                    "data"  :{
                        "property": "value",
                        "property": "value",
                        "property": "value",
                    }
                    
                }
                
                多个对象，列表对象
                {
                    "status": 200,
                    "msg"   : "ok",
                    "data"  : [
                        {
                                "property": "value",
                                "property": "value",
                                "property": "value"
                        },
                        {
                                "property": "value",
                                "property": "value",
                                "property": "value"
                        },
                        {
                                "property": "value",
                                "property": "value",
                                "property": "value"
                        },
                        
                    ]
                
                }
        """

        data = {
            "msg": "create success",
            "status": 201,
            # "data": marshal(goods, goods_fields)
            "data": goods
        }

        return data


class GoodsResource(Resource):

    @marshal_with(single_goods_fields)
    def get(self, id):

        goods = Goods.query.get(id)

        data = {
            "status": 200,
            "msg": "ok",
            "data": goods
        }

        return data

    def delete(self, id):

        goods = Goods.query.get(id)

        if not goods:
            # abort(404)
            abort(404, message="goods doesn't exist", msg="fail")

        if not goods.delete():
            abort(400)

        data = {
            "msg": "delete success",
            "status": 204
        }

        return data

    def put(self, id):

        goods = Goods.query.get(id)

        if not goods:

            abort(404)

        g_price = request.form.get('g_price')

        g_name = request.form.get('g_name')

        goods.g_price = g_price

        goods.g_name = g_name

        if not goods.save():
            abort(400)

        data = {
            "msg": "put ok",
            "status": 201,
            "data": goods
        }

        return marshal(data, single_goods_fields)

    @marshal_with(single_goods_fields)
    def patch(self, id):

        goods = Goods.query.get(id)

        if not goods:
            abort(404)

        g_price = request.form.get('g_price')

        g_name = request.form.get('g_name')

        goods.g_price = g_price or goods.g_price

        goods.g_name = g_name or goods.g_name

        if not goods.save():
            abort(400)

        data = {
            "msg": "put ok",
            "status": 201,
            "data": goods
        }

        return data