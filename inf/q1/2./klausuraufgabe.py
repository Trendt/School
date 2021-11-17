import sqlite3 as sql
import datetime
from random import randrange, randint, random

file = "Klausuraufgabe.db"
conn = sql.connect(file)

agentur_str = """
    CREATE TABLE IF NOT EXISTS Agentur(
        Name VARCHAR(255) PRIMARY KEY,
        Ort VARCHAR(255)
    );
"""

model_str = """
    CREATE TABLE IF NOT EXISTS Model(
        MID INTEGER PRIMARY KEY,
        Name VARCHAR(255),
        Vorname Varchar(255),
        Geschlecht VARCHAR(255),
        Größe REAL,
        Agentur VARCHAR(255),
        FOREIGN KEY(Agentur) REFERENCES Agentur(Name)
    );
"""

hersteller_str = """
    CREATE TABLE IF NOT EXISTS Hersteller(
        ID INTEGER PRIMARY KEY,
        Name VARCHAR(255)
    );
"""

produkt_str = """
    CREATE TABLE IF NOT EXISTS Produkt(
        Bezeichnung VARCHAR(255) PRIMARY KEY,
        HerstellerID INTEGER,
        FOREIGN KEY(HerstellerID) REFERENCES Hersteller(ID),
    );
"""

fotograf_str = """
    CREATE TABLE IF NOT EXISTS Fotograf(
        ID INTEGER PRIMARY KEY,
        Name VARCHAR(255)
    );
"""

shooting_str = """
    CREATE TABLE IF NOT EXISTS Shooting(
        Termin DATE NOT NULL,
        Ort VARCHAR(255) NOT NULL,
        FotografID INTEGER NOT NULL,
        Produkt Varchar(255) NOT NULL,
        FOREIGN KEY(FotografID) REFERENCES Fotograf(ID),
        FOREIGN KEY(Produkt) REFERENCES Produkt(Bezeichnung),
        PRIMARY KEY(Termin, Ort)
    );
"""

shooting_model_str = """
    CREATE TABLE IF NOT EXISTS ShootingModel(
        MID INTEGER NOT NULL,
        ShootingTermin DATE NOT NULL,
        ShootingOrt VARCHAR(255) NOT NULL,
        Honorar Real,
        FOREIGN KEY(MID) REFERNCES Model(MID),
        FOREIGN KEY(ShootingTermin) REFERENCES Shooting(Termin),
        FOREIGN KEY(ShootingOrt) REFERENCES Shooting(Ort)
"""

number_data = 5
Agenturen = [("Agentur1", "Berlin"), ("Agentur2", "Berlin"), ("Agentur3", "Bonn"), ("Agentur3", "Bremen"),("Agentur4", "Bochum"), ("Agentur5", "Bielefeld")]
Models = [(x, f"Name{x}", f"Vorname{x}", "weiblich", randrange(140, 190) + random(), f"Agentur{randint(1,5)}") for x in range(number_data)]
Hersteller = [(x, f"Hersteller{x}") for x in range(number_data)]
Produkte = [(f"Produkt{x}", randint(1, number_data)) for x in range(number_data)]
Fotografen = [(x, f"Fotograf{x}") for x in range(number_data)]
Shootings = [(x, datetime.datetime.now(), "Berlin", randint(1000, 100000)) for x in range(number_data)]
# shootingModel


print("\n".join(map(str, Agenturen)))
print("\n".join(map(str, Models)))
print("\n".join(map(str, Hersteller)))
print("\n".join(map(str, Produkte)))
print("\n".join(map(str, Fotografen)))

def query(query:str) -> tuple:
    pass
