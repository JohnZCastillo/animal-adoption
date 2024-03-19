from flask import Flask
from .routes.public import public
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from .model.user import User
from .model.database import db

import os

def create_app():

    env_path = os.path.join(os.path.dirname(__file__),'.env')
    load_dotenv(env_path)
    
    app = Flask(__name__)

    # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('db')

    # db.init_app(app)
        
    # migrate = Migrate(app,db)
    
    app.register_blueprint(public)
    
    @app.route('/test')
    def test():
        return os.getenv('db','hello')
    
    return app