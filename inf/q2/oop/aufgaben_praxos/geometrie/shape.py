import math

class Shape:
    def __init__(self):
        pass

    def circumference(self) -> float:
        pass

    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, a:float,b:float):
        self.a = a
        self.b = b

    def circumference(self) -> float:
        return 2*self.a + 2*self.b

    def area(self) -> float:
        return self.a*self.b

class Circle(Shape):
    def __init__(self, radius:float):
        self.radius = radius

    def circumference(self) -> float:
        return 2*math.pi*self.radius

    def area(self) -> float:
        return 

class Triangle(Shape):
    def __init__(self, a:float, b:float, c:float):
        self.a, self.b, self.c = a,b,c

    def circumference(self) -> float:
        return a+b+c

    def area(self) -> float:
        s=self.circumference()/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
