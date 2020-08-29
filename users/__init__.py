from flask import Flask

users = Flask(__name__)

from users import routes
