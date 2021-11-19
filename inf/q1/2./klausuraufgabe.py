import sqlite3 as sql
import datetime
from random import randrange, randint, random
from sys import argv

number_data = int(argv[1])
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
        Groesse REAL,
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
        FOREIGN KEY(HerstellerID) REFERENCES Hersteller(ID) 
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
        ID INTEGER PRIMARY KEY,
        Termin DATE NOT NULL,
        Ort VARCHAR(255) NOT NULL,
        FotografID INTEGER NOT NULL,
        Produkt Varchar(255) NOT NULL,
        FOREIGN KEY(FotografID) REFERENCES Fotograf(ID),
        FOREIGN KEY(Produkt) REFERENCES Produkt(Bezeichnung)
    );
"""

shooting_model_str = """
    CREATE TABLE IF NOT EXISTS ShootingModel(
        MID INTEGER NOT NULL,
        ShootingID INTEGER NOT NULL,
        Honorar Real,
        FOREIGN KEY(MID) REFERENCES Model(MID),
        FOREIGN KEY(ShootingID) REFERENCES Shooting(ID)
    );
"""

def query(query_str:str) -> tuple:
    cursor = conn.cursor()
    cursor.execute(query_str)
    data = cursor.fetchall()
    cursor.close()
    if data:
        return data

date = datetime.datetime.now()
Agenturen = [(f"Agentur{x}", "Berlin") for x in range(number_data)]
Models = [(f"Name{x}", f"Vorname{x}", "weiblich", randrange(140, 190) + random(), f"Agentur{randint(1,number_data-1)}") for x in range(number_data)]
Hersteller = [(f"Hersteller{x}",) for x in range(number_data)]
Produkte = [(f"Produkt{x}", randint(1, number_data)) for x in range(number_data)]
Fotografen = [(x, f"Fotograf{x}") for x in range(number_data)]
Shootings = [(date+datetime.timedelta(days=x), "Berlin", randint(1, number_data-1), f"Produkt{x}") for x in range(number_data)]
shootingModel = [(x, date+datetime.timedelta(days=x), "Berlin", randrange(100,100000)) for x in range(number_data)]

query(agentur_str)
query(model_str)
query(hersteller_str)
query(produkt_str)
query(fotograf_str)
query(shooting_str)
query(shooting_model_str)

cursor = conn.cursor()
cursor.executemany("INSERT INTO Agentur VALUES(?,?)", Agenturen)
cursor.executemany("INSERT INTO Model(Name, Vorname, Geschlecht, Groesse, Agentur) VALUES(?,?,?,?,?)", Models)
cursor.executemany("INSERT INTO Hersteller(Name) VALUES(?)", Hersteller)
cursor.executemany("INSERT INTO Produkt(Bezeichnung, HerstellerID) VALUES(?,?)", Produkte)
cursor.executemany("INSERT INTO Fotograf(ID, Name) VALUES(?,?)", Fotografen)
cursor.executemany("INSERT INTO Shooting(Termin,Ort,FotografID,Produkt) VALUES(?,?,?,?)", Shootings)
cursor.executemany("INSERT INTO ShootingModel(MID, ShootingTermin, ShootingOrt, Honorar) VALUES(?,?,?,?)", shootingModel)
cursor.close()


print("\n".join(map(str, Agenturen)))
print("\n".join(map(str, Models)))
print("\n".join(map(str, Hersteller)))
print("\n".join(map(str, Produkte)))
print("\n".join(map(str, Fotografen)))

print("Selektion (SELECT * FROM Agentur:", query("Select * From Agentur"))
print("Projektion (SELECT * FROM Model WHERE MID == 1:", query("Select * From Model WHERE MID == 1"))
print("Join (SELECT MID, Name, Vorname FROM Model CROSS JOIN Shooting):", query("SELECT MID, Name, Vorname FROM Model CROSS JOIN Shooting"))


