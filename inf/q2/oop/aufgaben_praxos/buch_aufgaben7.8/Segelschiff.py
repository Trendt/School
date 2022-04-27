class Segelschiff:
    def __init__(self, anzahlMasten:int, crewMitglieder:int):
        self.__anzahlMasten = anzahlMasten
        self.__crewMitglieder = crewMitglieder

    def setAnzahlMasten(self, neueZahl:int):
        self.__anzahlMasten = neueZahl

    def getAnzahlMasten(self) -> int:
        return self.__anzahlMasten

    def setCrewMitglieder(self, n:int):
        self.__crewMitglieder = n

    def getCrewMitglieder(self) -> int:
        return self.__crewMitglieder

class Artikel:
    def __init__(self, preis:float, marke:str):
        self.__preis = preis
        self.__marke = marke

    def setMarke(self, marke:str):
        self.__marke = marke

    def getMarke(self) -> str:
        return self.__marke

    def setPreis(self, preis:float):
        self.__preis = preis

    def getPreis(self) -> float:
        return self.__preis

class Hund:
    def __init__(self, name:str, rasse:str):
        self.__name = name
        self.__rasse = rasse

    def setName(self, name:str):
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def setRasse(self, rasse:str):
        self.__rasse = rasse

    def getRasse(self) -> str:
        return self.__rasse

# ----------------

class Auto:
    def __init__(self, farbe:str, kennzeichen:str, preis:float, baujahr:int):
        self.farbe = farbe
        self.kennzeichen = kennzeichen
        self.preis = preis
        self.baujahr = baujar

    def setFarbe(self, farbe:str):
        self.farbe = farbe

    def getFarbe(self) -> str:
        return self.farbe

    def setKennzeichen(self, kennzeichen:str):
          self.kennzeichen = kennzeichen
       
    def getKennzeichen(self) -> str:
          return self.kennzeichen

    def setPreis(self, preis:float):
          self.farbe = farbe
       
    def getPreis(self) -> float:
          return self.preis

    def setBaujahr(self, baujahr:int):
        self.baujahr = baujahr

    def getBaujahr(self) -> int:
        return self.baujahr

    def __repr(self):
        return "Farbe: {self.farbe}

auto1 = Auto("rot", "B-AB-1234", 79_000.23, 2000)
auto2 = Auto("grüla", "BER-LI-3912", 2429.76, 2002)


s1.setAnzahlMasten(4)
print(s1.getAnzahlMasten())
