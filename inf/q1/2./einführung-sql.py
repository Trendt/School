import sqlite3 as sql

data = [[1, None, 3, "Christoph Reeg", None,           None],
        [2,    1, 1,      "junetz.de", None,   "069-754758"],
        [3,    2, 1,            "Uli", None,           None],
        [4,    3, 1,            "JCP", None,   "069-754758"],
        [5,    1, 2,          "Maier", None, "06196-671797"],
        [6,    5, 2,          "Maier", None, "069-97640232"],]

conn = sql.connect("test.db")
cur = conn.cursor()

def create_table():
    cur.execute('''CREATE TABLE Mitarbeiter 
            (MitarbNr INT PRIMARY KEY     NOT NULL,
            VorgesetztenNr           INT,
            AbtNr            INT     NOT NULL,
            Name        TEXT       NOT NULL,
            GebDatum         DATE,
            Telephon         TEXT);''')

def insert_values(values:list):
    for v in values:
        data_tuple = tuple(v)
        cur.execute(f"INSERT INTO Mitarbeiter (MitarbNr, VorgesetztenNr, AbtNr, Name, GebDatum, Telephon) VALUES (?,?,?,?,?,?);", data_tuple)
    conn.commit()

def execute(sql_statement:str) -> list:
    cur.execute(sql_statement)
    return cur.fetchall()

def print_tabular(table:list, *args, **kwargs):
    col_widths = [0 for x in range(len(table))]
    reversed_table = [[None for l in range(len(table))] for x in table[0]]
    
    for col_num, col in enumerate(table):
        for row, obj in enumerate(col):
            reversed_table[row][col_num] = obj
    
    col_widths = [max([len(str(s)) for s in m]) for m in reversed_table]    
    
    for row in table:
        row_str = ""
        for enum, col in enumerate(row):
            row_str += " " + str(col) + (col_widths[enum] - len(str(col)) + 1)*" "  + ("|" if enum != len(row)-1 else "")
        print(row_str)
        # print(len(row_str) * "-")
    
    print(row_str)
    print(*args, **kwargs)

# create_table()
# insert_values(data)

print("\n----------------\nSelect Aufgaben:\n")
print_tabular(execute("SELECT * from Mitarbeiter;"), "\n")
print_tabular(execute('SELECT * from Mitarbeiter WHERE Name="Maier";'), "\n")
print_tabular(execute('SELECT * from Mitarbeiter WHERE (VorgesetztenNr=1) AND (AbtNr=1);'), "\n")

print("\n----------------\nProjektion Aufgaben:")
print_tabular(execute('SELECT all Telephon FROM Mitarbeiter;'))
print_tabular(execute('SELECT DISTINCT Telephon FROM Mitarbeiter;'))
print_tabular(execute('SELECT AbtNr, Name, Telephon FROM Mitarbeiter;'))

print("\n----------------\nSortier Aufgaben:")
print_tabular(execute('SELECT * FROM Mitarbeiter ORDER BY Name'))
print_tabular(execute('SELECT * FROM Mitarbeiter ORDER BY Name DESC;'))
print_tabular(execute('SELECT * FROM Mitarbeiter ORDER BY GebDatum,Name;'))

print("\n----------------\nFunktionen Aufgaben:")
print_tabular(execute('SELECT count(*) FROM Mitarbeiter;'))
print_tabular(execute('SELECT count(*) FROM Mitarbeiter GROUP BY AbtNr;'))

print("\n----------------\nLimit Aufgaben:")
print_tabular(execute('SELECT * FROM Mitarbeiter LIMIT 5,10;'))
print_tabular(execute('SELECT * FROM Mitarbeiter LIMIT 5;'))
print_tabular(execute('SELECT * FROM Mitarbeiter LIMIT 0, 5;'))

print("\n----------------\Where Aufgaben:")
print_tabular(execute('SELECT Name, AbtNr FROM Mitarbeiter WHERE (AbtNr=1) OR (VorgesetztenNr IS NULL);'))

print("\n----------------\Like Aufgaben:")
print_tabular(execute('SELECT Name, Telephon FROM Mitarbeiter WHERE (Telephon LIKE "%96-%");'))
print_tabular(execute('SELECT Name, Telephon FROM Mitarbeiter WHERE (Name LIKE "M_ier");'))

print("\n----------------\Like Aufgaben:")
print_tabular(execute('SELECT * FROM Mitarbeiter WHERE (AbtNr BETWEEN 2 AND 3);'))
print_tabular(execute('SELECT * FROM Mitarbeiter WHERE Telephon IN ("06196-671797","069-97640232");'))

conn.close()