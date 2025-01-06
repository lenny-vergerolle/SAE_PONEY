from src.app import db

class Poney(db.Model):
    __tablename__ = 'PONEY'
    
    idPo = db.Column(db.Integer, primary_key=True)
    nomPo = db.Column(db.String(45))
    poidsMax = db.Column(db.Float)
    couleurPo = db.Column(db.String(45))
    ddnPo = db.Column(db.Date)
