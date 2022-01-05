import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "wellnesshotel"
    )

class DBManager:
    def __init__(self, connection):
        self.db = connection

    def execute(self, statement:str, data=None):
        cursor = self.db.cursor()
        cursor.execute(statement, data)
        result = cursor.fetchall()
        self.db.commit()
        return result

    def insert_ort(self, postleitzahl:int, ort:str):
        self.execute(f"INSERT INTO Ort(Ort.ort, Ort.postleitzahl) VALUES(%s, %s)", (ort, postleitzahl))

    def insert_masseur(self, vorname:str, name:str):
        self.execute(f"INSERT INTO Massuer(Massuer.Vorname, Massuer.Name) VALUES(%s, %s)", (vorname, name))

    def insert_gast(self, vorname:str, name:str, geschlecht:str, geburtsjahr:int, strasse:str, postleitzahl:int, MasseurID:int, r_vorname:str=None, r_name:str=None, r_strasse:str=None, r_postleitzahl:int=None):
        self.execute(f"INSERT INTO Gast(Gast.Vorname, Gast.Name, Gast.geschlecht, Gast.geburtsjahr, Gast.straße, Gast.postleitzahl, Gast.MasseurID, Gast.r_vorname, Gast.r_name, Gast.r_str, Gast.r_postleitzahl VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (vorname, name, geschlecht, geburtsjahr, strasse, postleitzahl, MasseurID, r_vorname, r_name, r_strasse, r_postleitzahl))

    def insert_bereich(self, bezeichnung:str):
        self.execute(f"INSERT INTO Bereich(Bereich.Bereichsbezeichnung) VALUES(%s)", (bezeichnung))

    def insert_bett(self, ZimmerNr:int, BereichsID:int):
        self.execute(f"INSERT INTO Bett(Bett.Zimmernummer, Bett.BereichsID) VALUES(%s, %s)", (ZimmerNr, BereichsID))

    def insert_bettenbelegung(self, BettID:int, GastID:int, Anreise, Abreise):
        self.execute(f"INSERT INTO Bettenbelegung(Bettenbelegung.BettID, Bettenbelegung.GastID, Bettenbelegung.Anreise, Bettenbelegung.Abreise) VALUES(%s, %s, %s, %s)", (BettID, GastID, Anreise, Abreise))

    def insert_Mittel(self, Bezeichnung:str):
        self.execute(f"INSERT INTO Mittel(Mittel.Bezeichnung) VALUES(%s)", (Bezeichnung))    

    def insert_massiert(self, GastID:int, MittelID:int):
        self.execute(f"INSERT INTO massiert(massiert.GastID, massiert.MittelID) VALUES(%s, %s)", (GastID, MittelID))

    def insert_behandlung(self, GastID:int, MittelID:int):
        self.execute(f"INSERT INTO behandlung(behandlung.GastID, behandlung.MittelID) VALUES(%s, %s)", (GastID, MittelID))

    def select_Gaeste(self) -> tuple:
        return self.execute("SELECT * FROM Gast")

    def select_Masseure(self) -> tuple:
        return self.execute("SELECT * FROM Massuer")        
dbmanager = DBManager(mydb)
print(dbmanager.select_Masseure())
print(dbmanager.select_Gaeste())
# dbmanager.insert_masseur("Olaf", "Scholz")
# dbmanager.insert_ort(12345, "Milchhausen")
dbmanager.insert_gast("vorname", "name", "geschlecht", 1992, "Sesamstraße 1a", 12345, 2)
