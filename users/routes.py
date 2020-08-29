from app import app
from flask import render_template

@app.route("/")

@app.route("/login")
def login_view():
    return "Under construction - Login Page"
    #render_template("login.html")
