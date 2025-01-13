from datetime import date, time 
import unittest
from src.app import app_pour_tests, db
from src.models import Utilisateur, Poney, Role, Cours, Horaire, Travailler, Reserver

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
            
            moniteur = Utilisateur(id_utilisateur=2,nom_utilisateur="Mirabelle",prenom_utilisateur="Paul",mdp_utilisateur="1234",email_utilisateur="paul@mail.com",img_utilisateur=None,id_role=3,poidsUser=85,tel_utilisateur="1234567890",ddn_utilisateur="1/3/1997",sexe_utilisateur="M")
            Utilisateur.add_utilisateur(moniteur)
            
            dupond = db.session.get(Utilisateur,1)
            self.assertIsNotNone(dupond)
            self.assertEqual(utilisateur.nom_utilisateur, dupond.nom_utilisateur)
            self.assertEqual(dupond.prenom_utilisateur, "Pierre")
            self.assertEqual(dupond.sexe_utilisateur, "M")
            self.assertIn("@mail.com", dupond.email_utilisateur)

            self.assertTrue(dupond.is_adherent())
            self.assertFalse(dupond.is_admin())
            self.assertFalse(dupond.is_moniteur())
            self.assertEqual(Utilisateur.get_last_id(),moniteur.id_utilisateur)
            
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
            
    def test_cours(self):
        with self.app.app_context():
            cours = Cours(idCo=1,nomCo="initiation au poney",id_utilisateur=1,id_adherent=1)
            Cours.add_cours(cours)

            initiation = db.session.get(Cours,1)
            self.assertIsNotNone(initiation)
            self.assertEqual(cours.nomCo, initiation.nomCo)
            self.assertEqual(initiation.id_utilisateur, 1)
            self.assertEqual(initiation.id_adherent,1)
            
    def test_horaires(self):
        with self.app.app_context():
            horaire = Horaire(idHoraire=1,jour="lundi",horaireDebut=time(9,0,0),horaireFin=time(10,0,0))
            Horaire.add_horaire(horaire)
            
            lundi = db.session.get(Horaire,1)
            self.assertIsNotNone(lundi)
            self.assertEqual(horaire.jour, "lundi")
            self.assertEqual(lundi.horaireDebut, time(9,0,0))
            self.assertEqual(lundi.horaireFin, time(10,0,0))
            
    def test_travailler(self):
        with self.app.app_context():
            travailler = Travailler(id_utilisateur=1, idHoraire=1)
            Travailler.add_travailler(travailler)
            
            travail = db.session.get(Travailler,(1,1))
            self.assertIsNotNone(travail)
            self.assertEqual(travailler.id_utilisateur, travail.id_utilisateur)
            self.assertEqual(travailler.idHoraire, travail.idHoraire)
            self.assertEqual(travail.id_utilisateur, 1)
            self.assertEqual(travail.idHoraire, 1)
            
    def test_reserver(self):
        with self.app.app_context():
            reserver = Reserver(nomRes="reservation",duree=1,date=date(2025,4,4),heureDebut=time(9,0,0),nbPersonne=1,collectif=False,id_moniteur=2,idCo=1,idPo=1,id_utilisateur=1)
            Reserver.add_reserver(reserver)
            
            reservation = db.session.get(Reserver,(date(2025,4,4),time(9,0,0),1,1,1))
            self.assertIsNotNone(reservation)
            self.assertEqual(reserver.idCo, reservation.idCo)
            self.assertEqual(reserver.idPo, reservation.idPo)
            self.assertEqual(reserver.id_utilisateur, reservation.id_utilisateur)
            self.assertEqual(reservation.idCo, 1)
            self.assertEqual(reservation.idPo, 1)
            self.assertEqual(reservation.id_utilisateur, 1)
            self.assertEqual(reservation.date,date(2025,4,4))
            self.assertEqual(reservation.heureDebut,time(9,0,0))
            self.assertFalse(reservation.collectif)