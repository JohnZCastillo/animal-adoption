from flask import Flask
from .routes.public import public

def create_app():

    app = Flask(__name__)
    app.register_blueprint(public)
    
    return app
