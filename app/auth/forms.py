from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, 
                    ValidationError, BooleanField)
from wtforms.validators import Required, Email, EqualTo
from ..models import Client

class SignUpForm(FlaskForm):
    full_name = StringField("Your Full Name", validators=[Required()])
    username = StringField("Your Username", validators=[Required()])
    email = StringField("Your Email Address", validators=[Required(), Email()])
    password = PasswordField("Password", validators=[Required(), 
                             EqualTo("password_confirm",message="Passwords must match")])
    password_confirm = PasswordField("Confirm Passwords", validators=[Required()])
    submit = SubmitField("Sign Up")

    #Custom email validation
    def validate_email(self, data_field):
        if Client.query.filter_by(email = data_field.data).first():
            raise ValidationError("There is an account with that email")

    #Custom username validation
    def validate_username(self, data_field):
        if Client.query.filter_by(username = data_field.data).first():
            raise ValidationError("That username is taken")

class LoginForm(FlaskForm):
    email = StringField("Your Email Address", validators=[Required(), Email()])
    password = PasswordField("Password", validators=[Required()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")