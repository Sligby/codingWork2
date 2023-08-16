from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Feedback
from forms import RegisterForm, LoginForm, FeedbackForm, DeleteForm
from werkzeug.exceptions import Unauthorized

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

    form = RegisterForm()

    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data

        user = User.register(name, pwd)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id
        session["username"]= user.username

        return redirect("/home")

    else:
        return render_template("register.html", form=form)


# GET /login
# Show a form that when submitted will login a user. This form should accept a username and a password.
# Make sure you are using WTForms and that your password input hides the characters that the user is typing!
# POST /login
# Process the login form, ensuring the user is authenticated
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
            session['username']= user.name
            return redirect('/')

        else:
            form.username.errors = ["wrong username or password"]

    return render_template('login.html', form=form)


# GET /users/<username>
# Show information about the given user.

# Show all of the feedback that the user has given.

# For each piece of feedback, display with a link to a form to edit the feedback and a button to delete the feedback.

# Have a link that sends you to a form to add more feedback and a button to delete the user Make sure that only the user who is logged in can successfully view this page.

@app.route("/users/<username>")
def show_user(username):
    """Example page for logged-in-users."""

    if "username" not in session or username != session['username']:
        raise Unauthorized()

    user = User.query.get(username)
    form = DeleteForm()

    return render_template("users/show.html", user=user, form=form)





@app.route("/logout")
def logout():
    """Logs user out and redirects to homepage."""

    session.pop("user_id")

    return redirect("/")

if __name__ == '__main__':
    app.run()

# POST /users/<username>/delete
# Remove the user from the database and make sure to also delete all of their feedback. Clear any user information in the session and redirect to /. Make sure that only the user who is logged in can successfully delete their account
@app.route('/users/<username>/delete')
def deleteuser(username):

        user = User.query.get(username)

    
        if user:
            db.session.delete(user)
            db.session.commit()
        
            session.pop('user_id')
            session.pop('username')

        return redirect('/')

# GET /users/<username>/feedback/add
# Display a form to add feedback Make sure that only the user who is logged in can see this form
# POST /users/<username>/feedback/add
# Add a new piece of feedback and redirect to /users/<username> — Make sure that only the user who is logged in can successfully add feedback
@app.route('/users/<username>/feedback/add', methods = ['GET', 'POST'])
def addfeedback(username):

    if username not in session or username != session['username']:
        raise Unauthorized()

    form = FeedbackForm()

    if form.validate_on_submit():
            title = form.title.data
            content = form.title.data

            feedback = Feedback(title=title, content= content)
            db.session.add(feedback)
            db.session.commit()

    else:
            return render_template('addfeedback.html', form=form)

    
# GET /feedback/<feedback-id>/update
# Display a form to edit feedback — **Make sure that only the user who has written that feedback can see this form **
# POST /feedback/<feedback-id>/update
# Update a specific piece of feedback and redirect to /users/<username> — Make sure that only the user who has written that feedback can update it
@app.route('/feedback/<int:feedback_id>/update', methods = ['GET', 'POST'])
def editfeed(feedback_id):

    feedback = Feedback.query.get(feedback_id)

    if "username" not in session or feedback.username != session['username']:
        raise Unauthorized() 

    form = FeedbackForm()
    
    if form.validate_on_submit():
        feedback.title = form.title.data
        feedback.content = form.content.data

        db.session.commit()

        return redirect(f"/users/{feedback.username}")

    return render_template("/feedback/editfeedback.html", form=form, feedback=feedback) 
    


# POST /feedback/<feedback-id>/delete
# Delete a specific piece of feedback and redirect to /users/<username> — Make sure that only the user who has written that feedback can delete it
@app.route("/feedback/<int:feedback_id>/delete", methods=["POST"])
def delete_feedback(feedback_id):
    """Delete feedback."""

    feedback = Feedback.query.get(feedback_id)
    if "username" not in session or feedback.username != session['username']:
        raise Unauthorized()

    form = DeleteForm()

    if form.validate_on_submit():
        db.session.delete(feedback)
        db.session.commit()

    return redirect(f"/users/{feedback.username}")