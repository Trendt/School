class Medium:
    count = 0

    def __init__(self, title:str, author:str, price:float, **kwargs):
        Medium.count+=1

        self.code = 100000 + Medium.count
        self.title = title
        self.author = author
        self.price = price
        self.comment = ""
        self.arguments = kwargs

    def getCode(self) -> int:
        return self.code

    def getTitle(self) -> str:
        return self.title

    def getAuthor(self) -> str:
        return self.author

    def getPrice(self) -> float:
        return self.price

    def setPrice(self, new_price:float):
        self.price = new_price

    def setComment(self, comment:str):
        self.comment = comment

    def getComment(self) -> str:
        return self.comment

    def __repr__(self) -> str:
        string = ""
        string += f"Code: {self.code}\n"
        string += f"Title: {self.title}\n"
        string += f"Price: {self.price}€\n"
        string += f"Comment: {self.comment}\n"
        for key, value in self.arguments.items():
            string += f"{key.replace('_', ' ').capitalize()}: {value}\n"
        return string

    def __str__(self) -> str:
        return self.__repr__()

    def __dict__(self) -> dict:
        return {"code":self.code,"title":self.title, "author":self.author, "price":self.price, "comment":self.comment, "arguments":self.arguments}

class Book(Medium):
    def __init__(self, title:str, author:str, price:float, year_of_release:int):
        super().__init__(title, author, price, year_of_release=year_of_release)

class Movie(Medium):
    def __init__(self, title:str, regisseur:str, price:float, year_of_release:int, lenght_in_sec:float):
        self.year_of_release=year_of_release
        self.lenght = str(lenght_in_sec//60) + ":" + str(lenght_in_sec%60)
        
        super().__init__(title, regisseur, price, year_of_release=year_of_release, lenght=self.lenght)
