from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                    SubmitField, SelectField)
from wtforms.validators import Required

class CaseForm(FlaskForm):
    title = StringField('Case title',validators=[Required()])
    post = TextAreaField('Your Case')
    category = SelectField(u'Category', choices=[('Criminal', 'Criminal'), 
                                                ('Civil', 'Civil'),
                                                ('Divorce', 'Divorce'),
                                                ('Other', 'Other') ])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Post Comment', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us about yourself")
    submit = SubmitField("Update")