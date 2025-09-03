from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

oldgrad = Flask(__name__)
oldgrad.config.from_object(Config)
oldgrad_db = SQLAlchemy(oldgrad)
migrate = Migrate(oldgrad, oldgrad_db)

from app import routes, models