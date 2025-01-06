from src.app import db

class Administrateur(db.Model):
    __tablename__ = 'ADMINISTRATEUR'
    
    idAdm = db.Column(db.Integer, primary_key=True)
    nomAdm = db.Column(db.String(45))
    prenomAdm = db.Column(db.String(45))
    ddnAdm = db.Column(db.String(45))
    sexeAdm = db.Column(db.CHAR(1))
    telAdm = db.Column(db.String(45))
    mailAdm = db.Column(db.String(45), unique=True)
    motsDePasseAdm = db.Column(db.String(45))