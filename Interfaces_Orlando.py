'''
Name: Orlando Companioni

This is where all the interfaces of the program will be.
This program will be imported by the main program.
'''
from abc import ABC, abstractmethod # ABC is the abstract base class


# This is the interface for the whole program
class Repairable(ABC): 

    @abstractmethod
    def how_to_repair(self)->str: # This is the abstract method
        pass

class PriceProvider(ABC):

    @abstractmethod
    def get_price(self)->float: # This is the abstract method
        pass

class Playable(ABC):

    @abstractmethod
    def how_to_play(self)->str: # This is the abstract method
        pass
