from flask_wtf import FlaskForm
from flask_security import current_user
from wtforms import BooleanField, DateField, IntegerField, SelectField, StringField, HiddenField, FileField, PasswordField, RadioField, FloatField, SubmitField, TimeField
from wtforms.validators import DataRequired, NumberRange
from hashlib import sha256
from src.models.Role import Role
from src.models.Cours import Cours
from flask import current_app
from datetime import date

class CreationCoursForm(FlaskForm):
    nomCo = StringField('Nom du cours', validators=[DataRequired()])
    collectif = RadioField('Cours collectif',choices=[(True, 'Oui'), (False, 'Non')],validators=[DataRequired()])
    heureDebut = TimeField('Heure de début',format='%H:%M',render_kw={'min': '08:00', 'max': '17:00'}, validators=[DataRequired()])
    duree = IntegerField('Durée du cours', render_kw={"min": 1, 'max':2}, validators=[DataRequired()])
    date = DateField('Date du cours', default=date.today, render_kw={"min": date.today().strftime("%Y-%m-%d")} , validators=[DataRequired()])
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
    collectif = RadioField('Cours collectif',choices=[('true', 'Oui'), ('false', 'Non')])
    heureDebut = TimeField('Heure de début',format='%H:%M',render_kw={'min': '08:00', 'max': '17:00'}, validators=[DataRequired()])
    duree = IntegerField('Durée du cours',validators=[DataRequired(), NumberRange(min=1, max=2)])
    date = DateField('Date du cours', default=date.today, render_kw={"min": date.today().strftime("%Y-%m-%d")} , validators=[DataRequired()])
    nbPersonne = IntegerField('Nombre de personnes', render_kw={'min':1,'max':15}, validators=[DataRequired()])
    poneys = SelectField('Poney',coerce=int)
    moniteurs = SelectField('Moniteur',coerce=int)
    
    #def validate(self, extra_validators=None):
    #    if self.collectif.data == 'True':
    #        self.collectif.data = True
    #    elif self.collectif.data == 'False':
    #        self.collectif.data = False
    #    else:
    #        return False  
    #    return True
