import sqlite3

conn = sqlite3.Connection("wellnesshotel.db")

masseur_sql = """
    CREATE TABLE IF NOT EXISTS Masseur(
        MasseurID INTEGER PRIMARY KEY,
        Vorname VARCHAR(255),
        Name VARCHAR(255)
    );
"""

gast_sql = """
    CREATE TABLE IF NOT EXISTS Gast(
        GastID INTEGER PRIMARY KEY,
        Vorname VARCHAR(255),
       Name VARCHAR(255),
        Geschlecht VARCHAR(255),
        LieblingsMasseur INTEGER,
        Geburtsjahr INTEGER,
        Adresse VARCHAR(255),
        FOREIGN KEY(LieblingsMasseur) REFERENCES Masseur(MasseurID)
    );
"""

mittel_sql = """
    CREATE TABLE IF NOT EXISTS Mittel(
        MittelID INTEGER PRIMARY KEY,
        Bezeichnung VARCHAR(255)
    );
"""

mittel_gast = """
    CREATE TABLE IF NOT EXISTS MittelGast(
        MittelID INTEGER,
        GastID INTEGER,
        FOREIGN KEY(MittelID) REFERENCES Mittel(MittelID),
        FOREIGN KEY(GastID) REFERENCES Gast(GastID)
    );
"""
dbs = [masseur_sql, gast_sql, mittel_sql, mittel_gast]
[conn.execute(s) for s in dbs]
conn.commit()
