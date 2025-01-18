from datetime import date, datetime, time, timedelta
from src.forms.PoneyForm import PoneyForm
from src.models.Historique import Historique
from .app import app, db
from flask import flash, render_template, redirect, url_for, request
from sqlalchemy import and_, or_
from flask_security import login_required, current_user, roles_required,  logout_user, login_user
from src.forms.UtilisateurForm import InscriptionForm , ConnexionForm, UpdatePassword, UpdateUser #, UpdatePassword
from src.forms.CoursForm import CreationCoursForm,ReservationCoursForm
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


@app.route('/signin', methods=['GET', 'POST'])
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
                file.save(
                    os.path.join("src/static/img/profil",
                                 str(Utilisateur.get_last_id() + 1)))
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
    nb_adherents = len(Utilisateur.query.filter_by(id_role=1).all())
    nb_moniteurs = len(Utilisateur.query.filter_by(id_role=3).all())
    return render_template('home.html',
                           nb_adherents=nb_adherents,
                           nb_moniteurs=nb_moniteurs)


@login_required
@app.route("/mes-reservations")
def mes_reservations():
    """Renvoie la page des réservations de l'utilisateur

    Returns:
        mes-reservations.html : Une page des réservations de l'utilisateur
    """
    moniteurs = Utilisateur.query.filter_by(id_role=3).all()
    if (current_user.id_role == 1):
        les_reservations = Reserver.query.filter_by(id_utilisateur=current_user.id_utilisateur).all()
    elif (current_user.id_role == 3):
        les_reservations = Reserver.query.filter_by(id_moniteur=current_user.id_utilisateur).all()

    return render_template('mes-reservations.html',les_reservations=les_reservations,moniteurs=moniteurs)


@login_required
@app.route('/details-reservation/<string:nomRes>')
def details_reservation(nomRes):
    """Renvoie la page de détails d'une réservation

    Returns:
        details-reservation.html : Une page de détails d'une réservation
    """
    reservation = Reserver.query.filter_by(nomRes=nomRes).first()
    moniteurs = Utilisateur.query.filter_by(id_role=3).all()

    return render_template('une-reservation.html',
                           reservation=reservation,
                           historique=False,moniteurs=moniteurs,retour=False)


