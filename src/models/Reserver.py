from src.app import db

class Reserver(db.Model):
    __tablename__ = 'RESERVER'
    
    duree = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False, primary_key=True)
    heure = db.Column(db.Time, nullable=False, primary_key=True)

    idCo = db.Column(db.Integer, db.ForeignKey('COURS.idCo'), nullable=False, primary_key=True)
    idPo = db.Column(db.Integer, db.ForeignKey('PONEY.idPo'), nullable=False, primary_key=True)
    idAdh = db.Column(db.Integer, db.ForeignKey('ADHERENT.idAdh'), nullable=False, primary_key=True)
    
    adherent = db.relationship('Adherent', back_populates='reserver')
    cours = db.relationship('Cours', back_populates='reserver')
    poney = db.relationship('Poney', back_populates='reserver')