class Ampel:
    def __init__(self, zustand:str='rot', tageszeit:str='tag'):
        self.zustand = zustand
        self.tageszeit = tageszeit

    def schalten(self):
        if self.tageszeit == 'tag':
            if self.zustand == 'rot':
                self.zustand = 'rotgelb'
            elif self.zustand == 'rotgelb':
                self.zustand == 'gruen'
            elif self.zustand == 'gruen':
                self.zustand == 'rot'
        else:
            if self.zustand == 'rot':
                self.zustand = 'gelb'
            else:
                self.zustand = 'rot'

    def tageszeitWechseln(self):
        self.tageszeit = 'nacht' if self.tageszeit != 'nacht' else 'tag'

    def getLampen(self):
        if self.zustand == 'rot':
            return (True, False, False)
        elif self.zustand == 'rotgelb':
            return (True, True, False)
        elif selfzustand == 'gruen':
            return (False, False, True)