@app.route('/accueil-visiteur')
def accueil_visiteur():
    """Renvoie la page d'accueil des adherents

    Returns:
        accueil_adherent.html : Une page d'accueil pour les adherents
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


@app.route('/login', methods=['GET', 'POST'])
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


@app.route('/profil', methods=['GET', 'POST'])
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
                file_path = os.path.join("src/static/img/profil",
                                         str(current_user.id_utilisateur))
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
@app.route('/modif-mdp/<int:id_utilisateur>', methods=['GET','POST'])
def modifier_mdp(id_utilisateur):
    f = UpdatePassword()
    user = Utilisateur.query.filter_by(id_utilisateur = id_utilisateur).first()
    if f.validate_on_submit():
        if f.validate():
            if user:
                user.mdp_utilisateur = sha256(f.new_password.data.encode()).hexdigest()
                db.session.commit()
                return redirect(url_for('home'))
    return render_template('modifer-mdp.html', form = f, id_utilisateur = id_utilisateur, user = user)

@login_required
@app.route('/planning', methods=['GET','POST'])
def planning():
    """Renvoie la page de planning"""

    horaires = [
        {
            "id": 8,
            "plage": "08:00 - 09:00"
        },
        {
            "id": 9,
            "plage": "09:00 - 10:00"
        },
        {
            "id": 10,
            "plage": "10:00 - 11:00"
        },
        {
            "id": 11,
            "plage": "11:00 - 12:00"
        },
        {
            "id": 12,
            "plage": "12:00 - 13:00"
        },
        {
            "id": 13,
            "plage": "13:00 - 14:00"
        },
        {
            "id": 14,
            "plage": "14:00 - 15:00"
        },
        {
            "id": 15,
            "plage": "15:00 - 16:00"
        },
        {
            "id": 16,
            "plage": "16:00 - 17:00"
        },
        {
            "id": 17,
            "plage": "17:00 - 18:00"
        },
    ]
    jours = [
        "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"
    ]

    # Crée un dictionnaire avec une liste vide pour chaque jour
    dico_jours_horaires = {
        jour: {
            horaire['id']: []
            for horaire in horaires
        }
        for jour in jours
    }

    #mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

    jours_mapping = {
        "Monday": "Lundi",
        "Tuesday": "Mardi",
        "Wednesday": "Mercredi",
        "Thursday": "Jeudi",
        "Friday": "Vendredi",
        "Saturday": "Samedi",
        "Sunday": "Dimanche"
    }

    if current_user.is_authenticated:
        if current_user.id_role == 3:
            mes_reservations = Reserver.query.filter_by(
                id_moniteur=current_user.id_utilisateur).all()
        else:
            mes_reservations = Reserver.query.filter_by(
                id_utilisateur=current_user.id_utilisateur).all()

        # Organiser les cours par jour et horaire
        for reservation in mes_reservations:
            jour_francais = jours_mapping[reservation.date.strftime('%A')]

            if jour_francais in jours and reservation.heureDebut.hour in [
                    horaire['id'] for horaire in horaires
            ]:
                dico_jours_horaires[jour_francais][
                    reservation.heureDebut.hour].append(reservation)

        return render_template('planning.html',
                               dico=dico_jours_horaires,
                               jours=jours,
                               horaires=horaires)
    return redirect(url_for('home'))


@login_required
@app.route('/creer-cours', methods=['GET', 'POST'])
def creer_cours():
    """Renvoie la page de création de cours

    Returns:
        creer_cours.html: Une page de création de cours
    """

    f = CreationCoursForm()
    f.adherents.choices = [
        (adherent.id_utilisateur, adherent.nom_utilisateur)
        for adherent in Utilisateur.query.filter_by(id_role=1).all()
    ]
    if f.validate_on_submit():
        if f.validate():
            c = Cours()
            c.nomCo = f.nomCo.data
            c.id_utilisateur = current_user.id_utilisateur
            adherent = Utilisateur.query.get(f.adherents.data)
            c.id_adherent = adherent.id_utilisateur
            c.idCo = Cours.get_last_id() + 1
            try:
                db.session.add(c)
                db.session.commit()
                print("Cours créée")
            except Exception as e:
                print(f"Une erreur s'est produit {e}")
                db.session.rollback()

            return redirect(url_for('home'))
    return render_template('creer-cours.html', form=f)

@app.route('/modifier-moniteur', defaults={'id_utilisateur': None}, methods=['GET', 'POST'])
@app.route('/modifier-moniteur/<int:id_utilisateur>', methods=['GET', 'POST'])
@login_required
def modifier_moniteur(id_utilisateur=None):
    """Ajoute ou modifie un moniteur selon l'ID donné"""
    f = InscriptionForm()

    # Vérification de l'existence du moniteur
    moniteur = Utilisateur.query.filter_by(id_utilisateur=id_utilisateur).first() if id_utilisateur else None
    existe = bool(moniteur)

    if f.validate_on_submit():
        if not moniteur:
            moniteur = Utilisateur()
            db.session.add(moniteur)
            moniteur.nom_utilisateur = f.nom_user.data
            moniteur.prenom_utilisateur = f.prenom_user.data
            if not existe or f.mot_de_passe.data:
                moniteur.mdp_utilisateur = sha256(f.mot_de_passe.data.encode()).hexdigest()
            moniteur.email_utilisateur = f.email.data
            moniteur.id_role = 3  
            moniteur.ddn_utilisateur = f.ddn_user.data
            moniteur.sexe_utilisateur = f.sexeUser.data
            moniteur.poidsUser = float(f.poidsUser.data)
            moniteur.tel_utilisateur = f.telUser.data

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flash(f"Erreur lors de la sauvegarde : {e}", "danger")
            return redirect(url_for('modifier_moniteur', id_utilisateur=id_utilisateur))

        file_certif = f.certificationUser.data
        if file_certif:
            file_path = os.path.join(
                "src/static/doc_moniteur/certification/",
                f"certification_{Utilisateur.get_last_id() + 1}.pdf")
            file_certif.save(file_path)
            file_contrat = f.contratUser.data
        if file_contrat:
            file_path = os.path.join(
                "src/static/doc_moniteur/contrat/",
                f"contrat_{Utilisateur.get_last_id() + 1}.pdf")
            file_contrat.save(file_path)

        flash("Moniteur ajouté/modifié avec succès.", "success")
        return redirect(url_for('gerer_moniteurs'))
    #Modification des champs 
    if moniteur:
        f.nom_user.data = moniteur.nom_utilisateur
        f.prenom_user.data = moniteur.prenom_utilisateur
        f.email.data = moniteur.email_utilisateur
        f.telUser.data = moniteur.tel_utilisateur
        f.poidsUser.data = moniteur.poidsUser
        f.ddn_user.data = date.fromisoformat(moniteur.ddn_utilisateur)
        f.sexeUser.data = moniteur.sexe_utilisateur
    return render_template('ajout-moniteur.html', form=f, existe=existe, id_utilisateur=id_utilisateur)

