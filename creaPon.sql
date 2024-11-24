CREATE TABLE HORAIRE(
	idHoraire INT,
    jour VARCHAR(45),
	horaireDebut TIME,
	horaireFin TIME,
	PRIMARY KEY (idHoraire)
);

CREATE TABLE PONEY(
	idPo INT,
	nomPo VARCHAR(45),
	poidsMax FLOAT,
	couleurPo VARCHAR(45),
	ddnPo DATE,
	PRIMARY KEY (idPo)
);

CREATE TABLE MONITEUR(
	idMon INT,
	nomMon VARCHAR(45),
	prenomMon VARCHAR(45),
	ddnMon DATE,
	sexeMon CHAR(1),
	telMon VARCHAR(45),
	mailMon VARCHAR(45) UNIQUE,
	motsDePasseMon VARCHAR(45),
	poidsMon FLOAT,
	certification VARCHAR(45),
	contrat VARCHAR(45),
	PRIMARY KEY (idMon)
);

CREATE TABLE ADHERENT(
	idAdh INT,
	nomAdh VARCHAR(45),
	prenomAdh VARCHAR(45),
	ddnAdh DATE,
	sexeAdh CHAR(1) ,
	telAdh VARCHAR(45),
	mailAdh VARCHAR(45) UNIQUE,
	motsDePasseAdh VARCHAR(45),
	poidsAdh FLOAT,
	cotisation BOOLEAN,
	PRIMARY KEY (idAdh)
);

CREATE TABLE ADMINISTRATEUR(
	idAdm INT,
	nomAdm VARCHAR(45),
	prenomAdm VARCHAR(45),
	ddnAdm VARCHAR(45),
	sexeAdm CHAR(1),
	telAdm VARCHAR(45),
	mailAdm VARCHAR(45) UNIQUE,
	motsDePasseAdm VARCHAR(45)
);

CREATE TABLE COURS(
	idCo INT,
	nomCo VARCHAR(42),
	collectif BOOLEAN,
	nbPersonne INT ,
	idMon INT,
	PRIMARY KEY (idCo),
	FOREIGN KEY (idMon) REFERENCES MONITEUR(idMon)
);

CREATE TABLE RESERVER(
    duree INT,
	date DATE,
	heure TIME,
	idCo INT,
	idPo INT,
	idAdh INT,
	PRIMARY KEY (date, heure, idCo, idPo, idAdh),
	FOREIGN KEY (idCo) REFERENCES COURS(idCo),
	FOREIGN KEY (idPo) REFERENCES PONEY(idPo),
	FOREIGN KEY (idAdh) REFERENCES ADHERENT(idAdh)
);

CREATE TABLE TRAVAILLER(
	idMon INT,
	idHoraire INT,
	PRIMARY KEY (idMon, idHoraire),
	FOREIGN KEY (idMon) REFERENCES MONITEUR(idMon),
	FOREIGN KEY (idHoraire) REFERENCES HORAIRE(idHoraire)
);

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

--Les poneys doivent avoir au moins 1 heure de repos après 2 heures de course

delimiter |
create or replace trigger ReposMinimum before insert on RESERVER for each row 
begin
    declare heureDerniereReservation TIME;
    declare dureeDerniereReservation INT;
    declare lastReservation INT;
    declare mes VARCHAR(1000);

    select count(*) into lastReservation 
    from RESERVER where idPo = NEW.idPo ;

    if lastReservation > 0 then
        SELECT heure, duree into heureDerniereReservation, dureeDerniereReservation 
        from RESERVER 
        WHERE idPo = NEW.idPo
        ORDER BY heure DESC
        LIMIT 1;
    end if;

    if ADDTIME(heureDerniereReservation, SEC_TO_TIME(dureeDerniereReservation * 3600 + 3600)) > NEW.heure then
        set mes = 'Impossible !! Ce poney n est pas assez reposé !';
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if;
end |
delimiter ;

-- L'email doit contenir un @ et un . et doit faire au moins 10 caractères
delimiter |
create or replace trigger check_email_format_adh BEFORE INSERT ON ADHERENT FOR EACH ROW
BEGIN
    declare mes VARCHAR(1000);
    IF NOT (NEW.mailAdh LIKE '%@%' AND NEW.mailAdh LIKE '%.%' AND CHAR_LENGTH(NEW.mailAdh) >= 10) THEN
        SET mes = concat('Une adresse email doit avoir un @, un . et doit faire au moins 10 caractères');
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    END IF;
END |

