from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,TextAreaField, SubmitField,ValidationError
from wtforms.validators import Required,Email
from flask_login import current_user
from ..models import User

class CreateStatus(FlaskForm):
    title = StringField('Enter status title',validators=[Required()])
    content = TextAreaField('Blog Content',validators=[Required()])
    submit = SubmitField('Post')

class CreateFile(FlaskForm):
    username = StringField('Enter Your Username', validators=[Required()])
    email = StringField('Email Address', validators=[Required(), Email()])
    bio = TextAreaField('Write a few biographical facts about yourself.', validators=[Required()])
    profile_picture = FileField('profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Save')

    def validate_email(self, email):
        if email.data != current_user.email:
            if User.query.filter_by(email=email.data).first():
                raise ValidationError("This Email has already been registered!")

    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username=username.data).first():
                raise ValidationError("This username is not available")