@login_required
@app.route('/reserver-cours', defaults={'nomRes': None}, methods=['GET', 'POST'])
@app.route('/reserver-cours/<string:nomRes>', methods=['GET', 'POST'])
def reserver_cours(nomRes):
    """Renvoie la page de réservation de cours."""
    f = ReservationCoursForm()

    # Remplissage des choix pour les champs déroulants
    f.moniteurs.choices = [
        (moniteur.id_utilisateur, moniteur.prenom_utilisateur)
        for moniteur in Utilisateur.query.filter_by(id_role=3).all()
    ]
    f.poneys.choices = [
        (poney.idPo, poney.nomPo)
        for poney in Poney.query.filter(Poney.poidsMax > current_user.poidsUser).all()
    ]
    f.cours.choices = [
        (cour.idCo, cour.nomCo)
        for cour in Cours.query.filter(
            or_(
                Cours.id_adherent == current_user.id_utilisateur,
                Cours.id_adherent == 0
            )
        ).all()
    ]

    reservation = Reserver.query.filter_by(nomRes=nomRes).first()

    if f.validate_on_submit():
        
        if not reservation:
            reservation = Reserver()
            db.session.add(reservation)

        # Mise à jour des champs
        reservation.nomRes = f.nomRes.data
        reservation.collectif = f.collectif.data == 'true'
        reservation.nbPersonne = f.nbPersonne.data
        reservation.duree = f.duree.data
        reservation.date = f.date.data
        reservation.heureDebut = f.heureDebut.data
        reservation.id_utilisateur = current_user.id_utilisateur
        reservation.idPo = f.poneys.data
        reservation.id_moniteur = f.moniteurs.data
        reservation.idCo = f.cours.data

        # Vérification des conflits de réservation
        heureDebut_datetime = datetime.combine(datetime.today(), reservation.heureDebut)

        # Calcul de l'heure de fin de la réservation en ajoutant la durée (en minutes)
        heureFin_datetime = heureDebut_datetime + timedelta(minutes=reservation.duree)
        
        # Recherche des conflits de réservation
        conflit = Reserver.query.filter(
            Reserver.date == reservation.date,
            Reserver.heureDebut < heureFin_datetime.time(),  # Comparer avec l'heure de fin de la réservation
            (Reserver.heureDebut + Reserver.duree) > reservation.heureDebut
        ).first()

        if conflit:
            flash("Un cours est déjà prévu à cette date et heure.", "danger")
            return redirect(url_for('reserver_cours', nomRes=nomRes))
        # Stockage de l'historique
        stocker_historique(
            current_user.id_utilisateur,
            reservation.nomRes,
            reservation.collectif,
            reservation.duree,
            reservation.idCo,
            reservation.date,
            reservation.idPo,
            reservation.heureDebut,
            reservation.nbPersonne
        )
        try:
            db.session.commit()
            flash("Réservation effectuée avec succès.", "success")
            print("Réservation effectuée avec succès.")

            
    

            return redirect(url_for('planning'))
        
        except Exception as e:
            db.session.rollback()
            flash(f"Erreur lors de la sauvegarde : {e}", "danger")
            return redirect(url_for('reserver_cours', nomRes=nomRes))

    # Pré-remplissage des données du formulaire si une réservation existe
    if reservation:
        f.nomRes.data = reservation.nomRes
        f.collectif.data = 'true' if reservation.collectif else 'false'
        f.nbPersonne.data = reservation.nbPersonne
        f.duree.data = reservation.duree
        f.date.data = reservation.date
        f.heureDebut.data = reservation.heureDebut
        f.poneys.data = reservation.idPo
        f.moniteurs.data = reservation.id_moniteur
        f.cours.data = reservation.idCo

    return render_template('reserver-cours.html', form=f, nomRes=nomRes)



