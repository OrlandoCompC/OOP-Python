'''
Name: Orlando Companioni
 
This is where the woodwind family of instruments are defined.
'''
from Instruments_Orlando import MusicalInstrument as mi
from Interfaces_Orlando import Playable as pl


class WoodwindFamily(mi,pl):
    def __init__(self,made_of):
        self.made_of=made_of

    def getMadeOf(self):
        return f"The {self.name} is made of {self.made_of}"


class Flute(WoodwindFamily):
    def __init__(self):
        super().__init__(made_of="wood")
        self.name="Flute"
        self.price=74.99

    def how_to_play(self) -> str: 
        return f"By blowing into the flute"

    def get_price(self) -> float: 
        return f"${self.price}"

    def make_sound(self):
        return "Guiding a stream of air"
    
    def how_to_repair(self):
        return print("Flute can't be repaired!!")
    
    # def getSpecialFeature(self):  #Accessor
    #     return f"The Flute is made of {self.made_of}"
    