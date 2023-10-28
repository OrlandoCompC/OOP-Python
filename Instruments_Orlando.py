'''
Name: Orlando Companioni

This is where the MusicalInstrument class will be defined.
In class you stated that it was ok to have this inherit the Playable and PriceProvider interfaces.
'''
from abc import ABC, abstractmethod
from Interfaces_Orlando import PriceProvider

class MusicalInstrument(PriceProvider, ABC): #Parent class for all instruments

    def __ge__(self, __o):
        if not isinstance(__o, MusicalInstrument):
            raise ValueError ('Not the same type....')
        return self.price >= __o.price
    
    def __lt__(self, __o):
        if not isinstance(__o, MusicalInstrument):
            raise ValueError ('Not the same type....')
        return self.price < __o.price

    
    def getName(self): #This is to get the name of the instrument when needed
        return self.name
    
    @abstractmethod
    def make_sound(self): # abstractmethod will not have any implementation in abstract class
        pass
    
    
    
    

