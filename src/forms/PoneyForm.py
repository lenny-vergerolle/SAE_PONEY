from flask_wtf import FlaskForm
from flask_security import current_user
from wtforms import BooleanField, DateField, IntegerField, SelectField, StringField, HiddenField, FileField, SelectMultipleField, PasswordField, RadioField, FloatField, SubmitField, TimeField, ValidationError
from wtforms.validators import DataRequired, NumberRange
from hashlib import sha256
from src.models.Poney import Poney

class PoneyForm(FlaskForm):
    nomPo = StringField('Nom du poney', validators=[DataRequired()])
    poidsMax = FloatField('Poids maximum', validators=[DataRequired()])
    couleurPo = StringField('Couleur du poney', validators=[DataRequired()])
    ddnPo = DateField('Date de naissance', validators=[DataRequired()])