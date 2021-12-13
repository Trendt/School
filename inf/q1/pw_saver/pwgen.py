from string import ascii_letters, punctuation, digits
from random import choice

class PWGen:
    def __init__(self):
        pass
    
    def generate_pw(self, length:int=16, symbols:str=ascii_letters+punctuation+digits) -> str:
        symbols = "".join(set(symbols)) #no duplicates
        return "".join([choice(symbols) for _ in range(length)])