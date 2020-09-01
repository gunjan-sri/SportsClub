from flask import Blueprint, render_template

tableTennis = Blueprint('tableTennis', __name__, template_folder='templates')

@tableTennis.route('/table')
def indexTT():
    return render_template('TTindex.html')
