from medium import *
import json

class Database:
    def __init__(self, file:str):
        self.file = file
        self.data = {}
        self.readData()

    def readData(self):
        pass
        

    def addMedium(self, medium:Medium):
        if type(medium).__name__ in self.data.keys():
            self.data[type(medium).__name__].append(medium.__dict__())
        else:
            self.data[type(medium).__name__] = [medium.__dict__(),]

        print(self.data)
        self.writeData()

    def writeData(self):
        json_object = json.dumps(self.data, indent=4)
        
        with open(self.file, "w") as fo:
            fo.write(json_object)

d = Database("db.json")
b = Book("a","author", 22.99, 1905)
d.addMedium(b)
print(d.data)
