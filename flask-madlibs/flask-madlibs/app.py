from flask import Flask, renderTemplate, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

app.route("/")
def gen_questions():

    prompts = story.prompts

    return render_template("prompts.html", prompts = prompts)

app.route("/story")
def gen_story():

    text = story.generate(request.args)

    return render_template("story.html", text = text)
    