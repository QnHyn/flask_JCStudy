from flask import request


def load_middleware(app):
    """
    统计
    优先级
    反爬
    频率
    用户认证
    用户权限
    """
    @app.before_request
    def before():
        print("中间件", request.url)

    @app.after_request
    def after(res):
        # 一定要有返回
        print("after", res)
        print(type(res))
        return res