from src.app import db

# Classe Horaire
class Horaire(db.Model):
    __tablename__ = 'HORAIRE'

    id_horaire = db.Column(db.Integer, primary_key=True)
    jour = db.Column(db.String(45))
    horaire_debut = db.Column(db.Time)
    horaire_fin = db.Column(db.Time)
