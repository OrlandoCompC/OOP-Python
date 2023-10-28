'''
Name: Orlando Companioni
 
Here I will tests the implementation of the the program 
'''

#Import the classes
from StringFamily_Orlando import StringFamily,Violin,Harp
from PercussionFamily_Orlando import PercussionFamily,Drum,Xylophone
from WoodwindFamily_Orlando import WoodwindFamily,Flute
from Piano_Orlando import Piano
from OrderList_Orlando import Order


#Create objects
#These objects are global so that they are accessible for all functions
drum=Drum(0,20) #create a drum object with 0 keys and a diameter of 20 inches
flute=Flute()
harp=Harp(40)
piano=Piano(88,230)
violin=Violin(4)
xylophone=Xylophone(25)
instrument_to_print=[drum,flute,harp,piano,violin,xylophone] #List of all the instruments that we have

def main(): # This main function will act as the controller
    process()

def process(): # This is the process function that will call all the other functions
    inst_details()
    special_features()
    sorted()
    order_Created()
    custom_order()

def inst_details():
    #Test the methods
    # List of instruments to print in order of the assignment output   
    # instrument_to_print=[drum,flute,harp,piano,violin,xylophone] 
    
    for inst in instrument_to_print:
        if not isinstance(inst,Flute):
            print(f"\033[1;44m\n---------------Details of {inst.getName()}-----------------------\033[0;0m")
            print(f"Makes sound: {inst.make_sound()}")
            print(f"Play method: {inst.how_to_play()}")
            print(f"Repair method: {inst.how_to_repair()}")
            print(f"The price: {inst.get_price()}")
        else:
            print(f"\033[1;44m\n---------------Details of Flute-----------------------\033[0;0m")
            print(f"Makes sound: {inst.make_sound()}")
            print(f"Play method: {inst.how_to_play()}")
            print(f"The price: {inst.get_price()}")

def special_features():
    print("\033[1;44m\n-----------------SPECIAL FEATURES-----------------------\033[0;0m")

    # List of instruments to print in order of the assignment output
    # instrument_List=[xylophone,drum,harp,piano,flute,violin]
    for inst in instrument_to_print:
        if isinstance(inst,StringFamily) and not isinstance(inst,Piano): # This is to make sure not to double print piano
            print(inst.getString_num())
        elif isinstance(inst,PercussionFamily) and not isinstance(inst,Piano):
            if isinstance(inst,Drum):
                print(inst.getDiameter())
                print(inst.getKeys_num())
            else:
                print(inst.getKeys_num())
        elif isinstance(inst,WoodwindFamily):
            print(inst.getMadeOf())
        elif isinstance(inst,Piano):
            print(inst.getString_num())
            print(inst.getKeys_num())
    # # sorted(instrument_to_print)
    
def sorted():
    # List of instruments to print in order of the assignment output
    instrument_to_print.sort()
    print("\033[1;44m\n-----------------SORTED INSTRUMENTS-----------------------\033[0;0m")
    for inst in instrument_to_print:
        print(f"{inst.getName()} price: {inst.get_price()}")
        
def order_Created():
    #Create an order
    print("\033[1;44m\n---------------------ORDERS-------------------------\033[0;0m")
    order_Bob = Order(111, 'Bob')
    order_Alice = Order(222, 'Alice')
    # percussion_instruments=[drum,xylophone,piano]
    # stringINstruments=[violin,harp,piano]

    for instrument in instrument_to_print:
        if isinstance(instrument,PercussionFamily)and not isinstance(instrument,Piano):
            order_Bob.add_instrument(instrument)
        elif isinstance(instrument,StringFamily) and not isinstance(instrument,Piano):
            order_Alice.add_instrument(instrument)
        elif isinstance(instrument,Piano):
            order_Alice.add_instrument(instrument)
            order_Bob.add_instrument(instrument)


    # for intrument in percussion_instruments:
    #     order_Bob.add_instrument(intrument)

    # for instrument in stringINstruments:
    #     order_Alice.add_instrument(instrument)

    bob_total=order_Bob.getTotal_Price()
    # for item in order_Bob.getOrders():
    #     price=item.get_price().lstrip("$")
    #     bob_total=bob_total+float(price)
    print(f"Order Bob total: {bob_total}")

    alice_total=order_Alice.getTotal_Price()
    # for item in order_Alice.getOrders():
    #     price=item.get_price().lstrip("$")
    #     alice_total=alice_total+float(price)
    print(f"Order Alice total: {alice_total}")


def custom_order(): # This function has the custom order functionallity
    print(f"\033[1;44m\n-----------------CUSTOM ORDERS-----------------------\033[0;0m")
    order_Orlando=Order("087","Orlando") # it will not allow me to use 087 as an int so i used a string
    print("Please enter your order by typing the letter for each instrument without any spaces")
    print("\033[1;32md=Drum, f=Flute, h=Harp, p=Piano, v=Violin, x=Xylophone\033[0;0m")
    order=input("\033[1;34mEnter your order:  ").lower()
    for letter in order:
        if letter=="d":
            order_Orlando.add_instrument(drum)
        elif letter=="f":
            order_Orlando.add_instrument(flute)
        elif letter=="h":
            order_Orlando.add_instrument(harp)
        elif letter=="p":
            order_Orlando.add_instrument(piano)
        elif letter=="v":
            order_Orlando.add_instrument(violin)
        elif letter=="x":
            order_Orlando.add_instrument(xylophone)
        else:
            print("Invalid input")
    
    # orlando_total=0.0
    # for item in order_Orlando.getOrders():
    #     # orderlist.append(item.getName())
    #     price=item.get_price().lstrip("$") #This will remove the $ sign from the price
    #     orlando_total=orlando_total+float(price) #This will add the price to the total
    total = order_Orlando.getTotal_Price()
    if order_Orlando.getOrders()==[]:
        print("\033[1;34mNo instruments were ordered\033[0;0m")
        print(f"\033[1;34mOrder total for {order_Orlando.getName()}: 0\033[0;0m")
    else:
        print(f"\033[1;34mThe order of {order_Orlando.getName()} is: {[item.getName() for item in order_Orlando.getOrders()]}\033[0;0m")
        # print(f"\033[1;34mOrder total for {order_Orlando.getName()}: {orlando_total}\033[0;0m")
        print(f"\033[1;34mOrder total for {order_Orlando.getName()}: {total}\033[0;0m")

try:
    if __name__=="__main__":
        main()
except KeyboardInterrupt:
    print("Program terminated by user") #This will catch a keyboard interrupt and print a message
