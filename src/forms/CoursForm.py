from flask_wtf import FlaskForm
from flask_security import current_user
from wtforms import BooleanField, DateField, IntegerField, SelectField, StringField, HiddenField, FileField, SelectMultipleField, PasswordField, RadioField, FloatField, SubmitField, TimeField, ValidationError
from wtforms.validators import DataRequired, NumberRange
from hashlib import sha256
from src.models.Role import Role
from src.models.Cours import Cours
from flask import current_app
from datetime import date, datetime, time, timedelta

class CreationCoursForm(FlaskForm):
    nomCo = StringField('Nom du cours', validators=[DataRequired()])
    adherents = SelectField('Adherent',coerce=int)
    #def validate(self, extra_validators=None):
    #    if self.collectif.data == 'True':
    #        self.collectif.data = True
    #    elif self.collectif.data == 'False':
    #        self.collectif.data = False
    #    else:
    #        return False  
    #    return True
   
class ReservationCoursForm(FlaskForm):
    nomRes = StringField('Nom de la réservation', validators=[DataRequired()])
    collectif = RadioField('Cours collectif',choices=[('true', 'Oui'), ('false', 'Non')], default='false', validators=[DataRequired()])
    heureDebut = TimeField('Heure de début', format='%H:%M', render_kw={'min': '08:00', 'max': '18:00'}, validators=[DataRequired()])
    id_moniteur = HiddenField('id_moniteur')
    def validate_heureDebut(self, field):
        heure = field.data
        if not ((heure >= time(8, 0) and heure <= time(12, 0)) or (heure >= time(14, 0) and heure <= time(18, 0))):
            raise ValidationError('L heure doit être entre 8h00 et 12h00 ou entre 14h00 et 18h00.')
    duree = IntegerField('Durée du cours',validators=[DataRequired(), NumberRange(min=1, max=2)])
    date = DateField('Date du cours', default=date.today()+timedelta(days=1), render_kw={"min": (date.today()+timedelta(days=1)).strftime("%Y-%m-%d"), 'max': (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")}, validators=[DataRequired()])
    nbPersonne = IntegerField('Nombre de personnes', render_kw={'min':1,'max':15}, validators=[DataRequired()])
    poneys = SelectField('Poney',coerce=int)
    moniteurs = SelectField('Moniteur',coerce=int)
    cours = SelectField('Cours',coerce=int)
    
    