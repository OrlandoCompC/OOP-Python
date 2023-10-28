'''
Name: Orlando Companioni
 
This is where the StringFamily class will be defined.
'''
from Instruments_Orlando import MusicalInstrument as mi
from Interfaces_Orlando import Repairable as rp , Playable as pl

class StringFamily(mi,rp, pl): #Parent class for Violin, Harp and Piano
    def __init__(self, string_num):
        self.string_num=string_num

    def getString_num(self):
        return f"String count of {self.name}: {self.string_num}"

class Violin(StringFamily):
    def __init__(self, string_num):
        super().__init__(string_num)
        self.name="Violin"
        self.price=350.00
        
    # overriding the abstract methods
    def how_to_play(self) -> str:
        return f"By resting the violin on shoulder, plucking the strings bow and picking notes with fingers"

    def get_price(self) -> float:
        return f"${self.price}"
    
    def make_sound(self):
        return f"Vibrating strings"
    
    def how_to_repair(self)->str:
        return f"Replace the broken bridge"
    
    # def getSpecialFeature(self): #Accessor
    #     return f"String count of Violin: {self.string_num}"

class Harp(StringFamily):
    def __init__(self, string_num):
        super().__init__(string_num)
        self.name="Harp"
        self.price=255.00

    # overriding the abstract methods
    def how_to_play(self) -> str: 
        return f"By strumming the strings and peddling to adjust the string lengths"

    def get_price(self) -> float: 
        return f"${self.price}"
    
    def make_sound(self):
        return f"Vibrating strings"
    
    def how_to_repair(self)->str:
        return f"Replace the broken strings"
    
    # def getSpecialFeature(self): #Accessor
    #     return f"String count of Harp: {self.string_num}"


