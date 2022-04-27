from medien import *

class Datenbank:
    
    def __init__(self): 
        self.medien = []
    
    def erfasseMedium(self, med):
        self.medien.append(med)
    def auflisten(self):
        for i in range(0, len(self.medien), 1):
            self.medien[i].druckeInfo()
