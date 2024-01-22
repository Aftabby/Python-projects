#Coffee Shop Software
class Starbux:
    def __init__(self):
        self.sell = 0
        self.stock = 100
        self.unit_price = 3.5

    def restock(self):
        self.stock += 50
        print("Restocked! Updated stock:", self.stock)

    def confirm_order(self, quantity):
        if self.stock < quantity:
            print("We are out of stock, we only have", self.stock, "coffee")
            self.restock()
            return
        self.sell += self.unit_price * quantity
        self.stock -= quantity
        print("Thank you for buying", quantity, "coffee" )

coffeeshop1 = Starbux()

coffeeshop1.confirm_order(10)
coffeeshop1.confirm_order(45)
coffeeshop1.confirm_order(35)
coffeeshop1.confirm_order(35)
coffeeshop1.confirm_order(5)
coffeeshop1.confirm_order(50)

print(coffeeshop1.sell, "and the stock left:", coffeeshop1.stock)







#Shopping
class Shopping:
    def __init__(self):
        self.total = 0
        self.cart = []
    
    def add_to_cart(self, item, price):
        self.cart.append(item)
        self.total += price

    def checkout(self, amount):
        if self.total != amount :
            print("No change! Please pay the exact amount.")
            return                                                  #Using the return keyword in a method
        print("Thanks for purchsing", self.cart)
        self.cart = []
        self.total = 0

customer10 = Shopping()
customer10.add_to_cart("Lichi", 50)
customer10.add_to_cart("Mango", 65)
print(customer10.cart, customer10.total)
customer10.checkout(115)





#Bank account - The minimum withdrawal from a bank account

class Bank:
    def __init__(self, initial_amount):
        self.minimum = 500
        self.balance = initial_amount
    
    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("You don't have enough balance.")
            return
        if amount >= self.minimum:
            self.balance -= amount
        else:
            print("The amount is too low to withdraw.")

account1 = Bank(5000)
print(account1.balance)     
print(account1.get_balance())        # -- client1.get_balance() --- and --- client1.balance --- will return the same value

account1.withdraw(350)
print(account1.balance)     
print(account1.get_balance())

account1.withdraw(850)
print(account1.balance)     
print(account1.get_balance())

account1.withdraw(59930)
print(account1.balance)     
print(account1.get_balance())



# Withdraw - (Practicing with problems, playing with examples)

class Bank:
    def __init__(self, balance):
        self.acc_balance = balance
    
    def get_balance(self):
        return self.acc_balance
    
    def withdraw(self, amount):
        self.acc_balance -= amount

client1 = Bank(6000)
print(client1.get_balance())   # -- client1.get_balance() --- and --- client1.acc_balance --- will return the same value
print(client1.acc_balance)

client1.withdraw(3500)          #Withdrawing client money from bank, using a method
print(client1.acc_balance)      #Showing client remaining account balance by accessing object's attribute--- object_name.attribute_name ----
print(client1.get_balance())    #Showing client remaining account balance by calling a method which returns the same attribute ---   object_name.method_name()   ----













# CONCEPT STARTED FROM HERE ----














#Instance Attribute  (A serious problem regarding class level attribute, two objects attribute value becomes same and merged, that's been solved with example)

class Shopping:
    cart = []
    def add_to_cart(self, item):
        self.cart.append(item)


customer1 = Shopping()           #cart of customer 1
customer1.add_to_cart("t-shirt")
print("customer 1 cart", customer1.cart)

customer2 = Shopping()          # cart of customer 2
customer2.add_to_cart("Shoes")
print("customer 2 cart", customer2.cart)    #customer 2 only added shoes to cart, but the print out showing both t-shirt and shoes, --- this happened because the attribute declared in the class is a --class level attribute---.
                                            # That's why both the first and second customer was using the same class level cart list
                                            # To solve this, we have to create -- cart -- attribute inside the -- constructor -- then every object from the class will have a separate -- cart -- attribute
                                            # This is called ---  Instance attribute --
class Shopping:
    def __init__(self):                    # Created the attribute inside the constructor - it will solve the -- class level attribute -- problem
        self.cart =[]
    def add_to_cart(self, item):
        self.cart.append(item)
    
customer3 = Shopping()           #cart of customer 3
customer3.add_to_cart("t-shirt")
print("customer 3 cart", customer3.cart)

customer4 = Shopping()          # cart of customer 4
customer4.add_to_cart("Shoes")
print("customer 4 cart", customer4.cart)    #Now you can see the two carts doesn't get mixed up
    

















