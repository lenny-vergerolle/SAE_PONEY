#from src.app import db
#
#class Moniteur(db.Model):
#    __tablename__ = 'MONITEUR'
#    
#    idMon = db.Column(db.Integer, primary_key=True)
#    nomMon = db.Column(db.String(45), nullable=False)
#    prenomMon = db.Column(db.String(45), nullable=False)
#    ddnMon = db.Column(db.Date, nullable=False)
#    sexeMon = db.Column(db.CHAR(1), nullable=False)
#    telMon = db.Column(db.String(45), nullable=False)
#    mailMon = db.Column(db.String(45), unique=True, nullable=False)
#    motsDePasseMon = db.Column(db.String(45), nullable=False)
#    poidsMon = db.Column(db.Float, nullable=False)
#    certification = db.Column(db.String(45), nullable=False)
#    contrat = db.Column(db.String(45), nullable=False)
#
#
#    # Relation vers les cours
#    cours = db.relationship('Cours', back_populates='moniteur')
#
#    # Relation avec Travailler
#    travailler = db.relationship('Travailler', back_populates='moniteur')