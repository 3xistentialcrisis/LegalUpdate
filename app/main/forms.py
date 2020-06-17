from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,TextAreaField, SubmitField,ValidationError
from wtforms.validators import Required,Email
from flask_login import current_user
from ..models import User

class CreateFile(FlaskForm):
    client_name = StringField('Enter the Client Name', validators=[Required()])
    file_name = StringField('Enter the File Name', validators=[Required()])
    file_type = StringField('Enter the File Type', validators=[Required()])
    submit = SubmitField('Save')

class CreateStatus(FlaskForm):
    title = StringField('Enter status title',validators=[Required()])
    content = TextAreaField('Blog Content',validators=[Required()])
    submit = SubmitField('Post')


