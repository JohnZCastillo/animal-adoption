from flask import Flask,render_template
from .routes.auth import auth
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from .model.user import User
from .model.database import db
from .model.animal import Animal
from flask_login import LoginManager,login_required
from .routes.animal import animal

import os

env_path = os.path.join(os.path.dirname(__file__),'.env')
load_dotenv(env_path)
    
def create_app():

    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_DEVELOPMENT')    
    app.secret_key = os.getenv('SECRET')
    
    db.init_app(app)
    
    migrate = Migrate(app,db)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        try:
            return db.session.get_one(User,id)
        except:
            return None
        
    app.register_blueprint(auth)
    app.register_blueprint(animal)
    
    @app.route('/')
    @app.route('/homepage')
    @login_required
    def homepage():
        return render_template('/pages/homepage.html')
    
    
    return app