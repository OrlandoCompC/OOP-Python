'''
Name: Orlando Companioni
 
This is where the StringFamily class will be defined.
'''
from Instruments_Orlando import MusicalInstrument as mi
from Interfaces_Orlando import Repairable as rp , Playable as pl

class PercussionFamily(mi,rp,pl): #Parent class for Drum and Xylophone and Piano  
    def __init__(self,keys_num):
        self.keys_num=keys_num

    def getKeys_num(self):
        return f"Key count of {self.name}: {self.keys_num}"

class Drum(PercussionFamily): #drum class inherits from PercussionFamily
    #drum has extra atributte diameter_in_inch
    def __init__(self, keys_num,diameter_in_inch):
        super().__init__(keys_num)
        self.diameter_in_inch=diameter_in_inch
        self.name="Drum"
        self.price=349.50

    # overriding the abstract methods 
    def how_to_play(self) -> str:
        return f"By hitting the membrane with sticks"

    def get_price(self) -> float: #Accessor
        return f"${self.price}"
    
    def make_sound(self): 
       return f"Vibrating stretched membrane"

    def how_to_repair(self)->str:
        return f"Replace the membrane"

    
    #Accessors
    # def getSpecialFeature(self): 
    #     return f"Key count of drum: {self.keys_num}\nThe diameter of drum: {self.diameter_in_inch} inches"

    def getDiameter(self):
        return f"The diameter of drum: {self.diameter_in_inch} inches"
    
    
class Xylophone(PercussionFamily): #xylophone class inherits from PercussionFamily
    def __init__(self, keys_num):
        super().__init__(keys_num)
        self.name="Xylophone"
        self.price=49.00 # Doing this to be able to access the price later

    # overriding the abstract methods
    def how_to_play(self) -> str: 
        return f"By hitting bars with two mallets"

    def get_price(self) -> float: 
        return f"${self.price}"
    
    def make_sound(self): 
        return f"Through resonators"
    
    def how_to_repair(self)->str:
        return f"Replace the broken keys"
    
    #Accessor
    # def getSpecialFeature(self): 
    #     return f"Key count of Xylophone: {self.keys_num}"  