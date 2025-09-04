from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
import sqlalchemy as sql
from app import oldgrad_db
from app.models import User

class LoginForm(FlaskForm): #for log in page form
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')

class RegistrationForm(FlaskForm): #for creating new account form
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    rep_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    branch = StringField('Branch', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    passout_year = StringField('Passout year', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email: StringField):
        user = oldgrad_db.session.scalar(sql.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError('Please use diffrent email address.')
