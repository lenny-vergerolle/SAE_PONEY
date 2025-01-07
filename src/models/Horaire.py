from src.app import db

# Classe Horaire
class Horaire(db.Model):
    __tablename__ = 'HORAIRE'

    idHoraire = db.Column(db.Integer, primary_key=True)
    jour = db.Column(db.String(45))
    horaireDebut = db.Column(db.Time)
    horaireFin = db.Column(db.Time)

    # Relation avec Travailler
    travailler = db.relationship('Travailler', back_populates='horaire', lazy='dynamic')