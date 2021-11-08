import sqlite3

connection = sqlite3.connect("buchhandel.db")


create_verlag_table =  """CREATE TABLE IF NOT EXISTS Verlag (
                    VID INTEGER PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL,
                    Sitz VARCHAR(255) NOT NULL,
                    Ansprechpartner VARCHAR(255) NOT NULL
                );"""

create_buch_table =    """CREATE TABLE IF NOT EXISTS Buch (
                    ISBN INTEGER PRIMARY KEY,
                    Kategorie VARCHAR(255) NOT NULL,
                    Titel VARCHAR(255) NOT NULL,
                    Autor VARCHAR(255) NOT NULL,
                    Preis INT NOT NULL,
                    lieferbar INT NOT NULL,
                    Bewertung REAL NOT NULL,
                    VID INT NOT NULL,
                    FOREIGN KEY(VID) REFERENCES Verlag(VID)
                );"""
                
create_kunde_table =   """CREATE TABLE IF NOT EXISTS Kunde (
                    Username VARCHAR(255) PRIMARY KEY,
                    Email VARCHAR(255) NOT NULL,
                    Passwort VARCHAR(255) NOT NULL,
                    Addresse VARCHAR(255),
                    Vorname VARCHAR(255),
                    Nachname VARCHAR(255)
                );"""
                
create_kunde_buch_table =  """CREATE TABLE IF NOT EXISTS KundeBuch (
                        ISBN INT NOT NULL,
                        Username VARCHAR(255) NOT NULL,
                        Anzahl INT NOT NULL
                    );"""

def insert_Verlag(name:str, sitz:str, ansprechpartner:str):
    cursor = connection.cursor()
    insert = """INSERT INTO Verlag(NAME, Sitz, Ansprechpartner)
                VALUES(?, ?, ?);"""
                
    cursor.execute(insert, (name, sitz, ansprechpartner))
    cursor.close()
                    
def insert_Buch(ISBN:int, kategorie:str, titel:str, autor:str, preis:float, lieferbar:bool, bewertung:float, vid:int):
    cursor = connection.cursor()
    insert = """INSERT INTO Buch(ISBN, Kategorie, Titel, Autor, Preis, lieferbar, Bewertung, VID)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?);"""
    
    cursor.execute(insert, (ISBN, kategorie, titel, autor, preis, lieferbar, bewertung, vid))        
    cursor.close()

def insert_Kunde(username:str, email:str, passwort:str, addresse:str=None, vorname:str=None, nachname:str=None):
    cursor = connection.cursor()
    insert = """INSERT INTO Kunde(Username, Email, Passwort, Addresse, Vorname, Nachname)
                VALUES(?, ?, ?, ?, ?, ?);"""
    cursor.execute(insert, (username, email, passwort, addresse, vorname, nachname))
    cursor.close()
    
def insert_KundeBuch(ISBN:int, username:str, anzahl:int=1):
    cursor = connection.cursor()
    insert = """INSERT INTO KundeBuch(ISBN, Username, Anzahl) 
                VALUES(?, ?, ?)"""
    
    cursor.execute(insert, (ISBN, username, anzahl))
    cursor.close()

cursor = connection.cursor()    
cursor.execute(create_verlag_table)
cursor.execute(create_buch_table)
cursor.execute(create_kunde_table)
cursor.execute(create_kunde_buch_table)
