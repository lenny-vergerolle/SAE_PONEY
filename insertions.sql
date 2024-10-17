-- Insertions générées principalement grâce à Chatgpt  

INSERT INTO HORAIRE (idHoraire, horaireDebut, horaireFin) VALUES
(1, '08:00:00', '09:00:00'),
(2, '09:00:00', '10:00:00'),
(3, '10:00:00', '11:00:00'),
(4, '11:00:00', '12:00:00'),
(5, '12:00:00', '13:00:00'),
(6, '13:00:00', '14:00:00'),
(7, '14:00:00', '15:00:00'),
(8, '15:00:00', '16:00:00'),
(9, '16:00:00', '17:00:00'),
(10, '17:00:00', '18:00:00');


INSERT INTO PONEY (idPo, nomPo, poidsMax, couleurPo, ddnPo) VALUES
(1, 'Tonnerre', 200, 'Noir', STR_TO_DATE('01/05/2015', '%d/%m/%Y')),
(2, 'Eclair', 150, 'Blanc', STR_TO_DATE('15/06/2016', '%d/%m/%Y')),
(3, 'Lenny', 180, 'Alezan', STR_TO_DATE('20/03/2017', '%d/%m/%Y')),
(4, 'Shadow', 220, 'Gris', STR_TO_DATE('30/08/2014', '%d/%m/%Y')),
(5, 'Zigzag', 190, 'Bai', STR_TO_DATE('14/02/2018', '%d/%m/%Y')),
(6, 'Roudoudou', 170, 'Pie', STR_TO_DATE('05/12/2015', '%d/%m/%Y')),
(7, 'Fury', 160, 'Noir et blanc', STR_TO_DATE('20/11/2016', '%d/%m/%Y')),
(8, 'Caramel', 210, 'Châtain', STR_TO_DATE('19/07/2014', '%d/%m/%Y')),
(9, 'Pégase', 175, 'Noir', STR_TO_DATE('01/09/2017', '%d/%m/%Y')),
(10, 'Choco', 185, 'Bai', STR_TO_DATE('12/04/2015', '%d/%m/%Y'));


INSERT INTO MONITEUR (idMon, nomMon, prenomMon, ddnMon, sexeMon, telMon, mailMon, poidsMon, certification, contrat) VALUES
(1, 'Dupont', 'Jean', STR_TO_DATE('15/01/1980', '%d/%m/%Y'), 'M', '0612345678', 'jean.dupont@email.com', 75, 'CCE', 'CDI'),
(2, 'Martin', 'Sophie', STR_TO_DATE('20/03/1990', '%d/%m/%Y'), 'F', '0623456789', 'sophie.martin@email.com', 60, 'CET', 'CDD'),
(3, 'Bernard', 'Luc', STR_TO_DATE('25/06/1985', '%d/%m/%Y'), 'M', '0634567890', 'luc.bernard@email.com', 70, 'CCE', 'CDI'),
(4, 'Leroy', 'Clara', STR_TO_DATE('30/08/1992', '%d/%m/%Y'), 'F', '0645678901', 'clara.leroy@email.com', 55, 'CET', 'CDD'),
(5, 'Moreau', 'Paul', STR_TO_DATE('12/10/1978', '%d/%m/%Y'), 'M', '0656789012', 'paul.moreau@email.com', 80, 'CCE', 'CDI'),
(6, 'Garnier', 'Alice', STR_TO_DATE('01/12/1995', '%d/%m/%Y'), 'F', '0667890123', 'alice.garnier@email.com', 58, 'CET', 'CDD'),
(7, 'Boucher', 'François', STR_TO_DATE('17/02/1988', '%d/%m/%Y'), 'M', '0678901234', 'francois.boucher@email.com', 72, 'CCE', 'CDI'),
(8, 'Dumas', 'Julie', STR_TO_DATE('05/05/1991', '%d/%m/%Y'), 'F', '0689012345', 'julie.dumas@email.com', 65, 'CET', 'CDD'),
(9, 'Morel', 'Henri', STR_TO_DATE('22/11/1982', '%d/%m/%Y'), 'M', '0690123456', 'henri.morel@email.com', 77, 'CCE', 'CDI'),
(10, 'Michel', 'Laura', STR_TO_DATE('09/09/1993', '%d/%m/%Y'), 'F', '0601234567', 'laura.michel@email.com', 62, 'CET', 'CDD');


