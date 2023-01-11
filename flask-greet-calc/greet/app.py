from flask import Flask

app = Flask(__app__)

@app.route("/welcome")
def welcome():
    return "welcome"

@app.route("/welcome/home")
def welcome_home():
    return("welcome home!")

@app.route("/welcome/back")
def welcome_back():