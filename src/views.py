from datetime import time
from .app import app, db
from flask import flash, render_template, redirect, url_for, request
from flask_security import login_required, current_user, roles_required,  logout_user, login_user
from src.forms.UtilisateurForm import InscriptionForm , ConnexionForm, UpdateUser#, UpdatePassword
from src.forms.CoursForm import CreationCoursForm
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
from werkzeug.datastructures import FileStorage


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
            u.mdp_utilisateur = sha256(f.mot_de_passe.data.encode()).hexdigest()
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
    return redirect(url_for('home'))


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
            user.tel_utilisateur = f.telUser.data
            user.poidsUser = f.poidsUser.data
            file = f.img.data
            if file:
                file_path = os.path.join("src/static/img/profil", str(current_user.id_utilisateur))
                file.save(file_path)
            db.session.commit()
            return redirect(url_for('home'))
    f.nom_user.data = current_user.nom_utilisateur
    f.prenom_user.data = current_user.prenom_utilisateur
    f.email.data = current_user.email_utilisateur 
    f.telUser.data = current_user.tel_utilisateur
    f.poidsUser.data = current_user.poidsUser
    return render_template('profil.html', form=f)

@login_required
@app.route('/planning', methods=['GET','POST'])
def planning():
    """Renvoie la page de planning

    Returns:
        planning.html: Une page de planning
    """
    horaires = [
        
    {"id": 8, "plage": "08:00 - 09:00"},
    {"id": 9, "plage": "09:00 - 10:00"},
    {"id": 10, "plage": "10:00 - 11:00"},
    {"id": 11, "plage": "11:00 - 12:00"},
    {"id": 12, "plage": "12:00 - 13:00"},
    {"id": 13, "plage": "13:00 - 14:00"},
    {"id": 14, "plage": "14:00 - 15:00"},
    {"id": 15, "plage": "15:00 - 16:00"},
    {"id": 16, "plage": "16:00 - 17:00"},
    {"id": 17, "plage": "17:00 - 18:00"},
    ]
    jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

    if current_user.is_authenticated :
        mes_cours = Cours.query.filter_by(id_utilisateur=current_user.id_utilisateur).all()
        return render_template('planning.html', jours=jours,horaires=horaires, cours=mes_cours)
    return redirect(url_for('home'))

@app.route('/creer-cours', methods=['GET','POST'])    
def creer_cours():
    """Renvoie la page de création de cours

    Returns:
        creer_cours.html: Une page de création de cours
    """
    
    f = CreationCoursForm()
    if f.validate_on_submit():
        if f.validate():
            c = Cours()
            c.nomCo = f.nomCo.data
            c.collectif = bool(f.collectif.data)
            c.nbPersonne = f.nbPersonne.data
            c.duree = f.duree.data
            c.date = f.date.data
            c.heureDebut = f.heureDebut.data
            cours = Cours.query.all()
            if cours:
                for cour in cours:
                    if cour.date == c.date and cour.heureDebut == c.heureDebut:
                        print("Un cours est déjà prévu à cette date et heure")
                        return redirect(url_for('creer_cours'))
            if current_user.id_utilisateur:
                c.id_utilisateur = current_user.id_utilisateur
            c.idCo = Cours.get_last_id() + 1
            try:
                db.session.add(c)
                db.session.commit()
                print("Cours créée")
            except Exception as e:
                print(f"Une erreur s'est produit {e}")
                db.session.rollback()
    
            return redirect(url_for('planning'))
    return render_template('creer-cours.html', form=f)

@app.route('/ajout-moniteur', methods=['GET','POST'])
@login_required
def ajout_moniteur():
    """Renvoie la page d'inscription de moniteur dédiée aux admins

    Returns:
        ajout-moniteur : Une page d'inscription de moniteur dédiée aux admins
    """
    f = InscriptionForm()
    if f.validate_on_submit():
        print("Formulaire soumis et validé.")
        if f.validate():
            u = Utilisateur()
            u.nom_utilisateur = f.nom_user.data
            u.prenom_utilisateur = f.prenom_user.data
            u.mdp_utilisateur = sha256(f.mot_de_passe.data.encode()).hexdigest()
            u.email_utilisateur = f.email.data
            u.certification = str(Utilisateur.get_last_id() + 1)
            u.contrat = str(Utilisateur.get_last_id() + 1.1)
            u.id_role = 3
            u.ddn_utilisateur = f.ddn_user.data
            u.sexe_utilisateur = f.sexeUser.data
            u.poidsUser = float(f.poidsUser.data)
            u.tel_utilisateur = f.telUser.data
            db.session.add(u)
            db.session.commit()
            file_certif = f.certificationUser.data
            if file_certif:
                file_path = os.path.join("src/static/doc_moniteur/certification/",f"certification_{Utilisateur.get_last_id() + 1}.pdf")
                file_certif.save(file_path)
            file_contrat = f.contratUser.data
            if file_contrat:
                file_path = os.path.join("src/static/doc_moniteur/contrat/",f"contrat_{Utilisateur.get_last_id() + 1}.pdf")
                file_contrat.save(file_path)
            return redirect(url_for('ajout_moniteur'))
    return render_template('ajout_moniteur.html', form=f)