import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"Vecotr({self.x}, {self.y}, {self.z})"

    def __add__(self, v:Vector) -> Vector:
        return Vector(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, v:Vector) -> Vector:
        return Vector(self.x - v.x, self.y - v.y, self.z - v.z)

    def __mul__(self, v:Vector) -> Vector:
            
