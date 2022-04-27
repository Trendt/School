# 7.1

class Animal:
    def __init__(self, name="Tier", species="Elefant"):
        self.name = name
        self.species = species

    def describe(self):
        return ("{} ist ein {}".format(self.name, self.species))

maja = Animal("Maja", "Biene")
print(maja.describe())
print(Animal.describe(maja))

# maja.describe() --> self = self
# Animal.describe(maja) self = Maja

# 7.2

def define(self, name=None, species = None):
    self.name=name
    self.species=species

# 7.3
# ja -> fiunc(attr=value, attr2=value); self.attr, self.attr2 = attr,attr2

