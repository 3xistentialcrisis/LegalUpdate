from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Required, Email, EqualTo, Length
from ..models import Client

class RegistrationForm(FlaskForm):
    client_email = StringField('Client Email Address',validators=[Required(),Email()])
    client_name = StringField('Client name',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')
    
    
    def validate_email(self, data_field):
        if Client.query.filter_by(email = data_field.data).first():
            raise ValidationError("There is a client account with that email")
        
    def validate_username(self,data_field):
        if Client.query.filter_by(clientname = data_field.data).first():
            raise ValidationError("That client_username is taken")
        
class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(),Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class ResetPassword(FlaskForm):
    email = StringField('Email', validators=[Required(), Email()])
    submit = SubmitField('Reset Password')

class NewPassword(FlaskForm):
    password = PasswordField('Password',validators=[Required()])
    password_repeat = PasswordField('Repeat Password', validators=[Required(),EqualTo('password')])
    submit = SubmitField('Change Password')
    