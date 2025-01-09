from src.app import db, login_manager
from flask_security import UserMixin
import uuid

# Classe Utilisateur
class Utilisateur(db.Model, UserMixin):
    __tablename__ = 'UTILISATEUR'

    id_utilisateur = db.Column(db.Integer, primary_key=True)
    nom_utilisateur = db.Column(db.Text)
    prenom_utilisateur = db.Column(db.Text)
    mdp_utilisateur = db.Column(db.Text)
    email_utilisateur = db.Column(db.Text, unique=True)
    img_utilisateur = db.Column(db.Text)
    id_role = db.Column(db.Integer, db.ForeignKey('ROLE.id_role'))
    poidsUser = db.Column(db.Float) 
    tel_utilisateur = db.Column(db.String(45)) 
    ddn_utilisateur = db.Column(db.String(45))
    sexe_utilisateur = db.Column(db.CHAR(1))
    cotisation = db.Column(db.Float)  #Pour les adherents
    certification = db.Column(db.String(45)) #Pour les moniteurs
    contrat = db.Column(db.String(45)) #Pour les moniteurs
    active = db.Column(db.Boolean, default=True)
    fs_uniquifier = db.Column(db.String(255), unique=True, default=lambda: str(uuid.uuid4()))  
    
    # Relation vers les reservations
    reserver = db.relationship('Reserver', back_populates='utilisateur')
 
    # Relation vers les cours
    cours = db.relationship('Cours', back_populates='utilisateur')

    # Relation avec Travailler
    travailler = db.relationship('Travailler', back_populates='utilisateur')

    role = db.relationship('Role', backref='utilisateurs')
    
    def is_adherent(self):
        return self.role_id == 1
    
    def is_admin(self):
        return self.role_id == 2

    def is_moniteur(self):
        return self.role_id == 3
    
    def get_last_id():
        id = 0
        users = Utilisateur.query.all()
        for user in users:
            if user.id_utilisateur > id:
                id = user.id_utilisateur
        return id

