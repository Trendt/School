from pwgen import PWGen
from dbmanager import DBManager
import sys
from constants import password_standard_lenght

class Saver:
    def __init__(self, db_location:str="pw.db"):
        self.pwgen = PWGen()
        self.dbmanager = DBManager(db_location)
        
        self.user = None
        self.user_passwort = None
        
        
        print("-"*20)
        print(" "*5, "PWManager")
        self.startMenu()
        
    def startMenu(self):
        print("-"*20)
        print(" "*5, "Startmenu")
        action = input("Login, Register or Exit? [L/R/E]: ").strip().lower()
        if action == "l":
            self.login()
        elif action == "r":
            self.register()
        elif action == "e":
            sys.exit(1)
        else:
            print("Invalid option!")
            self.startMenu()
        
    def login(self):
        print("-"*20)
        print(" "*6, "Login", "\n")
        
        self.user = input("Username: ")
        self.user_passwort = input("Password: ")
        exists = self.dbmanager.check_user(self.user, self.user_passwort)
        if exists:
            self.menu()
        else:
            self.startMenu()
            
    def register(self):
        print("-"*20)
        print(" "*5, "Register", "\n")
        
        self.user = input("Username: ")
        self.user_passwort = input("Password: ")
        self.dbmanager.insert_user(self.user, self.user_passwort)
        print("Registered successfully!")
        
        self.startMenu()
                
    def menu(self):
        print("-"*20)
        print(" "*6, "Menu")       
        
        option = input("Show, create, delete password(s) or Logout? [S/C/D/L]: ").strip().lower()
        print("-"*20)
        if option == "s":
            passwords = self.dbmanager.get_user_data(self.user, self.user_passwort)
            if passwords != None:
                for p in passwords:
                    print(f"{p[0]} | {p[1]}   |   {p[2]}   | {p[3]}")
            self.menu()
        elif option == "d":
            passwords = self.dbmanager.get_user_data(self.user, self.user_passwort)
            for p in passwords:
                print(f"ID: {p[0]} | {p[1]}   |   {p[2]}   | {p[3]}")
            id_delete = input("Which id should be deleted? (0 for None): ")
            self.dbmanager.delete_passwort(id_delete)
            self.menu()
        elif option == "c":
            website = input("Website/usage: ").strip()
            generate_ = input("generate password? [n] else yes").strip().lower()
            if generate_ == "n":
                password = input("password: ").strip()
            else:
                length = password_standard_lenght
                try:
                    length = int(input(f"passwordlength(standard={password_standart_lenght}): "))
                except:
                    pass
                password = self.pwgen.generate_pw(length=length)
            note = input("Note: ")
            self.dbmanager.insert_passwort(self.user, password, website, notes=note)
            self.menu()
        elif option == "l":
            self.user = None
            self.user_passwort = None
            self.startMenu()
        else:
            print("Invalid option!")
            self.menu()
         
saver = Saver()