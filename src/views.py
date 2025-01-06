from flask import render_template, url_for
from .app import app, db
import src.views as views
import src.commands as commands

@app.route("/navbar")
def navbar():
    return render_template('navbar.html')