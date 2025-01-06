from flask import render_template
from .app import app, db
import src.views as views
import src.commands as commands
# import src.models as models

@app.route("/navbar")
def navbar():
    return render_template('navbar.html')