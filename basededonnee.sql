DROP TABLE ENCADRER;
DROP TABLE TRAVAILLER;
DROP TABLE RESERVER;
DROP TABLE PONEY;
DROP TABLE COURS;
DROP TABLE ADHERENT;
DROP TABLE MONITEUR;
DROP TABLE HORAIRE; 

CREATE TABLE HORAIRE(
    idHoraire INT,
    horaireDebut TIME,
    horaireFin TIME,
    PRIMARY KEY (idHoraire)
);

CREATE TABLE PONEY(
    idPo INT,
    nomPo VARCHAR(45),
    poidsMax INT,
    couleurPo VARCHAR(45),
    ddnPo DATE,
    PRIMARY KEY (idPo)
);

CREATE TABLE MONITEUR(
    idMon INT,
    nomMon VARCHAR(45),
    prenomMon VARCHAR(45),
    ddnMon DATE,
    sexeMon CHAR(1) CHECK (sexeMon IN ('F','M')),
    telMon VARCHAR(45),
    mailMon VARCHAR(45),
    poidsMon INT,
    certification VARCHAR(45),
    contrat VARCHAR(45),
    PRIMARY KEY (idMon)
);

CREATE TABLE ADHERENT(
    idAdh INT,
    nomAdh VARCHAR(45),
    prenomAdh VARCHAR(45),
    ddnAdh DATE,
    sexeAdh VARCHAR(45),
    telAdh VARCHAR(45),
    mailAdh VARCHAR(45),
    poidsAdh INT,
    cotisation BOOLEAN,
    PRIMARY KEY (idAdh)
);

CREATE TABLE COURS(
    idCo INT,
    nomCo VARCHAR(42),
    colllectif BOOLEAN,
    nbPersonne INT CHECK (nbPersonne <= 10),
    idMon INT,
    PRIMARY KEY (idCo),
    FOREIGN KEY (idMon) REFERENCES MONITEUR(idMon)
);

CREATE TABLE RESERVER(
    duree INT,
    datee DATE,
    heure INT,
    idCo INT,
    idPo INT,
    idAdh INT,
    PRIMARY KEY (datee, heure, idCo, idPo, idAdh),
    FOREIGN KEY (idCo) REFERENCES COURS(idCo),
    FOREIGN KEY (idPo) REFERENCES PONEY(idPo),
    FOREIGN KEY (idAdh) REFERENCES ADHERENT(idAdh)
);

CREATE TABLE ENCADRER(
    idCo INT,
    idMon INT,
    PRIMARY KEY (idCo, idMon),
    FOREIGN KEY (idCo) REFERENCES COURS(idCo),
    FOREIGN KEY (idMon) REFERENCES MONITEUR(idMon)
);

CREATE TABLE TRAVAILLER(
    idMon INT,
    idHoraire INT,
    PRIMARY KEY (idMon, idHoraire),
    FOREIGN KEY (idMon) REFERENCES MONITEUR(idMon),
    FOREIGN KEY (idHoraire) REFERENCES HORAIRE(idHoraire)
)