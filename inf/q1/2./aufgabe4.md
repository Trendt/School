a)
Fahrschüler(Name, Vorname, Geburtsdatum, Anzahl\ Fahrstunden, Theorie\ bestanden, Praxis\ bestanden, Fahrlerer Vorname, Fahrlerer Nachname, Fahrlehrer Telefonnummer)

Attribut | Datentype
--- | ---
Name | string
Vorname | string
Geburtsdatum | date
anzahl Fahrstunden | int
Theorie bestanden | boolean
Praxis bestanden | boolean
Fahrlerer Vorname | string
Fahrlerer Nachname | string
Fahrlerer Telefonnummer | string

kein geigneter key --> künstlicher key (id)
b)
--> Fahrlerer können mehrere Schüler haben z.b. Manfred Schulte hat 2 verschiedene Schüler und seine Daten sind in beiden zeilen vorhanden
wenn z.b. manfred seine Telefonnummer ändert, und dies in einer Zeile vergessen wird, sorgt dies für wiedersprüche. --> inkonsisten


