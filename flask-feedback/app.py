from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User
from forms import AddUserForm, LoginForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///hashing_login"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)

@app.route('/')
def homepage():

  return render_template('base.html')

# GET /
# Redirect to /register.)
# GET /register
# Show a form that when submitted will register/create a user. This form should accept a username, password, email, first_name, and last_name.
# Make sure you are using WTForms and that your password input hides the characters that the user is typing!
# POST /register
# Process the registration form by adding a new user. Then redirect to /secret
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user: produce form & handle form submission."""

    form = AddUserForm()

    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data

        user = User.register(name, pwd)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id

        return redirect("/home")

    else:
        return render_template("register.html", form=form)


# GET /login
# Show a form that when submitted will login a user. This form should accept a username and a password.
# Make sure you are using WTForms and that your password input hides the characters that the user is typing!
# POST /login
# Process the login form, ensuring the user is authenticated and going to /secret if so.
@app.route('/login')
def login():
    """Login User: load form and handle submission"""

    form = LoginForm()
    
    if form.validate_on_submit():
        username = form.username.data
        pwd = form.password.data

        user= User.authenticate(username, pwd)

        if user:
            session['user_id']= user.id
            return redirect('/')

        else:
            form.username.errors = ["wrong username or password"]

    return render_template('login.html', form=form)





# GET /secret
# Return the text “You made it!” (don’t worry, we’ll get rid of this soon)
@app.route("/secret")
def secret():
    """Example hidden page for logged-in users only."""

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/")

    else:
        return render_template("secret.html")

@app.route("/logout")
def logout():
    """Logs user out and redirects to homepage."""

    session.pop("user_id")

    return redirect("/")

if __name__ == '__main__':
    app.run()