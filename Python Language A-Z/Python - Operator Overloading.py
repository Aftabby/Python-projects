# Operators perform mainly mathematical operation - ( +, -, *, /, etc)
# But we can do something more with operators through operator overloading.
# Like adding two lists, concatening two strings etc
# The behaviour of an operator to have different functionalities according to the context is called operator overloading.
# In here, we will add two class with operator overloading


'''
Special methods for differenet types of operator overloading:

Addition operator -- (+) --    __add__(self, other)
Subtraction Operator --  (-)  --    __sub__(self, other)
Division Operator  --   (/)   --    __truediv__(self, other)
Floor Division Operator  --  (//)  -- __floordiv__(self, other)
Module Operator   --   (%)   ---  __mod__(self, other)

'''


#An example of using subtraction Operator Overloading
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def __sub__(self, other):                   #Special method to overload the addition operator
        
        #The new task of subtraction operator
        real = self.real - other.real         
        img = self.img - other.img

        return Complex(real, img)   #returning a class with the subtracted value of two class
    
    
    def __str__(self) -> str:
        return f"Real : {self.real}, Imaginary : {self.img}"
    
c1 = Complex(5, 10)
c2 = Complex(15, 20)

print("Subtraction is: c2 - c1 =", c2-c1)             #To perform arithmatic operation on objects from Complex class, we gotta add a special method in the Complex class block.