delimiter ;

-- L'email doit contenir un @ et un . et doit faire au moins 10 caractères
delimiter |
create or replace trigger check_email_format_Mon BEFORE INSERT ON MONITEUR FOR EACH ROW
BEGIN
    declare mes VARCHAR(1000);
    IF NOT (NEW.mailMon LIKE '%@%' AND NEW.mailMon LIKE '%.%' AND CHAR_LENGTH(NEW.mailMon) >= 10) THEN
        SET mes = concat('Une adresse email doit avoir un @, un . et doit faire au moins 10 caractères');
        SIGNAL SQLSTATE '45000' set MESSAGE_TEXT = mes ;
        
    END IF;
END |

delimiter ;

-- L'email doit contenir un @ et un . et doit faire au moins 10 caractères
delimiter |
CREATE OR REPLACE TRIGGER check_email_format_Adm BEFORE INSERT ON ADMINISTRATEUR FOR EACH ROW
BEGIN
    declare mes VARCHAR(1000);
    IF NOT (NEW.mailAdm LIKE '%@%' AND NEW.mailAdm LIKE '%.%' AND CHAR_LENGTH(NEW.mailAdm) >= 10) THEN
        SET mes = concat('Une adresse email doit avoir un @, un . et doit faire au moins 10 caractères');
        SIGNAL SQLSTATE '45000' set MESSAGE_TEXT = mes ;
        
    END IF;
END |

delimiter ;

-- Un numéro de téléphone doit avoir 10 chiffres
DELIMITER |

CREATE OR REPLACE TRIGGER check_num_Adm BEFORE INSERT ON ADMINISTRATEUR
FOR EACH ROW
BEGIN
    IF NOT (CHAR_LENGTH(NEW.telAdm) = 10 AND NEW.telAdm REGEXP '^[0-9]{10}$') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Un numéro de téléphone doit avoir 10 chiffres';
    END IF;
END |

DELIMITER ; 

-- Un numéro de téléphone doit avoir 10 chiffres
DELIMITER |

CREATE OR REPLACE TRIGGER check_num_Adh BEFORE INSERT ON ADHERENT
FOR EACH ROW
BEGIN
    IF NOT (CHAR_LENGTH(NEW.telAdh) = 10 AND NEW.telAdh REGEXP '^[0-9]{10}$') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Un numéro de téléphone doit avoir 10 chiffres';
    END IF;
END |
DELIMITER ;

-- Un numéro de téléphone doit avoir 10 chiffres
DELIMITER |
CREATE OR REPLACE TRIGGER check_num_Mon BEFORE INSERT ON MONITEUR
FOR EACH ROW
BEGIN
    IF NOT (CHAR_LENGTH(NEW.telMon) = 10 AND NEW.telMon REGEXP '^[0-9]{10}$') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Un numéro de téléphone doit avoir 10 chiffres';
    END IF;
END|
DELIMITER ;

-- Un réservation doit être entre 8h à 12h ou de 14h à 19h
DELIMITER |
CREATE OR REPLACE TRIGGER pause_midi BEFORE INSERT ON RESERVER
FOR EACH ROW
BEGIN 
    IF NOT ((HOUR(new.heure) >= 8 AND HOUR(new.heure) < 12) OR (HOUR(new.heure) >= 14 AND HOUR(new.heure) < 19)) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Une Réservation doit être entre 8h à 12h ou de 14h à 19h ';
    END IF;
END|
DELIMITER ;


--Les adhérents doivent avoir au moins 15 ans

delimiter |
create or replace trigger AgeMinimumAdh before insert on ADHERENT for each row
begin
    declare age INT;
    declare msg VARCHAR(1000);

    SET age = YEAR(NOW()) - YEAR(new.ddnAdh);

    if age < 15 then
        set msg = concat("Impossible de s'inscrire ! L'age requis est de minimum 15 ans.");
        signal SQLSTATE '45000' set MESSAGE_TEXT = msg;
    end if;
end |
delimiter ;


--Les poneys doivent être agé de 5 ans minimum pour pouvoir être chevauché

