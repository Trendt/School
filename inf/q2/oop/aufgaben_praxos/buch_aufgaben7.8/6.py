from abc import ABC

class Konto(ABC):
    def __init__(self, kontoNr: int = None, besitzer: str = None, kontostand: float = None, zinssatz: float = None):
        self.__kontoNr = kontoNr
        self.__besitzer = besitzer
        self._kontostand = kontostand
        self._zinssatz = zinssatz
    def get_kontoNr(self):
        return self.__kontoNr
    def get_besitzer(self):
        return self.__besitzer
    def get_kontostand(self):
        return self._kontostand
    def get_zinssatz(self):
        return self._zinssatz
    def set_kontoNr(self, kontoNr: int):
        self.__kontoNr = kontoNr
    def set_besitzer(self, besitzer: str):
        self.__besitzer = besitzer
    def set_kontostand(self, kontostand: float):
        self._kontostand = kontostand
    def set_zinssatz(self, zinssatz: float):
        self._zinssatz = zinssatz
    def einzahlen(self, val: float):
        self._kontostand += val
    def auszahlen(self, val: float):
        if self._kontostand-val>0:
            self._kontostand -= val
    def ueberzogen(self):
        if self._kontostand < 0:
            return True
        else:
            return False
    @abstractmethod
    def verrechneZinsen(self):
        pass

def Dispokonto(Konto):
    def __init__(self, kontoNr: int = None, besitzer: str = None, kontostand: float = None, zinssatz: float = None, dispokredit: float = None, dispoZinssatz: float = None):
        super().__init__(kontoNr, besitzer, kontostand, zinssatz)
        self.__dispokredit = dispokredit
        self.__dispoZinssatz = dispoZinssatz
    def get_dispokredit(self):
        return self.__dispokredit
    def get_dispoZinssatz(self):
        return self.__dispoZinssatz
    def set_dispokredit(self, dispokredit: float):
        self.__dispokredit = dispokredit
    def set_dispoZinssatz(self, dispoZinssatz: float):
        self.__dispoZinssatz = dispoZinssatz
    def verrechneDispozinsen(self):
        aktueller_dispo = 0
        if self._kontostand < 0:
            if -(self._kontostand>self.__dispokredit):
                aktueller_dispo = self.__dispokredit
            else:
                aktueller_dispo = -(self._kontostand)
            self._kontostand -= aktueller_dispo*self.__dispoZinssatz*(1/100)
    def verrechneZinsen(self):
        self._kontostand += self._kontostand*self._zinssatz*(1/100)
    def auszahlen(self, val: float):
        if self._kontostand-val>self.__dispokredit:
            self._kontostand -= val
            
def Sparkonto(Konto):
    def __init__(self, kontoNr: int = None, besitzer: str = None, kontostand: float = None, zinssatz: float = None, sparbetrag: float = None, sparZinssatz: float = None):
        super().__init__(kontoNr, besitzer, kontostand, zinssatz)
        self.__sparbetrag = sparbetrag
        self.__sparZinssatz = sparZinssatz
    def get_sparbetrag(self):
        return self.__sparbetrag
    def get_sparZinssatz(self):
        return self.__sparZinssatz
    def set_sparbetrag(self, sparbetrag: float):
        self.__sparbetrag = sparbetrag
    def set_sparZinssatz(self, sparZinssatz: float):
        self.__sparZinssatz = sparZinssatz
    def verrechneZinsen(self):
        if self._kontostand > self.__sparbetrag:
            self._kontostand += self._kontostand*self.__sparZinssatz*(1/100)
        else:
            self._kontostand += self._kontostand*self._zinssatz*(1/100)

class Girokonto(Konto):
    def __init__(self, kontoNr: int = None, besitzer: str = None, kontostand: float = None, zinssatz: float = None, kontogebuehr: float = None):
        super().__init__(kontoNr, besitzer, kontostand, zinssatz)
        self.__kontogebuehr = kontogebuehr
    def get_kontogebuehr(self):
        return self.__kontogebuehr
    def set_kontogebuehr(self, kontogebuehr: float):
        self.__kontogebuehr = kontogebuehr
    def verrechneKontogebuehr(self):
        if (self._kontostand-self.__kontogebuehr)>0:
            self._kontostand -= self.__kontogebuehr
    def verrechneZinsen(self):
        self._kontostand += self._kontostand*self._zinssatz*(1/100)