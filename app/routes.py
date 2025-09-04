#for running functions when you load a page
from app import oldgrad
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
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
            flash('Invalid email or password.') #print alert
            return redirect(url_for('login'))
        login_user(user, remember=loginform.remember_me.data) #log user in
        flash(f'Login successful, {current_user.name}.')
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
    return render_template('jobs.jinja')

@oldgrad.route('/alumni')
@login_required
def alumni():
    return render_template('alumni.jinja')

@oldgrad.route('/donations')
@login_required
def donations():
    return render_template('donations.jinja')

@oldgrad.route('/profile')
@login_required
def profile():
    return render_template('profile.jinja')

#optional account registration feature
@oldgrad.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: #already logged in
        return redirect(url_for('events'))
    registrationform = RegistrationForm()
    if registrationform.validate_on_submit():
        user = User(name=registrationform.name.data, email=registrationform.email.data, phone_number=registrationform.phone_number.data, branch=registrationform.branch.data, location=registrationform.location.data, passout_year=registrationform.passout_year.data)
        user.set_password(registrationform.password.data)
        oldgrad_db.session.add(user)
        oldgrad_db.session.commit()
        flash('Welcome to our community.')
        return redirect(url_for('index'))
    return render_template('register.jinja', registrationform=registrationform)
