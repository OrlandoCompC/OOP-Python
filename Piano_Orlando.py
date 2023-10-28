'''
Name: Orlando Companioni
 
This is where the class piano will be defined
It inherits from two classes at the same time
'''
from PercussionFamily_Orlando import PercussionFamily as pm
from StringFamily_Orlando import StringFamily as sf

class Piano(pm, sf):#multiple inheritance
    def __init__(self, keys_num,string_num):
        super().__init__(keys_num) # this is attributed to pm
        sf.__init__(self,string_num) # this is attributed to sf
        self.name="Piano"
        self.price=725.00

    # overriding the abstract methods
    def how_to_play(self) -> str:
        return f"By hitting the keys that trigger hammers to hit the strings"

    def get_price(self) -> float:
        return f"${self.price}"
    
    def make_sound(self):
        return f"Vibrating the soundboard"
    
    def how_to_repair(self)->str:
        return f"Replace the broken strings or keys"
     
    #Accessors
    # def getSpecialFeature(self): 
    #     return f"String count of Piano: {self.string_num}\nKey count of Piano: {self.keys_num}"
    
    # def getKey(self): 
    #     return self.keys_num
    
    # def getString(self): #Accessor
    #     return self.string_num