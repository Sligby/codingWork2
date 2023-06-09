from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField

class AddUserForm(FlaskForm):

    username = StringField('username')
    password = StringField('password')
    email = StringField('email')
    first_name= StringField('first name')
    last_name= StringField('last name')

class LoginForm(FlaskForm):

    username = StringField('username')
    password = StringField('password')
