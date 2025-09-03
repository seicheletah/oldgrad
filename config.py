import os

databasedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'verysecretkey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE') or 'sqlite:///' + os.path.join(databasedir, 'oldgrad_db.db')