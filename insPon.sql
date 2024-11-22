-- Insertions générées principalement grâce à Chatgpt  

INSERT INTO HORAIRE (idHoraire, jour, horaireDebut, horaireFin) VALUES 
(1, 'Lundi', '08:00:00', '09:00:00'),
(2, 'Lundi', '09:00:00', '10:00:00'),
(3, 'Lundi', '10:00:00', '11:00:00'),
(4, 'Lundi', '11:00:00', '12:00:00'),
(5, 'Lundi', '13:00:00', '14:00:00'),
(6, 'Lundi', '14:00:00', '15:00:00'),
(7, 'Lundi', '15:00:00', '16:00:00'),
(8, 'Lundi', '16:00:00', '17:00:00'),
(9, 'Lundi', '17:00:00', '18:00:00'),
(10, 'Mardi', '08:00:00', '09:00:00'),
(11, 'Mardi', '09:00:00', '10:00:00'),
(12, 'Mardi', '10:00:00', '11:00:00'),
(13, 'Mardi', '11:00:00', '12:00:00'),
(14, 'Mardi', '13:00:00', '14:00:00'),
(15, 'Mardi', '14:00:00', '15:00:00'),
(16, 'Mardi', '15:00:00', '16:00:00'),
(17, 'Mardi', '16:00:00', '17:00:00'),
(18, 'Mardi', '17:00:00', '18:00:00'),
(19, 'Mercredi', '08:00:00', '09:00:00'),
(20, 'Mercredi', '09:00:00', '10:00:00'),
(21, 'Mercredi', '10:00:00', '11:00:00'),
(22, 'Mercredi', '11:00:00', '12:00:00'),
(23, 'Mercredi', '13:00:00', '14:00:00'),
(24, 'Mercredi', '14:00:00', '15:00:00'),
(25, 'Mercredi', '15:00:00', '16:00:00'),
(26, 'Mercredi', '16:00:00', '17:00:00'),
(27, 'Mercredi', '17:00:00', '18:00:00'),
(28, 'Jeudi', '08:00:00', '09:00:00'),
(29, 'Jeudi', '09:00:00', '10:00:00'),
(30, 'Jeudi', '10:00:00', '11:00:00'),
(31, 'Jeudi', '11:00:00', '12:00:00'),
(32, 'Jeudi', '13:00:00', '14:00:00'),
(33, 'Jeudi', '14:00:00', '15:00:00'),
(34, 'Jeudi', '15:00:00', '16:00:00'),
(35, 'Jeudi', '16:00:00', '17:00:00'),
(36, 'Jeudi', '17:00:00', '18:00:00'),
(37, 'Vendredi', '08:00:00', '09:00:00'),
(38, 'Vendredi', '09:00:00', '10:00:00'),
(39, 'Vendredi', '10:00:00', '11:00:00'),
(40, 'Vendredi', '11:00:00', '12:00:00'),
(41, 'Vendredi', '13:00:00', '14:00:00'),
(42, 'Vendredi', '14:00:00', '15:00:00'),
(43, 'Vendredi', '15:00:00', '16:00:00'),
(44, 'Vendredi', '16:00:00', '17:00:00'),
(45, 'Vendredi', '17:00:00', '18:00:00');


