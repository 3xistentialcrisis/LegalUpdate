from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, EqualTo, ValidationError
from ..models import Lawyers


class RegistrationForm(FlaskForm):
    lawyer_email = StringField('Your Email Address', validators=[Required(), Email()])
    lawyer_name = StringField('Enter your Name', validators=[Required()])
    department = StringField('Enter your Department', validators=[Required()])
    password = PasswordField('Password', validators=[Required(),
                                                     EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if Lawyers.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_email(self, data_field):
        if Lawyers.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
