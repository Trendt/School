class Ampel(object):
    def __init__(self, anfangszustand:str='rot'):
        self.zustand = anfangszustand

    def setZustand(self, anfangszustand):
        self.zustand = anfangszustand

    def schalten(self):
        if self.zustand == 'rot':
            self.zustand = 'rotgelb'
        elif self.zustand == 'rotgelb':
            self.zustand = 'gruen'
        else:
            self.zustand = 'rot'

    def getLampen(self):
        if self.zustand == 'rot':
            lampen = (True, False, False)
        elif self.zustand == 'rotgelb':
            lampen = (True, True, False)
        else:
            lampen = (False, False, True)
        return lampen

ampel = Ampel('rot')

