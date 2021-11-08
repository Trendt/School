import sqlite3
from sys import exit
from constants import *

class DBManager:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self.create_tables()
        
        self.verlaege = []
        self.buecher = []
        self.kunden = []
        self.bestellungen = []
        
        self.get_data()
        
    def commit_close(self):
        self.conn.commit()
        self.conn.close()
        
    def create_tables(self):
        self.cursor.execute(create_verlag_table)
        
        # buch:
        self.cursor.execute(create_buch_table)
        self.cursor.execute(create_preis_table)
        self.cursor.execute(create_kategorie_table)
        self.cursor.execute(create_kategorie_buch_table)
        self.cursor.execute(create_autor_table)
        self.cursor.execute(create_autor_buch_table)
        
        self.cursor.execute(create_kunde_table)
        self.cursor.execute(create_kunde_buch_table)
        self.conn.commit()
     
    def __repr__(self):
        verlag_str = f"Verlaege: {[v[1] for v in self.verlaege]}"
        buch_str = f"Buecher: {[b[2] for b in self.buecher]}"
        kunde_str = f"Kunden: {[k[0] for k in self.kunden]}"
        bestellungen_str = f"Bestellungen: {self.buecher}"
        
        return verlag_str + "\n" + buch_str + "\n" + kunde_str + "\n" + bestellungen_str
     
    def query(self, QUERY:str, args:tuple=()):
        self.cursor.execute(QUERY, args)
        self.conn.commit()
        self.get_data()
        try:
            return self.cursor.fetchall()
        except:
            return None
    
    def get_data(self):
        self.cursor.execute("SELECT * FROM Verlag;")
        self.verlaege = self.cursor.fetchall()
        
        self.cursor.execute("SELECT * FROM Buch;")
        self.buecher = self.cursor.fetchall()
        
        self.cursor.execute("SELECT * FROM Kunde;")
        self.kunden = self.cursor.fetchall()
        
        self.cursor.execute("SELECT * FROM Bestellung;")
        self.bestellungen = self.cursor.fetchall()
        
    def insert_verlag(self, name:str, sitz:str, ansprechpartner:str):
        try:
            self.cursor.execute("""
                    INSERT INTO Verlag (Name, Sitz, Ansprechpartner) 
                    VALUES (?, ?, ?);
                """, (name, sitz, ansprechpartner))
            self.conn.commit()
        except Exception as e:
            print(e)
    
    def insert_buch(self, ISBN:int, kategorie:tuple[str], titel:tuple[str], autoren:tuple, preis:float, lieferbar:bool, bewertung:float, vid:int):
        self.cursor.execute("""
                INSERT INTO BUCH
                VALUES (?, ?, ?, ?, ?, ?)
            """, (ISBN, titel, preis, lieferbar, bewertung, vid))
        
        for autor in autoren:
            #versuche den autor zu inserten, wenn es scheitert ist er bereits 
            try:
                self.cursor.execute("INSERT INTO Autor (Name) VALUES (?)",
                                    (autor,))
            except:
                pass
            
            # kriege id wo autorname = name --> namen könnten doppelt sein? --> nicht verhinderbar da man nichts als namen hat
            self.cursor.execute("SELECT ID FROM Autor WHERE Name == ?;",
                                (autor,))
            self.conn.commit()
            
            autor_id = self.cursor.fetchall()[0][0]
            self.cursor.execute("INSERT INTO AutorBuch VALUES (?, ?)",
                                (autor_id, ISBN))
        for kat in kategorie:
            # check if category exists, if get katID and fill katID,ISBN in KategorieBuch
            try:
                self.cursor.execute("INSERT INTO Kategorie (Name) VALUES (?)",
                                    (kat,))
            except:
                pass
            
            self.cursor.execute("SELECT ID FROM Kategorie WHERE Name == ?;",
                                (kat, ))
            kategorie_id = self.cursor.fetchall()[0][0]
            self.cursor.execute("INSERT INTO KategorieBuch VALUES(?, ?)",
                                (kategorie_id, ISBN))
        
        self.conn.commit()
    
    def insert_kunde(self, username:str, email:str, passwort:str, addresse:str=None, vorname:str=None, nachname:str=None):
        try:
            self.cursor.execute("""
                    INSERT INTO Kunde
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (username, email, passwort, addresse, vorname, nachname))
            self.conn.commit()
        except Exception as e:
            print(e)
        
    def insert_bestellung(self, ISBN:int, username:str, anzahl:int):
        try:
            self.cursor.execute("""
                    INSERT INTO Bestellung (ISBN, Username, Anzahl)
                    VALUES (?, ?, ?);
                """, (ISBN, username, anzahl))
            self.conn.commit()
        except Exception as e:
            print(e)
        
    def delete_bestellung(self, ISBN:int=None, username:str=None):
        self.cursor.execute("""
                DELETE FROM Bestellung WHERE ISBN == ? or Username == ?;
            """, (ISBN, username))
        self.conn.commit()
    
    def delete_kunde(self, username:str):
        self.cursor.execute("""
                DELETE FROM Kunde WHERE Username == ?;
            """, (username,))
        self.delete_bestellung(username=username)
        self.conn.commit()
    
    def delete_buch(self, ISBN:int=None, VID:int=None):
        self.delete_bestellung(ISBN=ISBN)
        
        self.cursor.execute("DELETE FROM AutorBuch WHERE ISBN == ? OR ISBN == (SELECT ISBN FROM Buch WHERE VID == ?);",
                            (ISBN, VID))
        
        self.cursor.execute("DELETE FROM KategorieBuch WHERE ISBN == ? OR ISBN == (SELECT ISBN FROM Buch WHERE VID == ?);",
                            (ISBN, VID))
        
        self.cursor.execute("""
                DELETE FROM Buch WHERE ISBN == ? OR VID == ?;
            """, (ISBN, VID))
        self.conn.commit()
    
    def delete_verlag(self, verlagID:int):
        self.cursor.execute("DELETE FROM Verlag WHERE VID == ?;", (verlagID,))
        
        self.cursor.execute(""" 
                DELETE FROM Bestellung WHERE Bestellung.ISBN == (SELECT Buch.ISBN FROM Buch WHERE Buch.VID == ?);
            """, (verlagID,))
        
        self.delete_buch(VID=verlagID)
        self.conn.commit()
        
    
        
dbmanager = DBManager("buchhandel.db")
# dbmanager.insert_verlag("Verlagsname", "Verlagssitz", "Ansprechpartner")
dbmanager.delete_buch(ISBN=1337)
dbmanager.insert_buch(1337, ("Kategorie 1", "Kategorie 2"), "titel", ("Autor 1", "Autor 2"), 35.99, True, 10.0, 1)
# dbmanager.insert_kunde("username", "email@provider.com", "passwort", addresse="addresse", vorname="Vorname", nachname="Nachname")
# dbmanager.insert_bestellung(1337, "username", 4)

print("Vor löschen:\n", dbmanager)

# dbmanager.delete_kunde("username")
# dbmanager.delete_verlag(1)

# print("\nnach löschen:\n", dbmanager)
# dbmanager.commit_close()