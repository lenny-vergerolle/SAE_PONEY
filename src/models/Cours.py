from src.app import db

class Cours(db.Model):
    __tablename__ = 'COURS'
    
    idCo = db.Column(db.Integer, primary_key=True)
    nomCo = db.Column(db.String(42))
    collectif = db.Column(db.Boolean)
    nbPersonne = db.Column(db.Integer)
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('UTILISATEUR.id_utilisateur'))

    utilisateur = db.relationship('Utilisateur', back_populates='cours')
    reserver = db.relationship('Reserver', back_populates='cours')
