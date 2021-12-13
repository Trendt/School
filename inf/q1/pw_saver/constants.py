# DB Tables:

user_table = """
    CREATE TABLE IF NOT EXISTS User(
        uname VARCHAR(32) PRIMARY KEY,
        passwort VARCHAR(255)
    );
"""

passwort_table = """
    CREATE TABLE IF NOT EXISTS Passwort(
        ID INTEGER PRIMARY KEY,
        uname VARCHAR(32) ,
        passwort VARCHAR(255) NOT NULL,
        website VARCHAR(255) NOT NULL,
        notes TEXT,
        FOREIGN KEY(uname) REFERENCES User(uname)
    );
"""

# other:
password_standard_lenght = 32