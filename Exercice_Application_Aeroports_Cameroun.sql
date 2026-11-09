BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS Aeroports (
    id_aeroport INTEGER PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    ville VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS Passagers (
    id_passager INTEGER PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    id_vol INTEGER NOT NULL,
    FOREIGN KEY (id_vol) REFERENCES Vols(id_vol)
);
CREATE TABLE IF NOT EXISTS Vols (
    id_vol INTEGER PRIMARY KEY,
    numero_vol VARCHAR(10) NOT NULL UNIQUE,
    id_depart INTEGER NOT NULL,
    id_arrivee INTEGER NOT NULL,
    date_vol DATE NOT NULL,
    statut VARCHAR(20) NOT NULL
        CHECK (statut IN ('Programme', 'Retarde', 'Annule')),
    FOREIGN KEY (id_depart) REFERENCES Aeroports(id_aeroport),
    FOREIGN KEY (id_arrivee) REFERENCES Aeroports(id_aeroport),
    CHECK (id_depart <> id_arrivee)
);
INSERT INTO "Aeroports" ("id_aeroport","nom","ville") VALUES (1,'Aéroport de Douala','Douala'),
 (2,'Aéroport de Yaoundé-Nsimalen','Yaoundé'),
 (3,'Aéroport de Garoua','Garoua'),
 (4,'Aéroport de Maroua-Salak','Maroua'),
 (5,'Aéroport de Bafoussam','Bafoussam');
INSERT INTO "Passagers" ("id_passager","nom","prenom","email","id_vol") VALUES (1,'Njoya','Amina','amina@example.com',1),
 (2,'Fonkou','Paul','paul@example.com',1),
 (3,'Abena','Carine','carine@example.com',2),
 (4,'Oumarou','Ibrahim','ibrahim@example.com',2),
 (5,'Manga','Rose','rose@example.com',3),
 (6,'Tchoumi','Eric','eric@example.com',4),
 (7,'Bello','Mariam','mariam@example.com',4),
 (8,'Etoa','Daniel','daniel@example.com',6);
INSERT INTO "Vols" ("id_vol","numero_vol","id_depart","id_arrivee","date_vol","statut") VALUES (1,'CM101',1,2,'2026-11-15','Programme'),
 (2,'CM102',2,3,'2026-11-15','Retarde'),
 (3,'CM103',3,1,'2026-11-16','Programme'),
 (4,'CM104',1,4,'2026-11-16','Programme'),
 (5,'CM105',4,2,'2026-11-17','Programme'),
 (6,'CM106',2,1,'2026-11-17','Annule');
COMMIT;
