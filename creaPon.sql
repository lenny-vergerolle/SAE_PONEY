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
	heureDebutCo TIME,
	dureeCo INT,
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
