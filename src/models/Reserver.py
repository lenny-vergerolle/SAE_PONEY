from src.app import db

class Reserver(db.Model):
    __tablename__ = 'reserver'
    
    duree = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    heure = db.Column(db.Time, nullable=False)

    idCo = db.Column(db.Integer, db.ForeignKey('cours.idCo'), nullable=False)
    idPo = db.Column(db.Integer, db.ForeignKey('poney.idPo'), nullable=False)
    idAdh = db.Column(db.Integer, db.ForeignKey('adherent.idAdh'), nullable=False)
    
    adherent = db.relationship('Adherent', back_populates='reserver', lazy='True')
    cours = db.relationship('Cours', back_populates='reserver', lazy='True')
    poney = db.relationship('Poney', back_populates='reserver', lazy='True')