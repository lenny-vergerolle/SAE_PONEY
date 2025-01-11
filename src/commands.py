from hashlib import sha256
import click
from .app import app, db
from . models.Utilisateur import Utilisateur
from .models.Cours import Cours
from .models.Horaire import Horaire
from .models.Poney import Poney
from .models.Reserver import Reserver
from .models.Travailler import Travailler
from .models.Role import Role

@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    # Création de toutes les tables
    db.drop_all()
    db.create_all()
    
    # Import des modèles
    import src.models as md
    import yaml
    from datetime import time
    
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)

    elements = {
        'cours':{},
        'horaire':{},
        'poney':{},
        'reserver':{},
        'travailler':{},
        'utilisateur':{},
        'role':{},
    }

    for elem in data:
        if elem["type"] == "Utilisateur":
            if elem["role_id"] == 1: # Adherent
                utilisateur = Utilisateur(
                id_utilisateur = elem["idUser"],
                nom_utilisateur = elem["nomUser"],
                prenom_utilisateur = elem["prenomUser"],
                mdp_utilisateur = elem["motDePasseUser"],
                email_utilisateur = elem["mailUser"],
                img_utilisateur =  elem["imgUser"],
                id_role = elem["role_id"],
                poidsUser = elem["poidsUser"],
                ddn_utilisateur = elem["ddnUser"],
                tel_utilisateur = elem["telUser"],
                sexe_utilisateur = elem["sexeUser"],
                cotisation = elem["cotisation"],
                )
            elif elem["role_id"] == 2: # Administrateur
                utilisateur = Utilisateur(
                id_utilisateur = elem["idUser"],
                nom_utilisateur = elem["nomUser"],
                prenom_utilisateur = elem["prenomUser"],
                mdp_utilisateur = sha256(elem["motDePasseUser"].encode()).hexdigest(),
                email_utilisateur = elem["mailUser"],
                img_utilisateur =  elem["imgUser"],
                id_role = elem["role_id"],
                poidsUser = elem["poidsUser"],
                ddn_utilisateur = elem["ddnUser"],
                tel_utilisateur = elem["telUser"],
                sexe_utilisateur = elem["sexeUser"],
                )
            elif elem["role_id"] == 3: # Moniteur
                utilisateur = Utilisateur(
                id_utilisateur = elem["idUser"],
                nom_utilisateur = elem["nomUser"],
                prenom_utilisateur = elem["prenomUser"],
                mdp_utilisateur = elem["motDePasseUser"],
                email_utilisateur = elem["mailUser"],
                img_utilisateur =  elem["imgUser"],
                id_role = elem["role_id"],
                poidsUser = elem["poidsUser"],
                ddn_utilisateur = elem["ddnUser"],
                tel_utilisateur = elem["telUser"],
                sexe_utilisateur = elem["sexeUser"],
                certification = elem["certification"],
                contrat = elem["contrat"],
                )
            elements["utilisateur"][elem["idUser"]] = utilisateur
            db.session.add(utilisateur)

        elif elem["type"] == "Cours":
            cours = Cours(
            idCo = elem["idCo"],
            nomCo = elem["nomCo"],
            date = elem["date"],
            id_utilisateur = elem["idUser"],
            )
            elements["cours"][elem["idCo"]] = cours
            db.session.add(cours)
        elif elem["type"] == "Horaire":
            horaire = Horaire(
                idHoraire=elem["idHoraire"],
                jour=elem["jour"],
                horaireDebut=time.fromisoformat(elem["horaireDebut"]),
                horaireFin=time.fromisoformat(elem["horaireFin"]),
            )
            elements["horaire"][elem["idHoraire"]] = horaire
            db.session.add(horaire)
        
        elif elem["type"] == "Poney":
            poney = Poney(
            idPo = elem["idPo"],
            nomPo = elem["nomPo"],
            poidsMax = elem["poidsMax"],
            couleurPo = elem["couleurPo"],
            ddnPo = elem["ddnPo"],
            )
            elements["poney"][elem["idPo"]] = poney
            db.session.add(poney)
        elif elem["type"] == "Reserver":
            reserver = Reserver(
            duree = elem["duree"],
            date = elem["date"],
            heureDebut = time.fromisoformat(elem["heure"]),
            nbPersonne = elem["nbPersonne"],
            collectif = elem["collectif"],
            nomRes = elem["nomRes"],
            idCo = elem["idCo"],
            idPo = elem["idPo"],
            id_utilisateur = elem["idUser"],
            )
            elements["reserver"][elem["idCo"], elem["idPo"], elem["idUser"]] = reserver
            db.session.add(reserver)
        elif elem["type"] == "Travailler":
            travailler = Travailler(
            id_utilisateur = elem["idUser"],
            idHoraire = elem["idHoraire"],
            )
            elements["travailler"][elem["idUser"], elem["idHoraire"]] = travailler
            db.session.add(travailler)
        elif elem["type"] == "Role":
            role = Role(
                id_role = elem["id_role"],
                name = elem["name"],
            )
            elements["role"]["id_role"] = role
            db.session.add(role)
            
        
    db.session.commit()
    print("Base de données chargée avec succès")


@app.cli.command()
def delete_db():
    '''Synchronizes the database.'''
    db.drop_all()
    