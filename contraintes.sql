--Les poneys peuvent porter un cavalier jusqu'à  un certain poids.

delimiter |
create or replace trigger RespectDuPoids before insert on RESERVER for each row 
begin

    declare poidsPers INT;
    declare poidsMaxPoney INT ;
    declare mes VARCHAR(1000);

    SELECT poidsAdh into poidsPers from ADHERENT NATURAL JOIN RESERVER WHERE idAdh = new.idAdh ;
    SELECT poidsMax into poidsMaxPoney from PONEY NATURAL JOIN RESERVER WHERE idPo = new.idPo;

    if poidsPers > poidsMaxPoney then
        set mes = concat('Impossible !! Ce poney ne supportera pas ce poids ! ');
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if ;
end |

delimiter ;

-- Insert into PONEY table
INSERT INTO PONEY (idPo, nomPo, poidsMax, couleurPo, ddnPo) VALUES (1, 'Jeremy', 30, 'noir', '2023-10-01');

INSERT INTO ADHERENT (idAdh, nomAdh, prenomAdh, ddnAdh, sexeAdh, telAdh, mailAdh, poidsAdh, cotisation) 
VALUES (1, 'Dupont', 'Jean', '1990-05-15', 'M', '0123456789', 'jean.dupont@example.com', 45, TRUE);

-- Assurez-vous que la table MONITEUR contient une instance avec idMon = 1
INSERT INTO MONITEUR (idMon, nomMon, prenomMon) VALUES (1, 'Doe', 'John');

-- Insertion dans la table COURS
INSERT INTO COURS (idCo, nomCo, colllectif, nbPersonne, idMon) 
VALUES (1, 'Cours de dressage', TRUE, 10, 1);

-- Insert into RESERVER table
INSERT INTO RESERVER (idAdh, idPo,idCo heure, duree) VALUES (1, 1, 1, '2023-10-01','10:00:00', 2);

DELETE FROM RESERVER WHERE idPo = 1;
DELETE FROM PONEY WHERE idPo = 1;
DELETE FROM ADHERENT WHERE idAdh = 1;


--Les poneys doivent avoir au moins 1 heure de repos après 2 heures de course

--delimiter |
--create or replace trigger ReposMinimum before insert on RESERVER for each row 
--begin
--    
--    declare dureeReservation INT;
--    declare heureReservation INT;
--    declare mes VARCHAR(1000);
--
--    SELECT heure into heureReservation from RESERVER NATURAL JOIN PONEY WHERE idPoney = new.idPoney;
--    SELECT duree into dureeReservation from RESERVER NATURAL JOIN PONEY WHERE idPoney = new.idPoney;
--
--    if heure + duree > 2 then
--        set mes = concat('Impossible !! Ce poney n est pas assez reposé ! ');
--        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
--    end if ;
--end |
--
--delimiter;
--
--
----Vérifie que le certificat médicale est à jour pour être adhérent  
--
--delimiter |
--create or replace trigger CertificatMedicale before insert on ADHERENT for each row 
--begin
--    
--    declare certifMedical BOOL;
--    declare mes VARCHAR(1000);
--
--    SELECT certifMed into certifMedical from ADHERENT WHERE idPoney = new.idPoney;
--    
--    if not certifMedical then
--        set mes = concat('Impossible !! La peresonne n est pas apte à la pratique de l equitation ! ');
--        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
--    end if ;
--end |
--
--delimiter;
--
--
----Un cours peut contenir 10 personnes au maximum
--
--ALTER TABLE COURS ADD CONSTRAINT check_nb_personnes CHECK(nbPersonne <= 10);
--
----Un cours doit durer 1 ou 2 heures. 
--
--ALTER TABLE RESERVER ADD CONSTRAINT check_duree_cours CHECK(duree IN (1,2));
--
--
--
--
--