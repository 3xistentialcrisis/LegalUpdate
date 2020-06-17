from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SubmitField,ValidationError
from wtforms.validators import Required,Email
from flask_login import current_user
from ..models import Lawyers

#Lawyers Create Client File
class CreateFile(FlaskForm):
    client_name = StringField('Enter the Client Name', validators=[Required()])
    file_name = StringField('Enter the File Name', validators=[Required()])
    file_type = StringField('Enter the File Type', validators=[Required()])
    lawyer_email = StringField('Enter the File Type', validators=[Required(), Email()])
    submit = SubmitField('Save')

    def validate_email(self, email):
        if email.data != current_user.email:
            if Lawyers.query.filter_by(lawyer_email=email.data).first():
                raise ValidationError("You do not have permission to create a Client File!")

#Lawyers Create File Status
class CreateStatus(FlaskForm):
    title = StringField('Enter status title',validators=[Required()])
    content = TextAreaField('Status Content',validators=[Required()])
    lawyer_email = StringField('Enter the File Type', validators=[Required(), Email()])
    submit = SubmitField('Post')

    def validate_email(self, email):
        if email.data != current_user.email:
            if Lawyers.query.filter_by(lawyer_email=email.data).first():
                raise ValidationError("You do not have permission to create a File Status!")