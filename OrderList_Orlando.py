'''
Name: Orlando Companioni
 
This is the class order module. keeps track of orders for musical instruments by different customers
'''
class Order:
    def __init__(self,o_id,customer_name):
        self.o_id=o_id
        self.customer_name=customer_name
        self.orders=[]
        self.total=0
        
    #This will add an instrument to the order
    def add_instrument(self,instrument):
        self.orders.append(instrument)
    
    #Accessors
    def getTotal_Price(self): # This method will return the total price of the order for an specific customer
        for item in self.orders:
            price=item.get_price().lstrip("$")
            self.total+=float(price)
        return self.total
    
    def getOrders(self):
        return self.orders
    
    def getId(self):
        return self.o_id
    
    def getName(self):
        return self.customer_name

    #Mutators
     #Just in case it is required to change the id of the order or the customer name
    def setId(self,o_id):
        self.o_id=o_id
    
    def setName(self,customer_name):
        self.customer_name=customer_name