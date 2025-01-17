
from src.app import db



class Historique(db.Model):

    __tablename__ = 'HISTORIQUE'

    nomRes = db.Column(db.String(50), nullable=False)
    duree = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False, primary_key=True)
    heureDebut = db.Column(db.Time, nullable=False, primary_key=True)
    nbPersonne = db.Column(db.Integer)
    collectif = db.Column(db.Boolean, nullable=False)
    id_moniteur = db.Column(db.Integer)

    idCo = db.Column(db.Integer, db.ForeignKey('COURS.idCo'), nullable=False, primary_key=True)
    idPo = db.Column(db.Integer, db.ForeignKey('PONEY.idPo'), nullable=False, primary_key=True)
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('UTILISATEUR.id_utilisateur'), nullable=False, primary_key=True)

    utilisateur = db.relationship('Utilisateur')
    cours = db.relationship('Cours')
    poney = db.relationship('Poney')
