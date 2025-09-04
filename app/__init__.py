from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

oldgrad = Flask(__name__) #flask App Instance
oldgrad.config.from_object(Config) #for inserting flask Config class in flask app instance
oldgrad_db = SQLAlchemy(oldgrad) #flask Database Instance
migrate = Migrate(oldgrad, oldgrad_db) #flask Database Migrate Instance
login_manager = LoginManager(oldgrad) #flask Login Manager Instance
login_manager.login_view = 'login' 

from app import routes, models