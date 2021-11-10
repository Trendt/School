create_verlag_table =  """CREATE TABLE IF NOT EXISTS Verlag (
                    VID INTEGER PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL UNIQUE,
                    Sitz VARCHAR(255) NOT NULL,
                    Ansprechpartner VARCHAR(255) NOT NULL
                );"""

create_buch_table =    """CREATE TABLE IF NOT EXISTS Buch (
                    ISBN INTEGER PRIMARY KEY,
                    Titel VARCHAR(255) NOT NULL,
                    Preis REAL NOT NULL,
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
                
create_kunde_buch_table =  """CREATE TABLE IF NOT EXISTS Bestellung (
                        ISBN INT NOT NULL,
                        Username VARCHAR(255) NOT NULL,
                        Anzahl INT NOT NULL
                    );"""
                    
create_autor_table = """CREATE TABLE IF NOT EXISTS Autor(
                        ID INTEGER PRIMARY KEY,
                        Name VARCHAR(255) NOT NULL UNIQUE
                    );""" #N:M buch -->

create_autor_buch_table = """CREATE TABLE IF NOT EXISTS AutorBuch(
                        AutorID INTEGER NOT NULL,
                        ISBN INTEGER NOT NULL,
                        FOREIGN KEY(AutorID) REFERENCES Autor(ID),
                        FOREIGN KEY(ISBN) REFERENCES Buch(ISBN)
                    );"""

create_kategorie_table = """CREATE TABLE IF NOT EXISTS Kategorie(
                        ID INTEGER PRIMARY KEY,
                        Name Varchar(255) NOT NULL UNIQUE
                    );""" #N:M buch
                    
create_kategorie_buch_table = """CREATE TABLE IF NOT EXISTS KategorieBuch(
                        KategorieID INTEGER NOT NULL,
                        ISBN INTEGER NOT NULL,
                        FOREIGN KEY(KategorieID) REFERENCES Kategorie(ID),
                        FOREIGN KEY(ISBN) REFERENCES Buch(ISBN)
                    );"""

create_preis_table = """CREATE TABLE IF NOT EXISTS Preis(
                        ID INTEGER PRIMARY KEY,
                        Preis INTEGER NOT NULL,
                        Datum DATE NOT NULL,
                        ISBN INTEGER NOT NULL,
                        FOREIGN KEY(ISBN) REFERENCES Buch(ISBN)
                    );""" #N:1 buch