from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User


def email_exits(form, feild):
    email = User.query.filter_by(user_email=feild.data).first()
    if email:
        raise ValidationError('email already exists')


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(3,15, message='between 3 to 15 characters')])
    email = StringField('Email', validators=[DataRequired(), Email(), email_exits])
    password = PasswordField('Password', validators=[DataRequired(), Length(5), EqualTo('confirm', message='passwords must match')])
    confirm = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('stay logged-in')
    submit = SubmitField('LogIn')