import unittest

from sqlalchemy import null
from src.app import app, mkpath, db
from src.commands import loaddb
from src.models import Utilisateur

class tests_BD(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            self.db_uri = ('sqlite:///'+mkpath('poney.db'))
            app.config['TESTING'] = True
            app.config['WTF_CSRF_ENABLED'] = False
            app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri
            self.app = app.test_client()
            loaddb(db)
            db.drop_all()
            db.create_all()
            
    def test_utilisateur(self):
        with app.app_context():
            utilisateur = Utilisateur(1,"Dupond","Pierre","1234","dupond@mail.com",null,1,70,"1234567890","12/30/2000","M")
            Utilisateur.add_utilisateur(utilisateur)
            
                                      