delimiter |
create or replace trigger AgeMinimumPo before insert on RESERVER for each row
begin
    declare age INT;
    declare ddn DATE;
    declare msg VARCHAR(1000);

    SELECT ddnPo INTO ddn FROM PONEY WHERE PONEY.idPo = NEW.idPo;

    SET age = TIMESTAMPDIFF(YEAR, ddn, CURDATE());

    if age < 5 then
        set msg = concat("Impossible de réserver ce poney ! L'age requis est de minimum 5 ans pour qu'un poney soit chevauché.");
        signal SQLSTATE '45000' set MESSAGE_TEXT = msg;
    end if;
end |
delimiter ;

-- Un adhérent ne peut réserver qu’un seul cours à la fois pour une même heure.
-- Un moniteur ne peut encadrer qu’un seul cours à la fois.
-- Un poney ne peut être associé à plus d’un cours simultanément.

delimiter | 
create or replace trigger check_reservation before insert on RESERVER for each row
begin 
    declare dejaReserverAdh INT;
    declare dejaReserverMon INT;
    declare dejaReserverPo INT; 
    declare msg VARCHAR(1000);
    
    SELECT COUNT(*) into dejaReserverAdh FROM RESERVER 
    WHERE heure = new.heure AND idAdh = new.idAdh;

    SELECT COUNT(*) into dejaReserverMon FROM COURS
    JOIN RESERVER ON COURS.idCo = RESERVER.idCo
    WHERE COURS.idMon = (SELECT idMon FROM COURS WHERE idCo = new.idCo) AND RESERVER.heure = new.heure;

    SELECT COUNT(*) into dejaReserverPo FROM RESERVER 
    WHERE heure = new.heure AND idPo = new.idPo;

    IF dejaReserverAdh > 0 THEN
        set msg = concat("Impossible, un adhérent ne peut réserver qu’un seul cours à la fois pour une même heure.");
        signal SQLSTATE '45000' set MESSAGE_TEXT = msg;
    END IF;

    IF dejaReserverMon > 0 THEN
        set msg = concat("Impossible, un moniteur ne peut encadrer qu’un seul cours à la fois.");
        signal SQLSTATE '45000' set MESSAGE_TEXT = msg;
    END IF;

    IF dejaReserverPo > 0 THEN
        set msg = concat("Impossible, un poney ne peut être associé à plus d’un cours simultanément.");
        signal SQLSTATE '45000' set MESSAGE_TEXT = msg;
    END IF;
END |
delimiter ;

----Un cours peut contenir 10 personnes au maximum
ALTER TABLE COURS ADD CONSTRAINT check_nb_personnes CHECK(nbPersonne <= 10);

--Un cours doit durer 1 ou 2 heures. 
ALTER TABLE RESERVER ADD CONSTRAINT check_duree_cours CHECK(duree IN (1,2));

--Vérifie que le sexe est bien soit 'F' pour Féminin ou 'M' pour Masculin
ALTER TABLE ADHERENT ADD CONSTRAINT sexeAdh CHECK (sexeAdh IN ('F','M'));

--Vérifie que le sexe est bien soit 'F' pour Féminin ou 'M' pour Masculin
ALTER TABLE MONITEUR ADD CONSTRAINT sexeMon CHECK (sexeMon IN ('F','M'));

--Vérifie que le sexe est bien soit 'F' pour Féminin ou 'M' pour Masculin
ALTER TABLE ADMINISTRATEUR ADD CONSTRAINT sexeAdm CHECK (sexeAdm IN ('F','M'));

-- Insertion pour tester le trigger RespectDuPoids

INSERT INTO MONITEUR (idMon, nomMon, prenomMon, ddnMon, sexeMon, telMon, mailMon, motsDePasseMon, poidsMon, certification, contrat)
VALUES (1, 'Instructor', 'Mike', '1980-01-01', 'M', '0123456789', 'mike.instructor@example.com', 'moDePasse', 70, 'Cert1', 'Full-time');

INSERT INTO ADHERENT (idAdh, nomAdh, prenomAdh, ddnAdh, sexeAdh, telAdh, mailAdh, motsDePasseAdh, poidsAdh, cotisation)
VALUES (1, 'Doe', 'John', '2000-01-01', 'M', '0123456789', 'john.doe@example.com', 'password', 80, TRUE);

