#for running functions when you load a page
from app import oldgrad
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sql
from app import oldgrad_db
from app.models import User
from urllib.parse import urlsplit

@oldgrad.route('/')
@oldgrad.route('/index')
def index():
    return render_template('index.jinja')

@oldgrad.route('/login', methods=['GET', 'POST'])
def login(): #for all login related issues
    if current_user.is_authenticated: #already logged in
        return redirect(url_for('events'))
    loginform = LoginForm()
    if loginform.validate_on_submit(): #validate form on clicking submit
        user = oldgrad_db.session.scalar(sql.select(User).where(User.email == loginform.email.data)) #search database for user with the email
        if user is None or not user.check_password(loginform.password.data): #check the password hash
            flash('Invalid email or password') #print alert
            return redirect(url_for('login'))
        login_user(user, remember=loginform.remember_me.data) #log user in
        flash(f'Login successful, {current_user.name}')
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '': #check for url tampering
            next_page = url_for('events')
        return redirect(url_for(next_page[1:])) #added string slicing
    return render_template('login.jinja', loginform=loginform)

@oldgrad.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@oldgrad.route('/events')
@login_required
def events():
    return render_template('events.jinja')

@oldgrad.route('/jobs')
@login_required
def jobs():
    return render_template('index.jinja')

@oldgrad.route('/alumni')
@login_required
def alumni():
    return render_template('index.jinja')

@oldgrad.route('/donations')
@login_required
def donations():
    return render_template('index.jinja')
