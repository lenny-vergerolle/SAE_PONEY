from datetime import date
import unittest
from src.app import app_pour_tests, mkpath, db
from src.models import Utilisateur, Poney, Role

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
            
    def test_poney(self):
        with self.app.app_context():
            poney = Poney(idPo=1, nomPo="Eclair", poidsMax=100, couleurPo="noir", ddnPo=date(2018, 10, 25))
            Poney.add_poney(poney)
            
            eclair = db.session.get(Poney,1)
            self.assertIsNotNone(eclair)
            self.assertEqual(poney.nomPo, eclair.nomPo)
            self.assertEqual(eclair.nomPo, "Eclair")
            self.assertEqual(eclair.couleurPo, "noir")
            self.assertEqual(eclair.poidsMax, 100)
            self.assertEqual(eclair.ddnPo, date(2018, 10, 25))
            
    def test_role(self):
        with self.app.app_context():
            role1 = Role(id_role=1,name="Adhérent")
            Role.add_role(role1)
            adherent = db.session.get(Role,1)
            self.assertIsNotNone(adherent)
            self.assertEqual(role1.name, "Adhérent")
            
            role2 = Role(id_role=2,name="Moniteur")
            Role.add_role(role2)
            moniteur = db.session.get(Role,2)
            self.assertIsNotNone(moniteur)
            self.assertEqual(role2.name, "Moniteur")
            
            role3 = Role(id_role=3, name="Admin")
            Role.add_role(role3)
            admin = db.session.get(Role,3)
            self.assertIsNotNone(admin)
            self.assertEqual(role3.name, "Admin")
            

            
            