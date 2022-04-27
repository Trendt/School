# OOP (Objekt-Orientierte-Programmierung)

### Klassen und Objekte

### Grundbegriffe

* Abstraktion
	* Konzentration aufs Wesentliche
* Polymorphie
	* Vielgestaltigkeit
	* überschreiben von methoden der eltern klasse in einer kindklasse
* Vererbung
	* Elternklasse/Superklasse
	* Kindklasse/Subklasse
	* z.b. Person (Elternklasse), Kunde(Kindklasse), Mitarbeiter(Kindklasse)
	* uml: Kunde-> Person, Mitarbeiter->Person
* Kapselung
	* Abkapseln von Attributen der Klasse
	* -> so viel "verstecken" wie möglich

### 5 Schritte des OOD (Objekt orientiertes Design)

1. Anforderungen erfassen
2. Anwendung beschreiben
3. Objekte herausarbeiten
4. Interaktion definieren
5. Klassendiagramm erstellen

### 1. Anforderungen definieren

* Funktionale Anforderungen
	* Features/Fähigkeiten
	* z.b.: "Das system muss suchanfragen mit dem namen und geburtsdatum annehmen können"

* Nicht-Funktionale Anforderungen
	* Hilfe
	* Gesetze
	* Performance
	* Support
	* Sicherheit
	* z.b.: "Das system muss suchanfragen innerhlab von 2sekunden beantworten"

### Furps/Furps+

Functionality | Funktionalität

Usability | Benutzerfreundlichkeit

Reliability | Zuverlässigkeit

Performance | Effizienz

Supportability | Wartbarkeit

+ 

Design | Designanforderungen

Implementation | Implementierung

Interface | Schnittstellen

Physical | Physische Anforderungen

### UML(unified modelling language)

* Klassendiagramm

* Diagramm-tools:
	* Visio/Omnigraffle
* webbasierte diagrammersetllung:
	* giffy.com, creately.com, licdchart,com
* Pgrammbasierte: IDEs
	* Visual Studio, Eclipse

	
### Klassendiagramm

* table: header=classname
	first row = attributes
	second row = methods

### Abstrakte klassen:
	* klasse, benötigt weil andere davon abhängig jedoch selbst nie benutzt

### Aggregation und Komposition
* Aggregation:
	* "besteht aus", "hat"
	* leere Raute
* Komposition:
	* Existenz von kindern abhängig von existenz der eltern
	* volle raute
	* wenn eltern gelöscht -> kind löschen



