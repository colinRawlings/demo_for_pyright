from flask import Flask

def create_app(test_config: int):

    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def root():
        return 'at the root'

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

def app_factory():
    return create_app(1)