class Medium:
    zaehler = 0
    # Konstruktor
    def __init__(self, titel, preis):
        Medium.zaehler += 1
        self.code = 100000 + Medium.zaehler
        self.titel = titel
        self.preis = preis 
        self.kommentar = ''
    def getCode(self):
        return self.code
    def getTitel(self):
        return self.titel
    def getPreis(self):
        return self.preis
    def setPreis(self, preis):
        self.preis = preis
    def getKommentar(self):
        return self.kommentar
    def setKommentar(self, kommentar): 
        self.kommentar = kommentar
    def druckeInfo(self):
        print("Code:", self.code)
        print("Titel:", self.titel)
        print("Preis:", self.preis, "Euro")
        print("Kommentar:", self.kommentar)
        print()
# Subklasse Buch
class Buch(Medium):
    # Konstruktor
    def __init__(self, titel, autor, verlag, jahr, preis):
        # Konstruktor der Superklasse aufrufen
        # Buch erbt Titel und Preis:
        Medium.__init__(self, titel, preis)
        # neue, Buch-spezifische Eigenschaften:
        self.autor = autor
        self.verlag = verlag
        self.erscheinungsjahr = jahr
    def getAutor(self):
        return self.autor
    def getVerlag(self):
        return self.verlag
    def getErscheinungsjahr(self):
        return self.erscheinungsjahr
    def druckeInfo(self):
        print("Code:", self.code)
        print("Titel:", self.titel)
        print("Autor:", self.autor)
        print("Verlag:", self.verlag, ",", self.erscheinungsjahr)
        print("Preis:", self.preis, "Euro")
        print("Kommentar:", self.kommentar)
        print()
# Subklasse CD
class CD(Medium):
    def __init__(self, titel, interpret, titelanz, zeit, preis):
        Medium.__init__(self, titel, preis)
        # neue, CD-spezifische Eigenschaften:
        self.interpret = interpret
        self.titelanzahl = titelanz
        self.spieldauer = zeit
    def getInterpret(self): 
        return self.interpret
    def getTitelanzahl(self):
        return self.titelanzahl
    def getSpieldauer(self): 
        return self.spieldauer
    def druckeInfo(self):
        print("Code:", self.code)  
        print("Titel:", self.titel) 
        print("Interpret:", self.interpret) 
        print("Spieldauer:", self.spieldauer, "min,", self.titelanzahl, "Titel")  
        print("Preis:", self.preis, "Euro") 
        print("Kommentar:", self.kommentar)  
        print()
# Subklasse Video
class Video(Medium):
    def __init__(self, titel, reg, zeit, preis): 
        Medium.__init__(self, titel, preis)
        # neue, Video-spezifische Eigenschaften:
        self.regisseur = reg 
        self.spieldauer = zeit
    def getRegisseur(self): 
        return self.regisseur
    def getSpieldauer(self): 
        return self.spieldauer
    def druckeInfo(self):
        print("Code:", self.code)  
        print("Titel:", self.titel) 
        print("Regisseur:", self.regisseur) 
        print("Spieldauer:", self.spieldauer, "min")  
        print("Preis:", self.preis, "Euro") 
        print("Kommentar:", self.kommentar)  
        print()

class Kasette(Medium):
    def __init__(self, titel:str, autor:str, zeit_sek:int, preis:float):
        super().__init__(titel, preis)
        
        self.autor = autor
        self.zeit = zeit_sek

    def getAutor(self) -> str:
        return self.autor

    def getZeit(self) -> int:
        return self.zeit

    def druckeInfo(self):
        print("Code:", self.code)
        print("Titel:", self.titel)
        print("Autor:", self.autor)
        print("Spieldauer:", self.zeit//60,"min",self.zeit%60,"sek") 
        print("Preis:", self.preis,"Euro")
        print("Kommentar:", self.kommentar,"\n")
