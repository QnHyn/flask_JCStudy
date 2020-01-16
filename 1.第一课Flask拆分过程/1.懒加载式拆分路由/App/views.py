def init_route(app):
    @app.route('/')
    def index():
        return 'Hello Flask'
