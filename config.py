import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'verysecretkey'
    DATABASE = os.environ.get('DATABASE')