INSERT INTO PONEY (idPo, nomPo, poidsMax, couleurPo, ddnPo) VALUES 
(1, 'Robert', 130.71, 'Marron', STR_TO_DATE('22/01/2015', '%d/%m/%Y')),
(2, 'Brandon', 104.34, 'Marron', STR_TO_DATE('31/01/2017', '%d/%m/%Y')),
(3, 'Jimmy', 51.36, 'Tacheté', STR_TO_DATE('08/04/2017', '%d/%m/%Y')),
(4, 'Brad', 175.17, 'Marron', STR_TO_DATE('09/07/2021', '%d/%m/%Y')),
(5, 'Valerie', 76.36, 'Noir', STR_TO_DATE('19/07/2020', '%d/%m/%Y')),
(6, 'Matthew', 62.13, 'Gris', STR_TO_DATE('26/08/2021', '%d/%m/%Y')),
(7, 'Megan', 189.15, 'Marron', STR_TO_DATE('29/06/2017', '%d/%m/%Y')),
(8, 'Eddie', 100.48, 'Marron', STR_TO_DATE('12/09/2020', '%d/%m/%Y')),
(9, 'Gilbert', 106.27, 'Noir', STR_TO_DATE('07/12/2021', '%d/%m/%Y')),
(10, 'Michael', 129.53, 'Marron', STR_TO_DATE('27/09/2020', '%d/%m/%Y')),
(11, 'Cheryl', 110.68, 'Blanc', STR_TO_DATE('23/01/2018', '%d/%m/%Y')),
(12, 'Barbara', 143.51, 'Tacheté', STR_TO_DATE('08/06/2017', '%d/%m/%Y')),
(13, 'Taylor', 159.54, 'Tacheté', STR_TO_DATE('28/01/2018', '%d/%m/%Y')),
(14, 'John', 165.2, 'Tacheté', STR_TO_DATE('08/04/2020', '%d/%m/%Y')),
(15, 'Emma', 132.77, 'Marron', STR_TO_DATE('03/05/2023', '%d/%m/%Y'));


INSERT INTO MONITEUR (idMon, nomMon, prenomMon, ddnMon, sexeMon, telMon, mailMon, motsDePasseMon, poidsMon, certification, contrat) VALUES 
(1, 'Miller', 'David', STR_TO_DATE('03/08/1997', '%d/%m/%Y'), 'M', '0609017071', 'david.miller@mail.com', '1234', 79.2, 'médical', 'Stage'),
(2, 'Robertson', 'Bethany', STR_TO_DATE('02/02/1986', '%d/%m/%Y'), 'F', '0608850585', 'bethany.robertson@mail.com', '1234', 60.08, 'santé', 'Stage'),
(3, 'Martinez', 'John', STR_TO_DATE('17/03/1996', '%d/%m/%Y'), 'M', '0699267632', 'john.martinez@mail.com', '1234', 86.62, 'agent', 'CDD'),
(4, 'Spencer', 'Nicholas', STR_TO_DATE('30/10/1988', '%d/%m/%Y'), 'M', '0695270019', 'nicholas.spencer@mail.com', '1234', 78.64, 'performance', 'CDD'),
(5, 'Gentry', 'Brett', STR_TO_DATE('06/09/1992', '%d/%m/%Y'), 'M', '0694458870', 'brett.gentry@mail.com', '1234', 85.65, 'terrain', 'CDD'),
(6, 'Bell', 'Samantha', STR_TO_DATE('26/06/1994', '%d/%m/%Y'), 'F', '0626531274', 'samantha.bell@mail.com', '1234', 92.43, 'avenir', 'CDI'),
(7, 'Conrad', 'Terry', STR_TO_DATE('18/02/1979', '%d/%m/%Y'), 'M', '0627816522', 'terry.conrad@mail.com', '1234', 66.22, 'centre', 'Stage'),
(8, 'Herrera', 'Laura', STR_TO_DATE('03/03/2000', '%d/%m/%Y'), 'F', '0648838258', 'laura.herrera@mail.com', '1234', 98.99, 'et', 'Stage'),
(9, 'Reyes', 'Richard', STR_TO_DATE('08/07/1970', '%d/%m/%Y'), 'M', '0641892005', 'richard.reyes@mail.com', '1234', 63.69, 'matière', 'CDD'),
(10, 'Lin', 'Holly', STR_TO_DATE('07/06/1986', '%d/%m/%Y'), 'F', '0626916238', 'holly.lin@mail.com', '1234', 82.03, 'large', 'CDI');


