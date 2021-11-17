# S. 332 Nr.2 mit Zusatzaufgaben - Übung -

### 1.

Agentur
_Name_ | Ort
Ag1 | Berlin

Model
_MID_ | Name | Vorname | Geschlecht | Größe | ->Agentur.Name
--- | --- | --- | --- | --- | ---
1 | nachname | vorname | geschlecht | 172.4 | Ag1

Produkt 
_Bezeichnung_ | Hersteller
--- | ---
produkt1 | hersteller1

Fotograf
_Name_ | 
--- |
Fotograf1

Shooting 
_Termin_ | Ort | ->Fotograf.Name | Produkt.Bezeichnung
--- | --- | --- | ---
11.9.01 | New York | Fotograf1 | Flugzeug

Model_Shooting
->MID | ->Termin | Honorar
--- | --- | ---
1 | 11.9.01 | 120000

### 2.

Eine Agentur betreut beliebig viele Models.
Ein Model wird von genau einer Agentur betreut.

Ein Model nimmt an beliebig vielen Shootings teil.
Ein Shooting hat beliebig viele Models

Ein Produkt hat beliebig viele Shootings.
Ein Shooting ist für genau ein Produkt.

Ein Shooting wird von genau einem Fotograf gemacht.
Ein Fotograf macht beliebig viele Shootings

### 3.

Agentur
_Name_ | Ort
Agentur1 | Berlin
Agentur2 | Kölln 
Agentur3 | Bonn 
Agentur4 | Hamburg
Agentur5 | Potsdam

Model
_MID_ | Name | Vorname | Geschlecht | Größe | ->Agentur.Name
--- | --- | --- | --- | --- | ---
1 | nachname1 | vorname1 | weiblich | 172.4 | Agentur1
2 | nachname2 | vorname2 | männlich | 132.5 | Agentur1
3 | nachname3 | vorname3 | weiblich | 164.0 | Agentur2
4 | nachname4 | vorname4 | weiblich | 156.4 | Agentur4
5 | nachname5 | vorname5 | männlich | 201.9 | Agentur3

Produkt 
_Bezeichnung_ | Hersteller
--- | ---
produkt1 | hersteller1
produkt2 | hersteller1
produkt3 | hersteller2
produkt4 | hersteller5
produkt5 | hersteller8

Fotograf
_Name_ | 
--- |
Fotograf1 |
Fotograf2 |
Fotograf3 |
Fotograf4 |
Fotograf5 | 

Shooting 
_Termin_ | Ort | ->Fotograf.Name | ->Produkt.Bezeichnung
--- | --- | --- | ---
11.9.21 | New York | Fotograf1 | produkt1
12.9.21 | Berlin | Fotograf2 | produkt1
9.3.21 | Bonn | Fotograf2 | produkt2
1.1.22 | Berlin | Fotograf5 | produkt3
2.2.22 | Berlin | Fotograf4 | produkt4

Model_Shooting
->MID | ->Termin | Honorar
--- | --- | ---
1 | 11.9.21 | 120000
2 | 12.9.21 | 1230000
3 | 9.3.21  | 3001
3 | 2.2.22 | 3000
4 | 11.9.21 | 900

# 4.

> CREATE TABLE IF NOT EXISTS Agentur(
>	Name VARCHAR(255) PRIMARY KEY,
>	Ort VARCHAR(255) NOT NULL
>);

> CREATE TABLE IF NOT EXISTS Model(
>	MID INTEGER PRIMARY KEY,
>	Name Varchar(255),
>	Vorname Varchar(255),
>	Geschlecht Varchar(255),
>	Grösse REAL
>	AgenturName Varchar(255) NOT NULL,
>	FOREIGN KEY(AgenturName) REFERENCES Agentur(Name)
>);

> CREATE TABLE IF NOT EXISTS Produkt(
>	Bezeichnung VARCHAR(255) PRIMARY KEY,
>	Hersteller VARCHAR(255)
>);


> CREATE TABLE IF NOT EXISTS Shooting(
>	Termin DATE NOT NULL,
>	Ort VARCHAR(255) NOT NULL,
>	Produkt VARCHAR(255) NOT NULL,
>	Fotograf VARCHAR(255) NOT NULL,
>	FOREIGN KEY(Produkt) REFERENCES Produk(Bezeichnung),
>	FOREIGN KEY(Fotograf) REFERENCES Fotograf(Name),
>	PRIMARY KEY(Termin, Ort)
>);

### 5.

Selektion:
> SELECT * FROM Model;

Projektion:
> SELECT * FROM Model Where Model.Geschlecht == "männlich";

Join:
> SELECT MID, Name, Vorname CROSS JOIN Shooting;


### 6.

1NF:
* eingehalten
* es sind keine Felder vorhanden, in denen mehrere Werte gespeichert werden müssten

2NF:
<!---
* eingehalten
* kein Nichtschlüsselfeld, das direkt von einem anderem Feld abhängig ist wird in der gleichen Tabelle gespeichert
-->

* nicht eingehalten
* Fotograf.Name kann mehrfach vorkommen und ist Primary key --> probleme --> fotograf.id hinzufügen als PK(Primary Key)

3NF:
* nicht eingehalten
* name des herstellers könnte sich ändern --> extra tabelle und über hersteller.id

### Aufgabe 7
--> klausuraufgabe.py
