from src.app import db

class Travailler(db.Model):
    __tablename__ = 'TRAVAILLER'
    
    idMon = db.Column(db.Integer, db.ForeignKey('MONITEUR.idMon'), primary_key=True)
    idHoraire = db.Column(db.Integer, db.ForeignKey('HORAIRE.idHoraire'), primary_key=True)

    # Relations vers les autres tables
    moniteur = db.relationship('Moniteur', back_populates='travailler')
    horaire = db.relationship('Horaire', back_populates='travailler')