#Declaring a Constructor
class Phone:
    def __init__(self, brand, year = 0):   # As a constructor (special type of method) the name must be--   __init__   ---
        self.brand = brand      # It creates an attribute in the object with the value of the parameter passed into class_name, while creating object
        self.bought = year    # TO create any attribute, just put-- self.attribute_name = value -- the value will be the value passed while creating object to class_name

my_phone = Phone("SamSung")   # We are initializing a value while creating an object, though class_name / class doesn't take any argument/parameter -- but as there is a constructor method in the class, the parameter will be passed to constructor - which will create attributes and set it's value a/q to it's defined
grandma_phone = Phone("Nokia 1100", 1996) # Python call automatically the __init__ method (constructor) , while creating an object--- that's why we don't need to call it directly -- Although in some advanced cases you might wanna call it

print(my_phone.brand)
print(grandma_phone.brand, grandma_phone.bought)
#------------Another Example

class Laptop:
    def __init__(self, brand):      #self is must parameter in method, you dont need to pass anything for it while calling method -- It is used to call or declare parameter of the class inside the method
        self.lappybrand = brand    #We declared a attribute lappybrand, and the brand parameter value will be passed to class_name while creating the object. the init method (constructor) is called automatically while creating object
        self.age = 10              #We declared another attribute is declared name -- age -- to declare or call any attribute of class_name inside the method use---  self.attribute_name  ---  equals to the value
    
    def age_incrmnt(self, increment):   #It's just a normal method, where self is a default argument and we will pass another argument/parameter to it named increment
        self.age += increment           #We are calling an attribute age by -- self.age -- then assigning a new value to it
    
my_laptop = Laptop("Victus")   #Though Laptop is a class_name (not a method, or function), but while we call the class_name to create an object, it automatically calls the constructor defined inside it (__init__ special method), and thus the value we passed into it goes to the constructor as parameter
my_laptop.age_incrmnt(10)      #We are calling a method, that is inside the object, and we passed the parameter 'increment' -- as the 'self' parameter is not to be passed.

print(my_laptop.lappybrand)
print(my_laptop.age)

















#Declaring a method 
class Profile:
    name = "Ronaldo"        # An attribute is a variable inside a class
    def mood(self):         #A method is a function inside a class --- The self parameter is a default parameter , which is also automatically passed by python while calling the method
        print("I'm earning a lot of Dirham, Yalla Habibi")
    
    def add(self, a, b): #Using more than the default parameter in method
        return a + b        # self --Use self parameter to access any attributes or class of that class from inside a method
        
    

ronaldo_info = Profile()
ronaldo_info.mood()  # That's how you call a method, that is -- object_name.method_name() ---

ronaldo_salary = ronaldo_info.add(50, 70) #Here the first parameter of method-- self -- is automatically passed by python , the rest two parameter -- a, b --  is used by us
print(ronaldo_salary) # ------------------- Pass all the parameter excluding -- self -- parameter, python will automatically pass the self parameter


class Player:
    name = ""
    salary = 0
    def ten_percent_off_salary(self):
        return (self.salary * 0.9)    #Using self parameter to access attribute of that class from inside the method

messi_info = Player()
messi_info.name = "Messi"
messi_info.salary = 5000

print("Messi salary: ", messi_info.salary)
print("Messi salary after 10% discount: ", messi_info.ten_percent_off_salary() )  #Calling the method, which used self parameter to call the attribute within the same class





















#Declaring a Class
class Phone:   # Here class is a KW used to declare class, and Phone is a class_name
    brand = "Samsung"     #Here brand is an attribute, attributes are just like variables that you declare inside a class --- the initial value has been set to "Samsung"


class Computer:
    ram = "8 GB"
    ssd = 512           #Declaring class with multiple attribute, with it's default value
    screen = 16.1       # Attributes can be of differtent data types
    touch = False



















#Creating an Object
my_phone = Phone()    #Creating an object from a Phone Class -- object_name = class_name()  ----

print(my_phone.brand)   # To see the attribute in the object_name (which has been created from a class_name), type ----- object_name.attribute_name ----

my_phone.brand = "Pixel"  # Accessing the the attribute of an object and setting a new value
print(my_phone.brand)

his_phone = Phone()     #The default value of an attribute that comes from class, doesn't change if you change the attribute of any other object made from that particular class
print(his_phone.brand)


