from app import app
from flask import render_template

@app.route("/")

@app.route("/home")
def homepage():
    return render_template('homepage.html', title="Homepage")

@app.route("/sports")
def sports():
    return render_template('sports.html', title="Sports Information")

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html', title="About Us")