INSERT INTO PONEY (idPo, nomPo, poidsMax, couleurPo, ddnPo)
VALUES (1, 'Poney1', 70, 'Brown', '2015-01-01');

INSERT INTO COURS(idCo, nomCo, collectif, nbPersonne, idMon)
VALUES (1, 'Cours1', TRUE, 5, 1);

INSERT INTO RESERVER (duree, date, heure, idCo, idPo, idAdh)
VALUES (2, '2023-10-01', '10:00:00', 1, 1, 1);

-- Insertion pour tester le trigger ReposMinimum

INSERT INTO COURS(idCo, nomCo, collectif, nbPersonne, idMon)
VALUES (2, 'Cours2', TRUE, 5, 1);

INSERT INTO ADHERENT (idAdh, nomAdh, prenomAdh, ddnAdh, sexeAdh, telAdh, mailAdh, motsDePasseAdh, poidsAdh, cotisation)
VALUES (2, 'Smith', 'Jane', '2000-01-01', 'F', '0123456789','sqgfq@grzg.com', 'password', 60, TRUE);

INSERT INTO RESERVER (duree, date, heure, idCo, idPo, idAdh)
VALUES (2, '2023-10-01', '11:00:00', 2, 1, 2);

-- Insertion pour tester le trigger check_email_format_adh
INSERT INTO ADHERENT (idAdh, nomAdh, prenomAdh, ddnAdh, sexeAdh, telAdh, mailAdh, motsDePasseAdh, poidsAdh, cotisation)
VALUES (2, 'Smith', 'Jane', '2000-01-01', 'F', '0123456789', 'jane.smith', 'password', 60, TRUE);

-- Insertion pour tester le trigger check_num_Adh
INSERT INTO ADHERENT (idAdh, nomAdh, prenomAdh, ddnAdh, sexeAdh, telAdh, mailAdh, motsDePasseAdh, poidsAdh, cotisation)
VALUES (3, 'Brown', 'Alice', '2000-01-01', 'F', '01234', 'alice.brown@example.com', 'password', 55, TRUE);

-- Insertion pour tester le trigger AgeMinimumAdh
INSERT INTO ADHERENT (idAdh, nomAdh, prenomAdh, ddnAdh, sexeAdh, telAdh, mailAdh, motsDePasseAdh, poidsAdh, cotisation)
VALUES (4, 'Young', 'Tom', '2010-01-01', 'M', '0123456789', 'tom.young@example.com', 'password', 50, TRUE);

-- Insertion pour tester le trigger AgeMinimumPo
INSERT INTO PONEY (idPo, nomPo, poidsMax, couleurPo, ddnPo)
VALUES (2, 'Poney2', 70, 'White', '2020-01-01');

INSERT INTO RESERVER (duree, date, heure, idCo, idPo, idAdh)
VALUES (3, '2023-10-01', '14:00:00', 1, 2, 1);

-- Insertion pour tester le trigger check_reservation

--reservation 1

INSERT INTO PONEY (idPo, nomPo, poidsMax, couleurPo, ddnPo)
VALUES (3, 'Poney3', 70, 'Black', '2015-01-01');

INSERT INTO MONITEUR (idMon, nomMon, prenomMon, ddnMon, sexeMon, telMon, mailMon, motsDePasseMon, poidsMon, certification, contrat)
VALUES (2, 'Instructor', 'Mike', '1980-01-01', 'M', '0123456789', 'mike.instruor@example.com', 'password', 65, 'Cert1', 'Full-time');

INSERT INTO COURS (idCo, nomCo, collectif, nbPersonne, idMon)
VALUES (3, 'Cours1', TRUE, 5, 2);

INSERT INTO RESERVER (duree, date, heure, idCo, idPo, idAdh)
VALUES (4, '2023-10-01', '10:00:00', 3, 3, 1);

--reservation 2
INSERT INTO COURS (idCo, nomCo, collectif, nbPersonne, idMon)
VALUES (4, 'Cours2', TRUE, 5, 1);

INSERT INTO RESERVER (duree, date, heure, idCo, idPo, idAdh)
VALUES (2, '2023-10-01', '11:00:00', 4, 3, 1);