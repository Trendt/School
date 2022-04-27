from math import sqrt

class Point:
    def __init__(self, x:int, y:int):
        self.x, self.y = x,y
    

class Line:
    def __init__(self, p1:Point, p2:Point):
        self.p1, self.p2 = p1, p2

    def calcLen(self) -> float:
        return sqrt(abs(p1.x-p2.x)**2 + abs(p1.y-p2.y)**2)


p1 = Point(1,6)
p2 = Point(3,4)
l1 = Line(p1, p2)

print(l1.calcLen())
