from src.app import db

class Travailler(db.Model):
    __tablename__ = 'TRAVAILLER'
    
    idMon = db.Column(db.Integer, db.ForeignKey('MONITEUR.idMon'), primary_key=True)
    idHoraire = db.Column(db.Integer, db.ForeignKey('HORAIRE.idHoraire'), primary_key=True)

    moniteur = db.relationship('Moniteur', back_populates='travailler', lazy='True')
    horaire = db.relationship('Horaire', back_populates='travailler', lazy='True')
    