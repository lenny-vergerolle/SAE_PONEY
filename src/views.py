from flask import render_template
from .app import app, db
import src.views as views
import src.commands as commands
# import src.models as models

@app.route("/")
def home():
    """Renvoie la page d'accueil

    Returns:
        home.html : Une page d'accueil
    """
    return render_template('home.html')

@app.route("/accueil-visiteur")
def accueil_visiteur():
    """Renvoie la page d'accueil des visiteurs

    Returns:
        accueil_visiteur.html : Une page d'accueil pour les visiteurs
    """
    return render_template('accueil_visiteur.html')