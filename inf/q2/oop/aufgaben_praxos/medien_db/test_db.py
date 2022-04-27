from datenbank import * 
from medien import *
db = Datenbank()
db.erfasseMedium(Buch("Python 3", "Heiko Kalista", "Hanser", 2018, 32.00)) 
db.erfasseMedium(CD("Disintegration (Remastered)", "The Cure", 12, 72, 15.99))
db.erfasseMedium(Video("X-Men", "Bryan Singer", 100, 21.95)) 
db.erfasseMedium(Kasette("teast", "autoorrrr", 2619, 22.69))
db.auflisten()
