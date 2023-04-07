from flask import Flask
from .routes.gpt_routes import gpt_routes

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'my-secret'

    app.register_blueprint(gpt_routes, url_prefix='/')
    return app