INSERT INTO ADHERENT (idAdh, nomAdh, prenomAdh, ddnAdh, sexeAdh, telAdh, mailAdh, poidsAdh, cotisation) VALUES
(1, 'Durand', 'Pierre', STR_TO_DATE('01/01/2000', '%d/%m/%Y'), 'M', '0701234567', 'pierre.durand@email.com', 70, TRUE),
(2, 'Roux', 'Chloé', STR_TO_DATE('14/02/1995', '%d/%m/%Y'), 'F', '0712345678', 'chloe.roux@email.com', 55, TRUE),
(3, 'Petit', 'Lucas', STR_TO_DATE('23/03/1998', '%d/%m/%Y'), 'M', '0723456789', 'lucas.petit@email.com', 80, FALSE),
(4, 'Blanc', 'Emma', STR_TO_DATE('30/04/1992', '%d/%m/%Y'), 'F', '0734567890', 'emma.blanc@email.com', 60, TRUE),
(5, 'Lemoine', 'Noah', STR_TO_DATE('15/05/1987', '%d/%m/%Y'), 'M', '0745678901', 'noah.lemoine@email.com', 75, FALSE),
(6, 'Giraud', 'Juliette', STR_TO_DATE('10/06/1990', '%d/%m/%Y'), 'F', '0756789012', 'juliette.giraud@email.com', 50, TRUE),
(7, 'Charpentier', 'Victor', STR_TO_DATE('05/07/1985', '%d/%m/%Y'), 'M', '0767890123', 'victor.charpentier@email.com', 85, TRUE),
(8, 'Faure', 'Alice', STR_TO_DATE('12/08/1993', '%d/%m/%Y'), 'F', '0778901234', 'alice.faure@email.com', 68, FALSE),
(9, 'Jacques', 'Léo', STR_TO_DATE('22/09/1988', '%d/%m/%Y'), 'M', '0789012345', 'leo.jacques@email.com', 90, TRUE),
(10, 'Boyer', 'Zoé', STR_TO_DATE('15/10/1991', '%d/%m/%Y'), 'F', '0790123456', 'zoe.boyer@email.com', 58, TRUE),
(11, 'Simon', 'Thomas', STR_TO_DATE('03/11/1994', '%d/%m/%Y'), 'M', '0712345679', 'thomas.simon@email.com', 65, TRUE),
(12, 'Perrot', 'Inès', STR_TO_DATE('25/12/1996', '%d/%m/%Y'), 'F', '0723456780', 'ines.perrot@email.com', 54, TRUE),
(13, 'Lefevre', 'Jules', STR_TO_DATE('19/01/1999', '%d/%m/%Y'), 'M', '0734567891', 'jules.lefevre@email.com', 72, FALSE),
(14, 'Cohen', 'Clara', STR_TO_DATE('27/02/1986', '%d/%m/%Y'), 'F', '0745678902', 'clara.cohen@email.com', 61, TRUE),
(15, 'David', 'Gabriel', STR_TO_DATE('30/03/1990', '%d/%m/%Y'), 'M', '0756789013', 'gabriel.david@email.com', 76, TRUE),
(16, 'Joly', 'Sophie', STR_TO_DATE('14/04/1992', '%d/%m/%Y'), 'F', '0767890124', 'sophie.joly@email.com', 59, FALSE),
(17, 'Mathieu', 'Alex', STR_TO_DATE('21/05/1995', '%d/%m/%Y'), 'M', '0778901235', 'alex.mathieu@email.com', 88, TRUE),
(18, 'Fischer', 'Laura', STR_TO_DATE('02/06/1994', '%d/%m/%Y'), 'F', '0789012346', 'laura.fischer@email.com', 66, TRUE),
(19, 'Simon', 'Emma', STR_TO_DATE('07/07/1983', '%d/%m/%Y'), 'F', '0790123457', 'emma.simon@email.com', 63, FALSE),
(20, 'Lemoine', 'Léa', STR_TO_DATE('19/08/1991', '%d/%m/%Y'), 'F', '0701234568', 'lea.lemoine@email.com', 57, TRUE);


INSERT INTO COURS (idCo, nomCo, colllectif, nbPersonne, idMon) VALUES
(1, 'Initiation au poney', TRUE, 10, 1),
(2, 'Saut d’obstacles', TRUE, 8, 2),
(3, 'Dressage avancé', FALSE, 0, 3),
(4, 'Balade en forêt', TRUE, 12, 4),
(5, 'Concours de saut', TRUE, 6, 5),
(6, 'Équitation de loisir', FALSE, 0, 6),
(7, 'Cours particulier', FALSE, 0, 7),
(8, 'Préparation compétition', FALSE, 0, 8),
(9, 'Atelier poney', TRUE, 10, 9),
(10, 'Initiation aux soins', TRUE, 6, 10);

INSERT INTO RESERVER (duree, datee, heure, idCo, idPo, idAdh) VALUES
(1, STR_TO_DATE('01/10/2024', '%d/%m/%Y'), '10:00:00', 1, 1, 1),
(2, STR_TO_DATE('01/10/2024', '%d/%m/%Y'), '14:00:00', 2, 2, 2),
(1, STR_TO_DATE('02/10/2024', '%d/%m/%Y'), '09:00:00', 3, 3, 3),
(2, STR_TO_DATE('02/10/2024', '%d/%m/%Y'), '15:00:00', 4, 4, 4),
(1, STR_TO_DATE('03/10/2024', '%d/%m/%Y'), '11:00:00', 5, 5, 5),
(1, STR_TO_DATE('03/10/2024', '%d/%m/%Y'), '13:00:00', 6, 6, 6),
(2, STR_TO_DATE('04/10/2024', '%d/%m/%Y'), '12:00:00', 7, 7, 7),
(1, STR_TO_DATE('04/10/2024', '%d/%m/%Y'), '14:30:00', 8, 8, 8),
(2, STR_TO_DATE('05/10/2024', '%d/%m/%Y'), '10:00:00', 9, 9, 9),
(1, STR_TO_DATE('05/10/2024', '%d/%m/%Y'), '16:00:00', 10, 10, 10);

INSERT INTO ENCADRER (idCo, idMon) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO TRAVAILLER (idMon, idHoraire) VALUES
(1, 1),
(1, 2),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 1),
(7, 3),
(8, 2),
(9, 4),
(10, 6);


