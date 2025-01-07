from src.app import db

class Cours(db.Model):
    __tablename__ = 'COURS'
    
    idCo = db.Column(db.Integer, primary_key=True)
    nomCo = db.Column(db.String(42))
    collectif = db.Column(db.Boolean)
    nbPersonne = db.Column(db.Integer)
    idMon = db.Column(db.Integer, db.ForeignKey('MONITEUR.idMon'))

    moniteur = db.relationship('Moniteur', back_populates='cours')
    reserver = db.relationship('Reserver', back_populates='cours')
