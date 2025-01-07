import click
from .app import app, db
from .models.Adherent import Adherent
from .models.Administrateur import Administrateur
from .models.Cours import Cours
from .models.Horaire import Horaire
from .models.Moniteur import Moniteur
from .models.Poney import Poney
from .models.Reserver import Reserver
from .models.Travailler import Travailler

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
        'adherent':{},
        'administrateur':{},
        'cours':{},
        'horaire':{},
        'moniteur':{},
        'poney':{},
        'reserver':{},
        'travailler':{},
    }

    for elem in data:
        if elem["type"] == "Utilisateur":
            utilisateur = Utilisateur(
            id_utilisateur = elem["idUser"],
            nomUser = elem["nomUser"],
            prenom_utilisateur = elem["prenomUser"]
    ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            ddnAdh = elem["ddnAdh"],
            sexeAdh = elem["sexeAdh"],
            telAdh = elem["telAdh"],
            mailAdh = elem["mailAdh"],
            motsDePasseAdh = elem["motsDePasseAdh"],
            poidsAdh = elem["poidsAdh"],
            cotisation = elem["cotisation"],
            )
            elements["adherent"][elem["idAdh"]] = adherent
            db.session.add(adherent)
            
            
        #elif elem["type"] == "Administrateur":
        #    administrateur = Administrateur(
        #    idAdm = elem["idAdm"],
        #    nomAdm = elem["nomAdm"],
        #    prenomAdm = elem["prenomAdm"],
        #    ddnAdm = elem["ddnAdm"],
        #    sexeAdm = elem["sexeAdm"],
        #    telAdm = elem["telAdm"],
        #    mailAdm = elem["mailAdm"],
        #    motsDePasseAdm = elem["motsDePasseAdm"],
        #    )
        #    elements["administrateur"][elem["idAdm"]] = administrateur
        #    db.session.add(administrateur)
        if elem["type"] == "Cours":
            cours = Cours(
            idCo = elem["idCo"],
            nomCo = elem["nomCo"],
            collectif = elem["collectif"],
            nbPersonne = elem["nbPersonne"],
            idMon = elem["idMon"],
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
        #elif elem["type"] == "Moniteur":
        #    moniteur = Moniteur(
        #    idMon = elem["idMon"],
        #    nomMon = elem["nomMon"],
        #    prenomMon = elem["prenomMon"],
        #    ddnMon = elem["ddnMon"],
        #    sexeMon = elem["sexeMon"],
        #    telMon = elem["telMon"],
        #    mailMon = elem["mailMon"],
        #    motsDePasseMon = elem["motsDePasseMon"],
        #    poidsMon = elem["poidsMon"],
        #    certification = elem["certification"],
        #    contrat = elem["contrat"],
        #    )
        #    elements["moniteur"][elem["idMon"]] = moniteur
        #    db.session.add(moniteur)

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
            heure = time.fromisoformat(elem["heure"]),
            idCo = elem["idCo"],
            idPo = elem["idPo"],
            idAdh = elem["idAdh"],
            )
            elements["reserver"][elem["idCo"], elem["idPo"], elem["idAdh"]] = reserver
            db.session.add(reserver)
        elif elem["type"] == "Travailler":
            travailler = Travailler(
            idMon = elem["idMon"],
            idHoraire = elem["idHoraire"],
            )
            elements["travailler"][elem["idMon"], elem["idHoraire"]] = travailler
            db.session.add(travailler)
        
    db.session.commit()
    print("Database loaded")