from flask import Flask
from config import Config

oldgrad = Flask(__name__)
oldgrad.config.from_object(Config)

from app import routes