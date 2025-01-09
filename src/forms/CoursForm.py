from flask_wtf import FlaskForm
from flask_security import current_user
from wtforms import BooleanField, DateField, IntegerField, StringField, HiddenField, FileField, PasswordField, RadioField, FloatField, SubmitField
from wtforms.validators import DataRequired
from hashlib import sha256
from src.models.Role import Role
from src.models.Cours import Cours
from flask import current_app

class CreationCoursForm(FlaskForm):
    nomCo = StringField('Nom du cours', validators=[DataRequired()])
    collectif = RadioField('Cours collectif',choices=[(True, 'Oui'), (False, 'Non')], validators=[DataRequired()])
    nbPersonne = IntegerField('Nombre de personnes', validators=[DataRequired()])
    #def validate(self, extra_validators=None):
    #    if self.collectif.data == 'True':
    #        self.collectif.data = True
    #    elif self.collectif.data == 'False':
    #        self.collectif.data = False
    #    else:
    #        return False  
    #    return True
        
