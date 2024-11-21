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
    declare mes VARCHAR(1000);

    SELECT heure into heureReservation from RESERVER NATURAL JOIN PONEY WHERE idPo = new.idPo;
    SELECT duree into dureeReservation from RESERVER NATURAL JOIN PONEY WHERE idPo = new.idPo;

    if heureReservation + dureeReservation > 2 then
        set mes = concat('Impossible !! Ce poney n est pas assez reposé ! ');
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if;
end |

delimiter ;

--Les adhérents doivent avoir au moins 15 ans

delimiter |
create or replace trigger AgeMinimumAdh before insert on ADHERENT for each row
begin
    declare age INT;
    declare msg VARCHAR(1000);

    SELECT (YEAR(NOW()) - YEAR(ddnAdh)) INTO age FROM ADHERENT;

    if age < 15 then
        set msg = concat("Impossible de s'inscrire ! L'age requis est de minimum 15 ans.");
        signal SQLSTATE '45000' set MESSAGE_TEXT = msg;
    end if;
end |
delimiter ;
    
INSERT INTO ADHERENT (idAdh, nomAdh, prenomAdh, ddnAdh, sexeAdh, telAdh, mailAdh, motsDePasseAdh, poidsAdh, cotisation) VALUES 
(1111, 'Newton', 'Sabrina', STR_TO_DATE('06/12/2022', '%d/%m/%Y'), 'F', '0695249101', 'sabrina.newton@mail.com', '1234', 65.2, TRUE);


--Les poneys doivent être agé de 5 ans minimum pour pouvoir être chevauché

delimiter |
create or replace trigger AgeMinimumPo before insert on RESERVER for each row
begin
    declare age INT;
    declare msg VARCHAR(1000);

    SELECT (YEAR(NOW()) - YEAR(ddnPo)) INTO age FROM PONEY;

    if age < 5 then
        set msg = concat("Impossible de réserver ce poney ! L'age requis est de minimum 5 ans pour qu'un poney soit chevauché.");
        signal SQLSTATE '45000' set MESSAGE_TEXT = msg;
    end if;
end |
delimiter ;


----Un cours peut contenir 10 personnes au maximum
ALTER TABLE COURS ADD CONSTRAINT check_nb_personnes CHECK(nbPersonne <= 10);

--Un cours doit durer 1 ou 2 heures. 
ALTER TABLE RESERVER ADD CONSTRAINT check_duree_cours CHECK(duree IN (1,2));

--Un numéro de téléphone doit avoir 10 chiffres
ALTER TABLE ADHERENT ADD CONSTRAINT check_num_tel CHECK(telAdh ~ '^\d{10}$')

--Une adresse email doit avoir un @, un '.' et doit faire au moins 10 caractères
ALTER TABLE ADHERENT ADD CONSTRAINT check_email_format CHECK (mailAdh ~ '^.{10,}$' AND mailAdh LIKE '%@%' AND mailAdh LIKE '%.%');
