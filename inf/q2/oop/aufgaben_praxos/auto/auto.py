class Auto:
    def __init__(self, color:str, make:str, buildyear:int):
        self.color = color
        self.make = make
        self.buildyear = buildyear

    def get_color(self) -> str:
        return self.color

    def set_color(self, new_color:str):
        self.color = new_color

    def get_make(self) -> str:
        return self.make

    def set_make(self, new_make:str):
        self.make = new_make

    def get_buildyear(self) -> int:
        return self.buildyear

    def set_buildyear(self, new_buildyear):
        self.buildyear = new_buildyear

    def __str__(self):
        return f"{self.make}, baujahr:{self.buildyear} in farbe {self.color}"

auto = Auto("rot", "VW", 2001)

print(auto)
auto.set_make("Mercedes")
print(auto)
