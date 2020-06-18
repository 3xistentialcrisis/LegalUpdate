from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import (StringField, TextAreaField,
                    SubmitField, SelectField, ValidationError)
from wtforms.validators import Required, Email
from ..models import Client, Lawyers

# Lawyers Create Client File 
class CaseForm(FlaskForm):
full_name = StringField('Client Name',validators=[Required()])
    title = StringField('Case title',validators=[Required()])
    case = TextAreaField('Your Case')
    category = SelectField(u'Category', choices=[('Criminal', 'Criminal'), 
                                                ('Civil', 'Civil'),
                                                ('Divorce', 'Divorce'),
                                                ('Other', 'Other') ])
    submit = SubmitField('Submit')

#         def validate_email(self, lawyer_email):
# #         if lawyer_email.data != current_user.email:
# #             if Lawyers.query.filter_by(lawyer_email=lawyer_email.data).first():
# #                 raise ValidationError("You do not have permission to create a Client File!")
    
#Lawyers Create File Status
class CreateStatus(FlaskForm):
    title = StringField('Enter status title',validators=[Required()])
    content = TextAreaField('Status Content',validators=[Required()])
    lawyer_email = StringField('Enter the File Type', validators=[Required(), Email()])
    submit = SubmitField('Post')

    def validate_email(self, lawyer_email):
        if lawyer_email.data != current_user.email:
            if Lawyers.query.filter_by(lawyer_email=lawyer_email.data).first():
                raise ValidationError("You do not have permission to create a File Status!")
  
#Clients Comment on Status
class CommentForm(FlaskForm):
    comment = TextAreaField('Post Comment', validators=[Required()])
    submit = SubmitField('Submit')

#Client Update their Profile
class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us about yourself")
    submit = SubmitField("Update")