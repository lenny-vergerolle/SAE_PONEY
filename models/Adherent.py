from src.app import db

class Adherent(db.Model):
    __tablename__ = 'ADHERENT'
    
    idAdh = db.Column(db.Integer, primary_key=True)
    nomAdh = db.Column(db.String(45), nullable=False)
    prenomAdh = db.Column(db.String(45), nullable=False)
    ddnAdh = db.Column(db.Date, nullable=False)
    sexeAdh = db.Column(db.CHAR(1), nullable=False)
    telAdh = db.Column(db.String(45), nullable=False)
    mailAdh = db.Column(db.String(45), unique=True, nullable=False)
    motsDePasseAdh = db.Column(db.String(45), nullable=False)
    poidsAdh = db.Column(db.Float, nullable=False)
    cotisation = db.Column(db.Boolean, nullable=False)