INSERT INTO ADHERENT (idAdh, nomAdh, prenomAdh, ddnAdh, sexeAdh, telAdh, mailAdh, motsDePasseAdh, poidsAdh, cotisation) VALUES 
(1, 'Newton', 'Sabrina', STR_TO_DATE('06/12/1998', '%d/%m/%Y'), 'F', '0695249101', 'sabrina.newton@mail.com', '1234', 65.2, TRUE),
(2, 'Snyder', 'Sarah', STR_TO_DATE('28/09/1994', '%d/%m/%Y'), 'F', '0616275479', 'sarah.snyder@mail.com', '1234', 58.5, FALSE),
(3, 'Perry', 'Richard', STR_TO_DATE('30/09/1992', '%d/%m/%Y'), 'M', '0791721451', 'richard.perry@mail.com', '1234', 75.8, TRUE),
(4, 'Barker', 'Shelley', STR_TO_DATE('27/08/2005', '%d/%m/%Y'), 'F', '0674056426', 'shelley.barker@mail.com', '1234', 62.3, FALSE),
(5, 'Douglas', 'April', STR_TO_DATE('26/12/2007', '%d/%m/%Y'), 'F', '0759874602', 'april.douglas@mail.com', '1234', 54.7, TRUE),
(6, 'Pena', 'Jacob', STR_TO_DATE('27/12/1990', '%d/%m/%Y'), 'M', '0623643416', 'jacob.pena@mail.com', '1234', 82.1, TRUE),
(7, 'Sanchez', 'Brian', STR_TO_DATE('16/11/2006', '%d/%m/%Y'), 'M', '0649161921', 'brian.sanchez@mail.com', '1234', 68.4, FALSE),
(8, 'Moore', 'Travis', STR_TO_DATE('16/04/2004', '%d/%m/%Y'), 'M', '0649184428', 'travis.moore@mail.com', '1234', 79.0, TRUE),
(9, 'Gomez', 'Jessica', STR_TO_DATE('05/09/1996', '%d/%m/%Y'), 'F', '0658878773', 'jessica.gomez@mail.com', '1234', 63.6, TRUE),
(10, 'Krueger', 'Michael', STR_TO_DATE('08/02/2007', '%d/%m/%Y'), 'M', '0636023706', 'michael.krueger@mail.com', '1234', 72.2, FALSE),
(11, 'Johnson', 'Zachary', STR_TO_DATE('28/09/2007', '%d/%m/%Y'), 'M', '0610956473', 'zachary.johnson@mail.com', '1234', 77.4, TRUE),
(12, 'Smith', 'Marc', STR_TO_DATE('03/07/2004', '%d/%m/%Y'), 'M', '0640617359', 'marc.smith@mail.com', '1234', 66.9, FALSE),
(13, 'Burton', 'Justin', STR_TO_DATE('27/02/2003', '%d/%m/%Y'), 'M', '0635630182', 'justin.burton@mail.com', '1234', 78.6, TRUE),
(14, 'Reid', 'Kaylee', STR_TO_DATE('05/03/2000', '%d/%m/%Y'), 'F', '0639562409', 'kaylee.reid@mail.com', '1234', 59.8, TRUE),
(15, 'Lowe', 'Sabrina', STR_TO_DATE('22/04/2001', '%d/%m/%Y'), 'F', '0663954049', 'sabrina.lowe@mail.com', '1234', 64.5, FALSE),
(16, 'James', 'Anthony', STR_TO_DATE('04/11/1992', '%d/%m/%Y'), 'M', '0651643708', 'anthony.james@mail.com', '1234', 84.3, TRUE),
(17, 'Jimenez', 'Sara', STR_TO_DATE('28/11/2006', '%d/%m/%Y'), 'F', '0648178093', 'sara.jimenez@mail.com', '1234', 57.6, FALSE),
(18, 'Keller', 'David', STR_TO_DATE('04/12/1990', '%d/%m/%Y'), 'M', '0632068920', 'david.keller@mail.com', '1234', 89.7, TRUE),
(19, 'Hayes', 'Ana', STR_TO_DATE('15/08/1999', '%d/%m/%Y'), 'F', '0648568412', 'ana.hayes@mail.com', '1234', 60.9, FALSE);


