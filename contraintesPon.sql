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
    
    declare dureeReservation INT;
    declare heureReservation INT;
    declare heure TIME;
    declare duree INT;
    declare mes VARCHAR(1000);

    SELECT heure into heureReservation 
    from RESERVER NATURAL JOIN PONEY 
    WHERE idPo = new.idPo;

    SELECT duree into dureeReservation 
    from RESERVER NATURAL JOIN PONEY 
    WHERE idPo = new.idPo;

    if HOUR(heure) + duree > 2 then
        set mes = concat('Impossible !! Ce poney n est pas assez reposé ! ');
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if ;
end |

delimiter ;

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

DELIMITER |
CREATE OR REPLACE TRIGGER pause_midi BEFORE INSERT ON COURS
FOR EACH ROW
BEGIN 
    IF NOT 8 <= HOUR(new.heureDebutCo) < 12 AND 14 <= HOUR(new.heureDebutCo) < 19 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Un cours doit peut être entre 8h à 12h ou de 14h à 19h ';
    END IF;
END|
DELIMITER ;


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