def stocker_historique(id_utilisateur, nomRes, collectif, duree, idCo, date,
                       idPo, heureDebut, nbPersonne):
    """Stocke une action dans l'historique

    Args:
        id_utilisateur (int): L'identifiant de l'utilisateur
        nomRes (str): Le nom de la réservation
        collectif (bool): Le type de réservation (collectif ou non)
        duree (int): La durée de la réservation
        idCo (int): L'identifiant du cours
        date (datetime.date): La date de la réservation
        idPo (int): L'identifiant du poney
        heureDebut (datetime.time): L'heure de début de la réservation
        nbPersonne (int): Le nombre de personnes
    """
    
    # Vérifier si l'historique existe déjà avec la même combinaison de colonnes
    existe = Historique.query.filter_by(
        date=date,
        heureDebut=heureDebut,
        idCo=idCo,
        idPo=idPo,
        id_utilisateur=id_utilisateur
    ).first()
    
    if not existe:
        # Si l'historique n'existe pas
        h = Historique()
        h.nomRes = nomRes
        h.collectif = collectif
        h.nbPersonne = nbPersonne
        h.duree = duree
        h.date = date
        h.heureDebut = heureDebut
        h.idCo = idCo
        h.idPo = idPo
        h.id_utilisateur = id_utilisateur
        db.session.add(h)
        db.session.commit()
    else:
        # Si l'historique existe déjà, mettre à jour
        existe.nomRes = nomRes
        existe.collectif = collectif
        existe.nbPersonne = nbPersonne
        existe.duree = duree
        db.session.commit()

    

@login_required
@app.route('/home/historique', methods=['GET'])
def historique():
    """Renvoie la page de l'historique

    Returns:
        historique.html: Une page de l'historique
    """
    moniteurs = Utilisateur.query.filter_by(id_role=3).all()
    historiques = Historique.query.all()

    return render_template('historique.html', historiques=historiques, moniteurs=moniteurs)


@login_required
@app.route(
    '/home/suppression_reservation/<int:id_utilisateur>/<int:idCo>/<int:idPo>',
    methods=['GET'])
def suppression_reservation(idPo, id_utilisateur, idCo):
    """Supprime une réservation
    Args:
        idPo (int): L'identifiant du poney
        id_utilisateur (int): L'identifiant de l'utilisateur
        idCo (int): L'identifiant du cours
    Returns:
        redirect: Redirige vers la page des réservations
    """
    reservation = Reserver.query.filter_by(id_utilisateur=id_utilisateur,
                                           idPo=idPo,
                                           idCo=idCo).first()
    if reservation:
        db.session.delete(reservation)
        db.session.commit()
        print('La réservation a été supprimée avec succès.')
    else:
        print('La réservation n\'a pas été trouvée.')
    return redirect(url_for('mes_reservations'))


@login_required
@app.route('/home/gerer-moniteurs', methods=['GET'])
def gerer_moniteurs():
    """Renvoie la page de gestion des poneys

    Returns:
        gerer_poneys.html: Une page de gestion des poneys
    """
    moniteurs = Utilisateur.query.filter_by(id_role=3).all()
    return render_template('gerer-moniteurs.html', moniteurs=moniteurs)


@login_required
@app.route('/home/suppression-moniteur/<int:id_utilisateur>', methods=['GET'])
def suppression_moniteur(id_utilisateur):
    """Supprime un moniteur
    Args:
        id_utilisateur (int): L'identifiant du moniteur
    Returns:
        gerer-moniteurs.html: Une page de gestion des moniteurs
    """
    moniteur = Utilisateur.query.filter_by(
        id_utilisateur=id_utilisateur).first()
    if moniteur:
        db.session.delete(moniteur)
        db.session.commit()
        print('Le moniteur a été supprimée avec succès.')
    else:
        print('La moniteur n\'a pas été trouvée.')
    return redirect(url_for('gerer_moniteurs'))


