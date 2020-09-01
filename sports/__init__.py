from flask import Flask, Blueprint
from .tableTennis.routes import tableTennis
from .site.routes import site

app = Flask(__name__)

app.register_blueprint(tableTennis)
app.register_blueprint(site)
