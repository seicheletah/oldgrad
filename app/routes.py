from app import oldgrad
from flask import render_template

@oldgrad.route('/')
@oldgrad.route('/index')
def index():
    return render_template('index.jinja')

@oldgrad.route('/login')
def login():
    return render_template('login.jinja')

@oldgrad.route('/events')
def events():
    return render_template('index.jinja')

@oldgrad.route('/jobs')
def jobs():
    return render_template('index.jinja')

@oldgrad.route('/alumni')
def alumni():
    return render_template('index.jinja')

@oldgrad.route('/donations')
def donations():
    return render_template('index.jinja')
