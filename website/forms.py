from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, ValidationError
from website.models import Project, User
from website import db

class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])    
    submit = SubmitField('Submit please')

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login please')

# class EditForm(FlaskForm):
#     title = StringField('Title', validators=[DataRequired()])
#     author = StringField('Author', validators=[DataRequired()])
#     content = TextAreaField('Content', validators=[DataRequired()])    
#     approve = BooleanField('Approve this Post?')    
#     submit = SubmitField('Submit')
