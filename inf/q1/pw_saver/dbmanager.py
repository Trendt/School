import sqlite3
from constants import passwort_table, user_table
class DBManager:
    def __init__(self, file="pw.db"):
        self.conn = sqlite3.Connection(file)
        self.create_tables()
        
    def execute(self, STATEMENT:str, DATA:tuple=()):
        cursor = self.conn.cursor()
        cursor.execute(STATEMENT, DATA)
        data = cursor.fetchall()
        self.conn.commit()
        cursor.close()
        
        if data:
            return data
        
    def create_tables(self) -> None:
        self.execute(user_table)
        self.execute(passwort_table)
        
    def insert_user(self, user_name:str, user_passwort:str) -> None:
        try:
            self.execute("INSERT INTO User(uname, passwort) VALUES(?,?)", (user_name, user_passwort))
        except:
            print("username allready exists")
        
    def insert_passwort(self, user_name:str, passwort:str, website:str, notes:str=None) -> None:
        self.execute("INSERT INTO Passwort(uname, passwort, website, notes) VALUES(?,?,?,?)", (user_name, passwort, website, notes))
        
    def delete_passwort(self, ID:int) -> None:
        self.execute("DELETE FROM Passwort WHERE ID == ?", (ID,))
        
    def check_user(self, user_name:str, user_passwort:str) -> bool:
        check = self.execute("SELECT * FROM User WHERE uname == ? AND passwort == ?", (user_name, user_passwort))
        if check != None:
            return True
        else:
            return False
        
    # def delete_user(self, user_name:str, user_passwort:str):
    #     self.execute("DELETE FROM Passwort, User WHERE User.uname == Passwort.uname AND User.uname == ? AND User.passwort == ?", (user_name, user_passwort))
        
    def get_user_data(self, user_name:str, user_passwort:str):
        data = self.execute("SELECT Passwort.ID, Passwort.website, Passwort.passwort, Passwort.notes FROM Passwort, User WHERE Passwort.uname == User.uname AND User.uname == ? AND User.passwort == ?", (user_name, user_passwort))
        return data