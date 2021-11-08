import sqlite3
from sys import exit

# connection = sqlite3.connect("buchhandel.db")


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
 
def create_tables() -> None:
    cursor = connection.cursor()
    cursor.execute(create_verlag_table)
    cursor.execute(create_buch_table)
    cursor.execute(create_kunde_table)
    cursor.execute(create_kunde_buch_table)
    cursor.close()

class Verlag:
    def __init__(self, name:str, sitz:str, ansprechpartner:str, existing:bool=False, vid:int=None) -> None:
        self.name = name
        self.sitz = sitz
        self.ansprechpartner = ansprechpartner
        self.existing = existing
        
        if self.existing == False:
            self.insert()
            self.existing = True
        
        if vid:
           self.id = vid
        else: 
            self.id = self.get_verlag_id()
            print("Verlag.id:", self.id)
        
    def insert(self) -> None:
        cursor = connection.cursor()
        insert_statement = """INSERT INTO Verlag(Name, Sitz, Ansprechpartner) 
                            VALUES(?, ?, ?);"""
                            
        data = (str(self.name), str(self.sitz), str(self.ansprechpartner))
        cursor.execute(insert_statement, data)
        cursor.close()
        
    def get_verlag_id(self) -> int:
        # überarbeiten
        cursor = connection.cursor()
        
        data = (str(self.name), str(self.sitz), str(self.ansprechpartner))
        print(data)
        request_statement = """SELECT * FROM VERLAG WHERE NAME = ? AND Sitz = ? AND Ansprechpartner = ?;"""
        cursor.execute(request_statement, data)
        data = cursor.fetchall()
        

        if len(data) != 1:
            print("data:", data)
            exit(1)
        else:
            print("data:", data)
            return int(data[0][0])
    
class Buch:
    def __init__(self, ISBN:int, kategorie:str, titel:str, autor:str, preis:float, lieferbar:bool, bewertung:float, verlag:Verlag) -> None:
        self.ISBN = ISBN
        self.kategorie = kategorie
        self.titel = titel
        self.autor = autor
        self.preis = preis
        self.lieferbar = lieferbar
        self.bewertung = bewertung
        self.verlag = verlag
        
        try:
            self.insert()
        except:
            pass
        
    def insert(self) -> None:
        cursor = connection.cursor()
        insert_statement = """INSERT INTO Buch(ISBN, Kategorie, Titel, Autor, Preis, lieferbar, Bewertung, VID)
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?);"""
                    
        data = (int(self.ISBN), str(self.kategorie), str(self.titel), str(self.autor), float(self.preis), bool(self.lieferbar), float(self.bewertung), int(self.verlag.id))
        cursor.execute(insert_statement, data)    
        cursor.close()
        
class Kunde:
    def __init__(self, username:str, email:str, passwort:str, addresse:str=None, vorname:str=None, nachname:str=None, existing:bool=False) -> None:
        self.username = username
        self.email = email
        self.passwort = passwort
        self.addresse = addresse
        self.vorname = vorname
        self.nachname = nachname
        self.existing = existing
        
        if self.existing == False:
            self.insert()
            self.existing = True
        
    def bestell(self, buch:Buch, anzahl:int=1) -> None:
        cursor = connection.cursor()
        insert_statement = """INSERT INTO KundeBuch(ISBN, Username, Anzahl)
                    VALUES(?, ?, ?)"""
                    
        data = (int(buch.ISBN), str(self.username), int(anzahl))
        cursor.execute(insert_statement, data)
        cursor.close()

    def insert(self) -> None:
        cursor = connection.cursor()
        insert_statement = """INSERT INTO Kunde(Username, Email, Passwort, Addresse, Vorname, Nachname)
                    VALUES(?, ?, ?, ?, ?, ?);"""
                    
        data = (str(self.username), str(self.email), str(self.passwort), str(self.addresse), str(self.vorname), str(self.nachname))
        cursor.execute(insert_statement, data)
        cursor.close()


class DBManager:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self.create_tables()
        
        self.verlaege = []
        self.buecher = []
        self.kunden = []
        
        self.get_data()
        
    def commit_close(self):
        self.conn.commit()
        self.conn.close()
        
    def create_tables(self):
        self.cursor.execute(create_verlag_table)
        self.cursor.execute(create_buch_table)
        self.cursor.execute(create_kunde_table)
        self.cursor.execute(create_kunde_buch_table)
        
    def get_verlag_by_id(self, id:int):
        for v in self.verlaege:
            if v.id == id:
                return v
     
    def get_data(self):
        self.cursor.execute("SELECT * FROM Verlag;")
        verlaege = self.cursor.fetchall()
        self.verlaege = [Verlag(v[1], v[2], v[3], existing=True ,vid=v[0]) for v in verlaege]
        print("verlaege:", [v.name for v in self.verlaege])
        
        self.cursor.execute("SELECT * FROM Buch;")
        buecher = self.cursor.fetchall()
        self.buecher = [Buch(b[0], b[1], b[2], b[3], b[4], bool(b[5]), b[6], self.get_verlag_by_id(b[7])) for b in buecher]
        print("buecher:", [b.titel for b in self.buecher])
        
        self.cursor.execute("SELECT * FROM Kunde;")
        kunden = self.cursor.fetchall()
        self.kunden = [Kunde(k[0], k[1], k[2], k[3], k[4], k[5], existing=True) for k in kunden]
        print("kunden:", [k.username for k in self.kunden])
        
    def insert_verlag(self, name:str, sitz:str, ansprechpartner:str):
        self.cursor.execute("""
                INSERT INTO Verlag (Name, Sitz, Ansprechpartner) 
                VALUES (?, ?, ?);
            """, (name, sitz, ansprechpartner))
    
    def insert_buch(self, ISBN:int, kategorie:str, titel:str, autor:str, preis:float, lieferbar:bool, bewertung:float, vid:int):
        self.cursor.execute("""
                INSERT INTO Buch
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (ISBN, kategorie, titel, autor, preis, lieferbar, bewertung, vid))
    
    def insert_kunde(self, username:str, email:str, passwort:str, addresse:str=None, vorname:str=None, nachname:str=None):
        self.cursor.execute("""
                INSERT INTO Kunde
                VALUES (?, ?, ?, ?, ?, ?)
            """, (username, email, passwort, addresse, vorname, nachname))
        
    def delete_kunde(self, kunde:Kunde):
        pass
    
    def delete_buch(self, buch:Buch):
        pass
    
    def delete_verlag(self, verlag:Verlag):
        pass
        
dbmanager = DBManager("buchhandel.db")
dbmanager.insert_verlag("Verlagsname", "Verlagssitz", "Ansprechpartner")

dbmanager.commit_close()