my_pc = Computer()
print(my_pc.touch)














#OOP (Object Oriented Programming)
# The programming which is solely focused on objects
# Several objects will be at the heart of your code - this programming style is called Object Oriented Programming
# You will use significant numbers of objects and classes to organize elements of the program
# Three Pillars of OOP : 1. Inheritence , 2. Encapsulation, Polymorphism) {not discussed in this file}
# Alternative of OOP : 1. Functional Programming, 2. Procedural Processing { but OOP is widely used}
# USe Objects to organize elements of the program















#Instance Attribute
# In some cases(Class attributes) the object made from the same class, share same attributes_values among them, so when you update one object's attribute the other one also get updated. It is called class level attribute
# To solve this problem, we create attribute inside constructor, so that each object has separate attribute - this is called instance attribute.
# Everything is shown above with description and example -at - Instance Attribute  (A serious problem regarding class level attribute, that's been solved with example)
# Instance attribute are not shared among instances or objects created from a class -or - Instance attributes don't share data of one object with other objects














#Constructor (__init__)
# Constructor is a special type of method, it is used to provide initial values while creating class
# In python, the constructor method has to have a special name ---    __init__    ---- two underscore, then init followed by two more underscores
# The word - init - came from the word initialize - because you are initializing an object and while initializing you are providing some initial values
# As a constructor (special type of method) the name must be--   __init__   ---
# We are initializing a value while creating an object to class_name, though class_name / class doesn't take any argument/parameter -- but as there is a constructor method in the class, the parameter will be passed to constructor - which will create attributes and set it's value a/q to it's defined
# To get better idea, get a look above where we declared a constructor
# Python call automatically the __init__ method (constructor) , while creating an object --- that's why we don't need to call it directly -- Although in some advanced cases you might wanna call it
# TO create any attribute, just put-- self.attribute_name = value -- the value will be the value passed while creating object to class_name
# Everything is described above with example at - declaring a constructor
# Use __init_ method (this special method is known as Constructor) , to initialize object instance attributes









#Method
# Every function created inside a class are called a method (To remember you can call them class function -- though which is not what they are called)
# Every object created from that class can call that function or method and perform  task
# To declare a method inside a class --- def method_name(self):  ---
# To call a method, that is -- object_name.method_name() ---
# The first parameter (Also known as default or self parameter) of a method is passed automatically by python
# If you want to use 'n' number of parameter in python, declare 'n+1' number of parameter while declaring method
# The first parameter of method will be -self-, and you do not have to pass anything for - self - parameter while calling method (You can name it anything other than self, but programmers name it self)
# self -- Access everything, Use self parameter to access any attributes or method of that class from inside the method, just use --- self.attribute_name --- within the method
# Technically you can name the self parameter anything, here self means the first parameter of the method (but not recommended to name it otherwise)
# Self parameter represents the current instance of the object
# Methods are like functions













#Class
# Class is a template to create similar objects - 
# In programming, class is created - (like a template) - just to create individual objects with similar attributes
# To declare a class, use the KW ---- class Class_name:  -----
# Declaring an class has been shown above , name of class starting with a capital letter is a good practice
# You can create as much object as you want from a class











#Attributes
# Attributes are just like variables but declared inside a class
# Class attributes are declared inside the class and shared with all the objects created from the same class.
# However, instance attributes are not shared with all the objects created from the same class









#Object
# In programming everything is an object [Just like in real life, an object can be - a chair, an ice-cream, a person]
# Every object has an unique attribute or properties   [Just like in real life, every person looks different, or has different characteristics]
# -- -- Again object can have same attribute with different values [ Just like in real life, Every person has a name but the value of the name is different]
# An object may or may not perform task  [Just like in ral life, We eat food, Car drinks petrol, Chair eats nothing]
# To call an attribute from object use -- object_name.attribute_name

# Object Template - which is called class - Objects might look exactly similar if they were created using same template - or - Use a template to create similar object
# -- -- Using a template to create multiple objects - means - all the objects have same/similar attributes (tho the value might be changed later.)
# Creating an object has been shown above 
# All the objects created from a particular class will have same attribute, but the value of the attributes of the objects can be changed later







#Important Notes
# Everything has been described topic-wise above -- because that was more convenient way to do it
# List - is to use multiple variables with similar type , like grouping similar type variable
# Class - A class gives you the ability to group different type variable and functions etc together i.e - a class represents a collection of variables and functions etc
