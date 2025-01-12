import unittest
from src.app import app, mkpath, db
from src.commands import loaddb

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