@login_required
@app.route('/home/gerer-poneys', methods=['GET'])
def gerer_poneys():
    """Renvoie la page de gestion des moniteurs

    Returns:
        gerer_moniteurs.html: Une page de gestion des moniteurs
    """
    poneys = Poney.query.all()
    return render_template('gerer-poneys.html', poneys=poneys)


@login_required
@app.route('/home/suppression-poney/<int:idPo>', methods=['GET'])
def suppression_poney(idPo):
    """Supprime un poney
    Args:
        idPo (int): L'identifiant du poney
    Returns:
        gerer-poneys.html: Une page de gestion des poneys
    """
    poney = Poney.query.filter_by(idPo=idPo).first()
    if poney:
        db.session.delete(poney)
        db.session.commit()
        print('Le poney a été supprimé avec succès.')
    else:
        print('Le poney n\'a pas été trouvé.')
    return redirect(url_for('gerer_poneys'))


@login_required
@app.route('/home/ajout-poney', defaults={'idPo': None}, methods=['GET', 'POST'])
@app.route('/home/ajout-poney/<int:idPo>', methods=['GET', 'POST'])
def ajout_poney(idPo):
    """Renvoie la page d'ajout ou de modification d'un poney

    Returns:
        ajout-poney.html: Une page d'ajout ou de modification d'un poney
    """
    f = PoneyForm()
    existe = False
    poney = Poney.query.filter_by(idPo=idPo).first() if idPo else None
    if f.validate_on_submit():
        print("form soumis")
        if poney:
            poney.nomPo = f.nomPo.data
            poney.poidsMax = f.poidsMax.data
            poney.couleurPo = f.couleurPo.data
            poney.ddnPo = f.ddnPo.data
            print("babar")
            try:
                db.session.commit()
                print("Poney mis à jour")
            except Exception as e:
                print(f"Une erreur s'est produite : {e}")
                db.session.rollback()
        else:
       
            p = Poney(
                nomPo=f.nomPo.data,
                poidsMax=f.poidsMax.data,
                couleurPo=f.couleurPo.data,
                ddnPo=f.ddnPo.data
            )
            try:
                db.session.add(p)
                db.session.commit()
                print("Poney ajouté")
            except Exception as e:
                print(f"Une erreur s'est produite : {e}")
                db.session.rollback()
            return redirect(url_for('ajout_poneys'))
        return redirect(url_for('gerer_poneys'))
    if poney:
        f.nomPo.data = poney.nomPo
        f.poidsMax.data = poney.poidsMax
        f.couleurPo.data = poney.couleurPo
        f.ddnPo.data = poney.ddnPo
        existe = True

    return render_template('ajout-poney.html', form=f, existe=existe,idPo=idPo)



@login_required
@app.route('/home/gerer-adherents', methods=['GET'])
def gerer_adherents():
    """Renvoie la page de gestion des poneys

    Returns:
        gerer_poneys.html: Une page de gestion des poneys
    """
    adherents = Utilisateur.query.filter(and_(Utilisateur.id_role == 1, Utilisateur.id_utilisateur != 0)).all()
    return render_template('gerer-adherents.html', adherents=adherents)


@login_required
@app.route('/home/suppression-adherent/<int:id_utilisateur>', methods=['GET'])
def suppression_adherent(id_utilisateur):
    """Supprime un adherent
    Args:
        id_utilisateur (int): L'identifiant de l'adherent
    Returns:
        gerer-moniteurs.html: Une page de gestion des adherents
    """
    adherent = Utilisateur.query.filter_by(
        id_utilisateur=id_utilisateur).first()
    if adherent:
        db.session.delete(adherent)
        db.session.commit()
        print('Le moniteur a été supprimée avec succès.')
    else:
        print('La moniteur n\'a pas été trouvée.')
    return redirect(url_for('gerer_adherents'))


@login_required
@app.route('/home/gerer-grand-galop', methods=['GET', 'POST'])
def gerer_grand_galop():
    """Renvoie la page de gestion des poneys

    Returns:
        gerer_poneys.html: Une page de gestion des poneys
    """
    return render_template('gerer-grand-galop.html')

