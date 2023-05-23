from flask import *
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)


@app.route('/')
def home():
    "show home page"
    return render_template('base.html')

@app.route("/add", methods=['GET', 'POST'])
def addpet():
    "add pet form"

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url= form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        return redirect("/add")

    else:
        return render_template('addpet.html', form=form)

@app.route('/[pet-id]', methods=['GET', 'POST'])
def petpage(pet_id):
    "show pet details, edit pet"
    
    form = EditPetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url= form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        return redirect("/add")

    else:
        pet= Pet.query.get(pet_id)
        return render_template('pet_detail', pet=pet)



