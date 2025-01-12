from src.app import db
from sqlalchemy.types import Time

class Cours(db.Model):
    __tablename__ = 'COURS'
    
    idCo = db.Column(db.Integer, primary_key=True)
    nomCo = db.Column(db.String(42))
    #collectif = db.Column(db.Boolean)
    #duree = db.Column(db.Integer)
    #heureDebut =  db.Column(Time, nullable=False) 
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('UTILISATEUR.id_utilisateur'))
    date = db.Column(db.Date)
    utilisateur = db.relationship('Utilisateur', back_populates='cours')
    reserver = db.relationship('Reserver', back_populates='cours')

    def get_last_id():
        id = 0
        cours = Cours.query.all()
        for cour in cours:
            if cour.idCo > id:
                id = cour.idCo
        return id

    def add_cours(self):
        db.session.add(self)
        db.session.commit()