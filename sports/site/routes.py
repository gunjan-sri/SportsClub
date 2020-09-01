from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='templates')

@site.route('/home')
def homepage():
    return render_template('home.html')

@site.route('/aboutus')
def aboutus():
    return 'About Us Page'

@site.route('/halls')
def halls():
    return 'Halls Page'

@site.route('/login')
