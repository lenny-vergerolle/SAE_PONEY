from flask_wtf import FlaskForm
from flask_security import current_user
from wtforms import DateField, StringField, HiddenField, FileField, PasswordField, RadioField, FloatField, SubmitField
from wtforms.validators import DataRequired
from hashlib import sha256
from src.models.Role import Role
from src.models.Utilisateur import Utilisateur
from flask import current_app
from wtforms.validators import Email
from flask_wtf.file import FileAllowed
from werkzeug.datastructures import FileStorage

class InscriptionForm(FlaskForm):
    id = HiddenField('id')
    nom_user = StringField('Nom', validators=[DataRequired()])
    prenom_user = StringField('Prenom', validators=[DataRequired()])
    mot_de_passe = PasswordField('Mot de passe', validators=[DataRequired()])
    confirmation_mot_de_passe = PasswordField('Confirmation mot de passe', validators=[DataRequired()])
    email = StringField('Adresse mail', validators=[DataRequired()])
    img = FileField('Photo de profil')
    #role = RadioField('Role', validators=[DataRequired()])
    ddn_user = DateField('Date de naissance', validators=[DataRequired()])
    sexeUser = RadioField('Sexe',choices=[('M', 'Masculin'), ('F', 'Féminin')])
    poidsUser = FloatField('Poids', validators=[DataRequired()])
    telUser = StringField('Telephone', validators=[DataRequired()])
    certificationUser = FileField('Certification')
    contratUser = FileField('Contrat')
    def validate(self, extra_validators=None):
        if not FlaskForm.validate(self, extra_validators=extra_validators):
            return False
        if self.mot_de_passe.data != self.confirmation_mot_de_passe.data:
            self.confirmation_mot_de_passe.errors.append('Les mots de passe ne correspondent pas')
            return False
        if Utilisateur.query.filter_by(email_utilisateur=self.email.data).first():
            self.email.errors.append('Un utilisateur existe déjà avec cette adresse mail')
            return False
        if '@' not in self.email.data or '.' not in self.email.data or len(self.email.data) < 8:
            self.email.errors.append("L'adresse mail doit contenir un '@', un '.' et au moins 8 caractères")
            return False
        return True

class ConnexionForm(FlaskForm):
    id=HiddenField('id')
    email=StringField('Adresse mail', validators=[DataRequired()])
    mot_de_passe=PasswordField('Mot de passe', validators=[DataRequired()])
    def get_authenticated_user(self):
        u = Utilisateur.query.filter_by(email_utilisateur=self.email.data).first()
        
        if u and u.mdp_utilisateur == sha256(self.mot_de_passe.data.encode()).hexdigest():
            return u
        return None
    
 
class UpdateUser(FlaskForm):
    id =HiddenField('id')
    nom_user = StringField("Nom", validators=[DataRequired()])
    prenom_user = StringField('Prenom', validators=[DataRequired()])
    email = StringField('Adresse mail', validators=[DataRequired()])
    telUser = StringField('Telephone', validators=[DataRequired()])
    poidsUser = FloatField('Poids', validators=[DataRequired()])
    img = FileField('Modifier la photo')
    def validate(self, extra_validators=None):
        if not super().validate(extra_validators=extra_validators):
            return False
        user = current_user
        if user.email_utilisateur != self.email.data and Utilisateur.query.filter_by(email_utilisateur=self.email.data).first():
            self.email.errors.append('Un utilisateur existe déjà avec cette adresse mail')
            return False
        return True