INSERT INTO ADMINISTRATEUR (idAdm, nomAdm, prenomAdm, ddnAdm, sexeAdm, telAdm, mailAdm, motsDePasseAdm) VALUES 
(1, 'Sandoval', 'Benjamin', STR_TO_DATE('15/05/1985', '%d/%m/%Y'), 'M', '0612345678', 'benjamin.sandoval@mail.com', '1234'),
(2, 'Schroeder', 'Nicole', STR_TO_DATE('22/08/1987', '%d/%m/%Y'), 'F', '0623456789', 'nicole.schroeder@mail.com', '1234'),
(3, 'Smith', 'Christopher', STR_TO_DATE('10/12/1983', '%d/%m/%Y'), 'M', '0634567890', 'christopher.smith@mail.com', '1234'),
(4, 'Norman', 'Elizabeth', STR_TO_DATE('05/07/1990', '%d/%m/%Y'), 'F', '0645678901', 'elizabeth.norman@mail.com', '1234'),
(5, 'Brown', 'Richard', STR_TO_DATE('28/02/1980', '%d/%m/%Y'), 'M', '0656789012', 'richard.brown@mail.com', '1234');


INSERT INTO COURS (idCo, nomCo, colllectif, nbPersonne, idMon) VALUES 
(1, 'Cours Débutant', TRUE, 8, 1),
(2, 'Cours Avancé', TRUE, 5, 2),
(3, 'Cours Individuel', FALSE, NULL, 3),
(4, 'Cours Collectif', TRUE, 7, 4),
(5, 'Cours Enfants', TRUE, 6, 5),
(6, 'Cours Adultes', TRUE, 10, 6),
(7, 'Cours Équilibre', FALSE, NULL, 7),
(8, 'Cours Perfectionnement', TRUE, 4, 8),
(9, 'Cours Liberté', TRUE, 9, 9),
(10, 'Cours Sécurité', FALSE, NULL, 10);


INSERT INTO RESERVER (duree, date, heure, idCo, idPo, idAdh) VALUES 
(1, STR_TO_DATE('21/11/2024', '%d/%m/%Y'), '08:00', 1, 1, 1),
(2, STR_TO_DATE('21/11/2024', '%d/%m/%Y'), '09:00', 2, 2, 2),
(1, STR_TO_DATE('22/11/2024', '%d/%m/%Y'), '10:00', 3, 3, 3),
(1, STR_TO_DATE('22/11/2024', '%d/%m/%Y'), '11:00', 4, 4, 4),
(2, STR_TO_DATE('23/11/2024', '%d/%m/%Y'), '08:00', 5, 5, 5),
(1, STR_TO_DATE('23/11/2024', '%d/%m/%Y'), '09:00', 6, 6, 6),
(1, STR_TO_DATE('24/11/2024', '%d/%m/%Y'), '10:00', 7, 7, 7),
(2, STR_TO_DATE('24/11/2024', '%d/%m/%Y'), '11:00', 8, 8, 8),
(1, STR_TO_DATE('25/11/2024', '%d/%m/%Y'), '08:00', 9, 9, 9),
(1, STR_TO_DATE('25/11/2024', '%d/%m/%Y'), '09:00', 10, 10, 10);


INSERT INTO TRAVAILLER (idMon, idHoraire) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(1, 11),
(2, 12),
(3, 13),
(4, 14),
(5, 15),
(6, 16),
(7, 17),
(8, 18),
(9, 19),
(10, 20);



-- insertions qui ne passent pas  
INSERT INTO ADHERENT (idAdh, nomAdh, prenomAdh, ddnAdh, sexeAdh, telAdh, mailAdh, motsDePasseAdh, poidsAdh, cotisation) VALUES 
(20, 'Moore', 'Jamie', STR_TO_DATE('26/04/2023', '%d/%m/%Y'), 'F', '0632047668', 'jamie.moore@mail.com', '1234', 62.7, TRUE);


INSERT INTO RESERVER (duree, date, heure, idCo, idPo, idAdh) VALUES 
(1, STR_TO_DATE('21/11/2024', '%d/%m/%Y'), '08:00', 1, 15, 1);