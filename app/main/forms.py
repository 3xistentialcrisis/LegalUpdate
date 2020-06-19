from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import (StringField, TextAreaField,
                    SubmitField, SelectField, ValidationError)
from wtforms.validators import Required, Email
from ..models import  Lawyers

# Lawyers Create Client File 
class CaseForm(FlaskForm):
    full_name = StringField('Lawyer Name',validators=[Required()])
    title = StringField('Case title',validators=[Required()])
    client_name = StringField('Client Name')
    case = TextAreaField('Your Case')
    category = SelectField(u'Category', choices=[('Criminal', 'Criminal'), 
                                                ('Civil', 'Civil'),
                                                ('Divorce', 'Divorce'),
                                                ('Other', 'Other') ])
    submit = SubmitField('Submit')


#Lawyers Create File Status
class CreateStatus(FlaskForm):
    title = StringField('Enter Status title',validators=[Required()])
    client_name = StringField('Enter Client Name',validators=[Required()])
    case_title = StringField('Enter Case Title',validators=[Required()])
    content = TextAreaField('Enter Status Content',validators=[Required()])
    # lawyer_email = StringField('Enter the File Type', validators=[Required(), Email()])
    submit = SubmitField('Post')

  
#Clients Comment on Status
class CommentForm(FlaskForm):
    comment = TextAreaField('Post Comment', validators=[Required()])
    submit = SubmitField('Submit')

#Client Update their Profile
class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us about yourself")
    submit = SubmitField("Update")