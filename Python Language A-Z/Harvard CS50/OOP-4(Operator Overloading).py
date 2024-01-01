#Operator is like -- +, -, /, *   ---
#We know -- +  -- plus doesn't always adds mathematical terms
# It sometimes adds two strings altogether also adds two lists
# Here we will add two object made with the same class, also we will assign the addition to another object made with very same class.
# And we will do it with the special method --   __add__   --- for addition (+)
# We can overload any type of operator with special methods of their own.



class Vault:
    def __init__(self, usd, pound, bdt):
        self.usds = usd
        self.pounds = pound
        self.bdts = bdt
    
    def __str__(self):      #  __str__ is a special kind method, it gets called when the whole object is getting called , example -- print(object_name)
        return f"{self.usds} USD, {self.pounds} Pounds, {self.bdts} BDT"
    
    def __add__(self, other): # in an addition -- a + b ---  a is the first operand and b is the second operand , so here -- self -- is the first operand and -- other -- is the second operand
        usd = self.usds + other.usds
        pound = self.pounds + other.pounds  #We are adding variables of two objects here
        bdt = self.bdts + other.bdts
        
        #Now in -- return -- we will return an object (with these three total variables) of the same class, 
        return  Vault(usd, pound, bdt)



harry = Vault(20, 30, 100)
print(harry)

ron = Vault(40, 60, 50)
print(ron)

total = harry + ron #Here we are adding two objects, and how the addition operator will work, we have defined it in the class in --  __add__  -- method
                        #After the addition we have returned an object made with the same class and the total value
print(total)