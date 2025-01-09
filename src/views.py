from .app import app, db
from flask import render_template, redirect, url_for, request
from flask_security import login_required, current_user, roles_required,  logout_user, login_user
from src.forms.UtilisateurForm import InscriptionForm , ConnexionForm, UpdateUser#, UpdatePassword

from src.models.Utilisateur import Utilisateur
from src.models.Cours import Cours
from src.models.Horaire import Horaire
from src.models.Poney import Poney
from src.models.Reserver import Reserver
from src.models.Travailler import Travailler
from src.models.Role import Role

from hashlib import sha256
from flask_security import Security, SQLAlchemySessionUserDatastore

import os
from functools import wraps
from flask import abort


@app.route('/signin', methods=['GET','POST'])
def signin():
    f = InscriptionForm()
    #roles = Role.query.all()
    #if not roles:
    #    raise ValueError("Aucun roles trouvé.")

    #f.role.choices = [(role.id_role, role.name) for role in roles]
    if f.validate_on_submit():
        if f.validate():
            u = Utilisateur()
            u.nom_utilisateur = f.nom_user.data
            u.prenom_utilisateur = f.prenom_user.data
            u.mdp_utilisateur = sha256(
            f.mot_de_passe.data.encode()).hexdigest()
            u.email_utilisateur = f.email.data
            u.img_utilisateur = str(Utilisateur.get_last_id() + 1)
            u.id_role = 1
            u.ddn_utilisateur = f.ddn_user.data
            u.sexeUser = f.sexeUser.data
            u.poidsUser = float(f.poidsUser.data)
            u.tel_utilisateur = f.telUser.data
            file = f.img.data
            if file:
                file.save(os.path.join("src/static/img/profil", str(Utilisateur.get_last_id()+1)))
            db.session.add(u)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('signin.html', form=f)

@app.route('/')
def home():
    """Renvoie la page d'accueil

    Returns:
        home.html : Une page d'accueil
    """
    return render_template('home.html')

@app.route("/mes-reservations")
def mes_reservations():
    """Renvoie la page d'accueil

    Returns:
        home.html : Une page d'accueil
    """
    return render_template('mes-reservations.html')

@app.route("/accueil-visiteur")
def accueil_visiteur():
    """Renvoie la page d'accueil des visiteurs

    Returns:
        accueil_visiteur.html : Une page d'accueil pour les visiteurs
    """
    return render_template('accueil_visiteur.html')
  
  
@app.route('/accueil-adherent')
@login_required
def accueil_adherent():
    """Renvoie la page d'accueil des adherents

    Returns:
        accueil_adherent.html : Une page d'accueil pour les adherents
    """
    return render_template('accueil_adherent.html')

@app.route('/login', methods=['GET','POST'])
def login():
    """Renvoie la page de connexion

    Returns:
        connexion.html : Une page de connexion
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    f = ConnexionForm()
    if f.validate_on_submit():
        u = f.get_authenticated_user()
        if u:
            login_user(u)
            return redirect(url_for('home'))
    return render_template('connexion.html', form=f)

@app.route('/logout')
@login_required
def logout():
    """Déconnecte l'utilisateur

    Returns:
        login : Redirige vers la page de connexion
    """
    logout_user()
    return redirect(url_for('login'))


# A charger après la définition de la route login
user_datastore = SQLAlchemySessionUserDatastore(db.session, Utilisateur, Role)
security = Security(app, user_datastore)


@app.route('/profil', methods=['GET','POST'])
def modifier_profil():
    """Renvoie la page de modification du profil

    Returns:
        profil.html: Une page de modification du profil
    """
    f = UpdateUser()
    if f.validate_on_submit():
        if f.validate():
            user = current_user  # Récupérer l'utilisateur actuel via Flask-Login
            user.prenom_utilisateur = f.prenom_user.data
            user.nom_utilisateur = f.nom_user.data
            user.email_utilisateur = f.email.data
            file = f.img.data
            if file:
                file_path = os.path.join("src/static/img/profil", str(current_user.id_utilisateur))
                file.save(file_path)
            db.session.commit()
            return redirect(url_for('home'))
    f.nom_user.data = current_user.nom_utilisateur
    f.prenom_user.data = current_user.prenom_utilisateur
    f.email.data = current_user.email_utilisateur 
    return render_template('profil.html', form=f)

#@app.route('/profil/<int:id>', methods=['GET','POST'])
@app.route('/planning', methods=['GET','POST'])
def planning():
    """Renvoie la page de planning

    Returns:
        planning.html: Une page de planning
    """
    #user = Utilisateur.query.get(id)
    return render_template('planning.html')
