from src.app import db

class Reserver(db.Model):
    __tablename__ = 'RESERVER'
    
    nomRes = db.Column(db.String(50), nullable=False)
    duree = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False, primary_key=True)
    heure = db.Column(db.Time, nullable=False, primary_key=True)

    idCo = db.Column(db.Integer, db.ForeignKey('COURS.idCo'), nullable=False, primary_key=True)
    idPo = db.Column(db.Integer, db.ForeignKey('PONEY.idPo'), nullable=False, primary_key=True)
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('UTILISATEUR.id_utilisateur'), nullable=False, primary_key=True)
    
    utilisateur = db.relationship('Utilisateur', back_populates='reserver')
    cours = db.relationship('Cours', back_populates='reserver')
    poney = db.relationship('Poney', back_populates='reserver')