from src.app import db

class Travailler(db.Model):
    __tablename__ = 'TRAVAILLER'
    
    id_utilisateur= db.Column(db.Integer, db.ForeignKey('UTILISATEUR.id_utilisateur'), primary_key=True)
    idHoraire = db.Column(db.Integer, db.ForeignKey('HORAIRE.idHoraire'), primary_key=True)

    # Relations vers les autres tables
    utilisateur= db.relationship('Utilisateur', back_populates='travailler')
    horaire = db.relationship('Horaire', back_populates='travailler')
