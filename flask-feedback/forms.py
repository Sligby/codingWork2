from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional

class RegisterForm(FlaskForm):

    username = StringField('username',
        validators=[InputRequired(), Length(min=1, max=20)])
    password = StringField('password', 
        validators=[InputRequired(), Length(min=10, max=20)])
    email = StringField('email',
        validators=[InputRequired()])
    first_name= StringField('first name')
    last_name= StringField('last name')

class LoginForm(FlaskForm):

    username = StringField('username',
        validators=[InputRequired()])

    password = StringField('password',
        validators=[InputRequired()])

class FeedbackForm(FlaskForm):

    title = StringField('title')
    content = StringField('content',
    validators=[InputRequired()])


class DeleteForm(FlaskForm):
    """Delete form -- this form is intentionally blank."""
