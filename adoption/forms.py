from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField


class AddPetForm(FlaskForm):

    name = StringField("Pet Name")

    species = StringField("Pet Species")

    photo_url= StringField("Pet Photo URL")

    age = FloatField("Pet Age")

    notes = StringField("notes")

    available = BooleanField("Available")

class EditPetForm(FlaskForm):

    name = StringField("Pet Name")

    species = StringField("Pet Species")

    photo_url= StringField("Pet Photo URL")

    age = FloatField("Pet Age")

    notes = StringField("notes")

    available = BooleanField("Available") 






