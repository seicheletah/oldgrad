from app import oldgrad
from flask import render_template, flash, redirect
from app.forms import LoginForm

@oldgrad.route('/')
@oldgrad.route('/index')
def index():
    return render_template('index.jinja')

@oldgrad.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        flash(f'Welcome {loginform.username.data}!')
        return redirect('/index') #later needs to change to event
    return render_template('login.jinja', loginform=loginform)

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
