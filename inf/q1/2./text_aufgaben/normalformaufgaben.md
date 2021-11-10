# Aufgaben zu Normalformen


## S.339

### Aufgabe 1

a)

Es könnten Probleme entstehen, da die Namen und Noten aller schüler in einem Feld sind.
--> schüler und noten nicht richtig zuteilbar

b)

Schueler

ID | Vorname | Nachname
--- | --- | ---
1 | Karl | Klug
2 | Daniel | Denker
3 | Frank | Frisch
4 | Anna | Ableitung
5 | Ina | Integral
6 | Konny | Zuse

Fach

ID | Name
--- | ---
1 | Deutsch
2 | Mathematik
3 | Informatik

Note

-> Schueler.ID | -> Fach.ID | Note
--- | --- | ---
1 | 1 | 1
2 | 1 | 2+
3 | 1 | 4+
4 | 2 | 3+
5 | 2 | 2-
6 | 3 | 1-


### Aufgabe 2

a ) 

Carsharing
_KundenNr_ | Name | Tel | _Ausleihdatum_ | _Kennzeichen_ | Hersteller | KM-Stand | Baujahr
--- | --- | --- | --- | --- | --- | --- | ---
1 | Bernd | 9123901 | 8.11.2019 | B HR 1872 | VW | 192159 | 2001
2 | Bertha | 29580192 | 11.11.2019 | B HR 1873 | Mercedes | 19023 | 2019
3 | Bodo | 40512394 | 12.11.2019 | B HR 1874 | BMW | 72900 | 2018

b) 
Änderungs-, Einfügeanomalien könnten auftreten, löschanomalien nicht wirklich, da dann einfach nur daten fehlen.

c) 
Funktionale abhängigkeiten liegen zwischen dem namen und der telefonnummer vor.



d)
3 Tabellen:

Kunde
_KundenNr_ | Vorname | Nachname | Tel 
--- | --- | --- | ---
1 | Bernd | Blocksberg | 9123901

Auto
_Kennzeichen_ | Hersteller | KM-Stand | Baujahr 
--- | --- | --- | ---
B HR 1872 | VW | 192159 | 2001

Carsharing
-> Auto.Kennzeichen | -> Kunde.KundenNR | Ausleihdatum
--- | --- | ---
B HR 1872 | 1 | 8.11.2019





## S.340

### Aufgabe 4

a)

Sowohl die Faachgebiete, als auch die Institution wird redundant gespeichert, da diese immerwieder die gleichen sind.


b)

Das Institut ist transitiv abhängig von der MitarbeiterID.

c) 

Fachgebiete
_FachgebietID_ | Fachgebiet | Institut
--- | --- | ---
1 | Datenbank- und Informationssysteme | Informatik
2 | Codes und Kryptografie | Informatik

Mitarbeiter
MitarbeiterID | Nachname | ->FachgebietID
--- | --- | ---
123 | Engels | 1
128 | Blömer | 2
