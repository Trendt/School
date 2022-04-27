PI = 3.14159

class Objekt3D:
    def berechneVolumen(self):
        pass
        
class GeraderZylinder(Objekt3D):
    def __init__(self, radius: float = None, hoehe: float = None):
        self._radius = radius
        self._hoehe = hoehe

    def get_radius(self):
        return self._radius

    def get_hoehe(self):
        return self._hoehe

    def set_radius(self, radius: float):
        self._radius = radius

    def set_hoehe(self, hoehe: float):
        self._hoehe = hoehe

    def berechneVolumen(self):
        return PI*(self._radius**2)*self._hoehe
    
class Kugel(Objekt3D):
    def __init__(self, radius: float = None):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius: float):
        self.__radius = radius

    def berechneVolumen(self):
        return (4/3)*PI*(self.__radius**3)

class Quader(Objekt3D):
    def __init__(self, laenge: float = None, breite: float = None, hoehe: float = None):
        self.__laenge = laenge
        self.__breite = breite
        self.__hoehe = hoehe

    def get_laenge(self):
        return self.__laenge

    def get_breite(self):
        return self.__breite

    def get_hoehe(self):
        return self.__hoehe

    def set_laenge(self, laenge: float):
        self.__laenge = laenge

    def set_breite(self, breite: float):
        self.__breite = breite

    def set_hoehe(self, hoehe: float):
        self.__hoehe = hoehe

    def berechneVolumen(self):
        return self.__laenge*self.__breite*self.__hoehe
       
class HohlZylinder(GeraderZylinder):
    def __init__(self, radius: float = None, hoehe: float = None, radiusInnen: float = None):
        super().__init__(radius, hoehe)
        self._radiusInnen = radiusInnen

    def get_radiusInnen(self):
        return self._radiusInnen

    def set_radiusInnen(self, radiusInnen: float):
        self._radiusInnen = radiusInnen

    def berechneVolumen(self):
        return super().berechneVolumen()-PI*(self._radiusInnen**2)*self._hoehe
