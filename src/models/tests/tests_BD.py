from datetime import date
import unittest
from src.app import app_pour_tests, mkpath, db
from src.models import Utilisateur

class tests_BD(unittest.TestCase):
    def setUp(self):
        self.app = app_pour_tests()
        self.client = self.app.test_client()       
        with self.app.app_context():
            db.create_all()
            
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            
    def test_utilisateur(self):
        with self.app.app_context():
            utilisateur = Utilisateur(id_utilisateur=1,nom_utilisateur="Dupond",prenom_utilisateur="Pierre",mdp_utilisateur="1234",email_utilisateur="dupond@mail.com",img_utilisateur=None,id_role=1,poidsUser=70,tel_utilisateur="1234567890",ddn_utilisateur="12/30/2000",sexe_utilisateur="M")
            Utilisateur.add_utilisateur(utilisateur)
            
            dupond = db.session.get(Utilisateur,1)
            self.assertIsNotNone(dupond)
            self.assertEqual(utilisateur.nom_utilisateur, dupond.nom_utilisateur)
            self.assertEqual(dupond.prenom_utilisateur, "Pierre")
            self.assertEqual(dupond.sexe_utilisateur, "M")
            self.assertIn("@mail.com", dupond.email_utilisateur)

            self.assertTrue(dupond.is_adherent())
            self.assertFalse(dupond.is_admin())
            self.assertFalse(dupond.is_moniteur())
            self.assertEqual(Utilisateur.get_last_id(),dupond.id_utilisateur)
