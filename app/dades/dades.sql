USE rubriDB;


DROP TABLE IF EXISTS Nivell;

DROP TABLE IF EXISTS Avalua;

DROP TABLE IF EXISTS Grau;

DROP TABLE IF EXISTS Criteri;

DROP TABLE IF EXISTS Rubrica;

DROP TABLE IF EXISTS Alumne;

DROP TABLE IF EXISTS UF;

CREATE TABLE UF (
    numero DECIMAL(1) NOT NULL,
    nom VARCHAR(20) NOT NULL,
    PRIMARY KEY (numero)
);

CREATE TABLE Alumne (
    cognoms VARCHAR(40) NOT NULL,
    nom VARCHAR(40) NOT NULL,
    PRIMARY KEY (cognoms, nom)
);

CREATE TABLE Rubrica (
    nom VARCHAR(20) NOT NULL,
    descripcio VARCHAR(100),
    PRIMARY KEY (nom)
);


CREATE TABLE Criteri (
    nom VARCHAR(20) NOT NULL,
    nom_rubrica VARCHAR(20) NOT NULL,
    numero_uf DECIMAL(1),
    descripcio VARCHAR(100),
    pes DECIMAL(3) NOT NULL,
    PRIMARY KEY (nom, nom_rubrica),
    FOREIGN KEY (numero_uf) REFERENCES UF(numero),
    FOREIGN KEY (nom_rubrica) REFERENCES Rubrica(nom)
);

CREATE TABLE Grau (
    nom VARCHAR(20) NOT NULL,
    nom_criteri VARCHAR(20) NOT NULL,
    nom_rubrica VARCHAR(20) NOT NULL,
    descripcio VARCHAR(100),
    qualificacio DECIMAL(4,2) NOT NULL,
    PRIMARY KEY (nom, nom_criteri, nom_rubrica),
    FOREIGN KEY (nom_criteri, nom_rubrica) REFERENCES Criteri(nom, nom_rubrica)
        ON UPDATE CASCADE
);

CREATE TABLE Avalua (
    cognoms_alumne VARCHAR(40) NOT NULL,
    nom_alumne VARCHAR(40) NOT NULL,
    nom_rubrica VARCHAR(20) NOT NULL,
    PRIMARY KEY (cognoms_alumne, nom_alumne, nom_rubrica),
    FOREIGN KEY (cognoms_alumne, nom_alumne) REFERENCES Alumne(cognoms, nom)
        ON UPDATE CASCADE,
    FOREIGN KEY (nom_rubrica) REFERENCES Rubrica(nom)
        ON UPDATE CASCADE
);

CREATE TABLE Nivell (
    cognoms_alumne VARCHAR(40) NOT NULL,
    nom_alumne VARCHAR(40) NOT NULL,
    nom_grau VARCHAR(20) NOT NULL,
    nom_criteri VARCHAR(20) NOT NULL,
    nom_rubrica VARCHAR(20) NOT NULL,
    comentari VARCHAR(50),
    PRIMARY KEY (cognoms_alumne, nom_alumne, nom_grau, nom_criteri, nom_rubrica),
    FOREIGN KEY (cognoms_alumne, nom_alumne) REFERENCES Alumne(cognoms, nom)
        ON UPDATE CASCADE,
    FOREIGN KEY (nom_grau, nom_criteri, nom_rubrica) REFERENCES Grau(nom, nom_criteri, nom_rubrica)
        ON UPDATE CASCADE
);


INSERT INTO UF (numero, nom)
VALUES (1, "primera uf"),
       (2, "segona uf");
       
INSERT INTO Alumne (cognoms, nom)
VALUES ("Rodríguez Bellido", "Joan"),
       ("Camps", "Maria"),
       ("Puertas", "Albert");

INSERT INTO Rubrica (nom, descripcio)
VALUES
       ("Sistemes", "Rúbrica completa del mòdul de sistemes"),
       ("Xarxes", "Rúbrica completa del mòdul de xarxes");

INSERT INTO Criteri (nom, nom_rubrica, numero_uf, descripcio, pes)
VALUES
       ("Windows", "Sistemes", 1, "Instal·lació, configuració i verificació d'un sistema Windows", 10),
       ("Linux", "Sistemes", 1, "Instal·lació, configuració i verificació d'un sistema Linux", 20);

INSERT INTO Grau (nom, nom_criteri, nom_rubrica, descripcio, qualificacio)
VALUES
       ("Espectacular", "Windows", "Sistemes", "Instal·la Windows de forma espectacular", 10),
       ("Casi perfecte", "Windows", "Sistemes", "Instal·la Windows, però es deixa alguna cosa", 7.5),
       ("Funciona", "Windows", "Sistemes", "Instal·la Windows i funciona", 5),
       ("No funciona", "Windows", "Sistemes", "No aconsegueix instal·lar Windows, però casi", 2.5),
       ("Res", "Windows", "Sistemes", "No és capaç de fer res", 0);

INSERT INTO Avalua (cognoms_alumne, nom_alumne, nom_rubrica)
VALUES
       ("Rodríguez Bellido", "Joan", "Sistemes"),
       ("Camps", "Maria", "Sistemes"),
       ("Puertas", "Albert", "Sistemes"),
       ("Camps", "Maria", "Xarxes"),
       ("Puertas", "Albert", "Xarxes");

INSERT INTO Nivell (cognoms_alumne, nom_alumne, nom_grau, nom_criteri, nom_rubrica, comentari)
VALUES
       ("Rodríguez Bellido", "Joan", "Espectacular", "Windows", "Sistemes", "Aquest nano és un crack"),
       ("Puertas", "Albert", "No funciona", "Windows", "Sistemes", "Ho intenta, però no se'n surt");


