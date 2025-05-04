#Polymorphism
class Car:
    car_name = "Prius"
    def move(self):
        print(self.car_name + " is moving.")
    
class Truck:
    truck_name = "Hino"
    def move(self):
        print(self.truck_name + " is moving.")
    
class Bike:
    bike_name = "Gixxer"
    def move(self):
        print(self.bike_name + " is moving.")


vehicles = [Car(), Truck(), Bike()]
for vehicle in vehicles:    
    vehicle.move()          #The move method taking many form here, based on the class it's on, it calls the right method in the right class
                            # This is polymorphism - Theory concept described below












#Encapsulation
class Bank:
    def __init__(self, name, deposit):
        self.name = name
        self.__balance = deposit    # When we create any attribute name that starts with two underscores, it becomes encapsulated. Thus we can't access it from outside the class
    
    def get_balance(self):
        return self.__balance   #Returning an encapsulated attribute, by accessing it from inside the class


account1 = Bank("Aftab", 5000)
print(account1.name)
# print(account1.__balance)       #This line will show error if you unComment it - because you can't access an encapsulated attribute
print(account1.get_balance())   #However you can access the encapsualted attribute from inside





























#Nested Inheritance
class A:
    def call_me(self):
        print("I am A")

class B:
    def call_me(self):
        print("I am B")
        A.call_me(self) # While calling a -- parent class -- from a -- child class -- must include the parameter -- self --

class C:
    def call_me(self):
       print("I am C")  #First we are printing -- I am C --
       B.call_me(self) # Then we calling B -- call_me -- method, and then in that method, it is printing " I am B" and then the B class calling the method -- call_me -- from A an it's printing from "I am A"
       A.call_me(self)  #Now we are directly calling a -- call_me -- method which is in -- A -- class. And the class -- A -- is not inherited directly in class -- C -- but it is nested inherited


caller = C()
caller.call_me()











#Multiple Inheritance
class Student:
    good_student = 0
    good_athelete = True

    def __init__(self, student_name, id):   #We will pass -- student_name, id -- while creating object from -- Student -- class. It's a constructor, constructor calls --  __init__ -- function automatically upon creating an object
        self.name = student_name    #We will be creating two attribute -- name , id -- while creating object 
        self.id = id
    
    def get_Id(self):    #Just a method to get student id
        return self.id      #It'll return the -- id -- attribute value of the class

class Athelete:
    def __init__(self, sports):
        self.sport = sports
    
    def get_sport(self):
        return self.sport

class Person(Student, Athelete):    #Creating multiple inheritance that is inheriting from multiple parents, the child class is -- Person -- and the two parents are -- Student , Athelete -- write -- 
    def __init__(self, name, id, sports):
        Student.__init__(self, name, id)    #Inheriting and creating attribute of -- Student -- class from -- Person -- class. While creating an attribute or calling a method, that is present at parent class, inside the child class write -- Parentclass1.method_name(parameter1, parameter2) -- or -- Parentclass1.attribute_name = value --
        Athelete.__init__(self, sports)     # While calling a -- parent class -- from another -- child class -- must pass the parameter -- self -- as the first parameter.

    Student.good_student = False        #You can access anytime the -- Parent_class -- from the -- Child_class by writing -- Parent_class.attribute -- or -- Parent_class.method(parameter1, parameter2) --

human1 = Person("Harry Potter", 3553, "magic")
print(human1.name)          #Calling an attribute that is not present at -- Person -- class, but it is present at -- Student -- class and it got inherited
print(human1.id)
print(human1.sport)
print(human1.good_student)
print(human1.good_athelete)









# Inheritance Declaration
class Phone:
    video_call = True
    def __init__(self, phone_brand, phone_price): #Constructor and Instance Attribute
        self.brand = phone_brand        #Declaring attribute brand and price, the value will be the parameter passed through the class while declaring object
        self.price = phone_price

    def recharge(self):
        print("Hello I am recharging")
        print ("My battery will be full soon")

class Watch:
    video_call = False          #Declaring class level attribute
    def __init__(self, watch_brand, price):
        self.brand = watch_brand
        self.price = price
    
    def recharge(self):             #In both the class the recharge method is same
        print("Hello I am recharging")
        print ("My battery will be full soon")

my_watch = Watch("Casio", 1250)
print(my_watch.brand)
my_watch.recharge()

#As in both the method the recharge() method is same - we can create a class with the common method/s and use it to the other classes (as a parameter while declaring) which needs it, and the methods will be inherited upon calling - see below for better understanding

class SmartDevice:              #It was the common part, so we declared a class for the common method
    def recharge(self):
        print("Hello I am recharging")
        print ("My battery will be full soon")


#NOw we will pass the the common method class as a parameter to those two classes

class Phone(SmartDevice): #We declared the Phone class, but as a parameter we passed SmartDevice class, and thus Phone class will inherit all the feature of SmartDevice class
    video_call = True
    def __init__(self, brand, phone_price):
        self.brand = brand
        self.price = phone_price
    
class Watch(SmartDevice): #Same as before, -- Watch -- class will now inherit the property(attributes and methods) of -- SmartDevice -- class
    video_call = False
    def __init__(self, watch_brand, price):
        self.brand = watch_brand
        self.price = price
    
# When we will call the --recharge -- method to an object which is made from -- Watch -- class, Python will look into -- Watch -- class, if it don't get it there it'll look into -- SmartDevice -- class and will find it. And thus the method was inherited to -- Watch -- class from -- SmartDevice -- class

my_phone = Phone("Pixel", 12500)
my_watch = Watch("Naruto", 3300)

print(my_phone.brand)
print(my_watch.brand)

my_watch.recharge()  #Here the recharge method still worked though it is not in the -- Watch -- class (the class from where my_watch object was created), because the recharge method was inherited from the -- SmartDevice -- class
                        #Python first looked into -- Watch -- class and then looked into --SmartDevice -- class and found the method
                        #Similarly you can make the -- Phone -- class inherit its attribute from the -- SmartDevice -- class












#Polymorphism
# When the code can take many forms it's called polymorphism
# The word 'poly' means many. And 'morph' means a change of shape
# Polymorphism is a higher level concept, might take several months to understand it.
# It means many forms



















#Encapsulation (Private attributes)
# Remember it from the word 'capsule' , which means to protect something / encapsulate something. In coding if we protect some sensitive information, so that others can't access or modify it - is called encapsulation
# While creating a class, if you create an attribute that starts with two underscores --  __attribute_name  -- that attribute becomes private. You can't access it from outside
# Example shown above

















#Inheritance
# Inheriting from others is called inheritance ( like son inherits the property after the dad dies)
# We use Inheritance if we wanna add the feature of a class (attributes, methods) to another class
# Suppose we have 3 class, a , b, and c -- now a and b has d,e,f methods common (present in both of the class), In this case we declare these methods in -- c -- class, and when needed -- a -- and -- b -- will inherit the methods from c, so that we don't have to write the same common thing again and again to every class 
# Now while declaring -- a -- class, we will use -- class a(c): -- thus while calling the methods that is present in -- c -- from object made from -- a -- class. Pythons first looks for the method in -- a -- , and then goes to -- c -- and finds it in class -- c -- then calls the method (as we passed -- c -- class as a parameter while declaring class -- a --)
# Thus the method inherited to -- a -- class from -- c -- class . This is why it is called inheritance
# The class you inherit from is called the parent class /base class. And the class that is inheriting is called the child class / derived class. Just remember, you are deriving the child class from the base class (parent class)
# Inheritance organizes coding
# Above in --  Inheritance Declaration -- everything is described with examples

# Multiple Inheritance - Sometimes, one class can inherit attributes/methods from multiple parent_class. Just pass the parent classes as parameter while declaring child class --- class ChildClass(ParentClass1, ParentClass2):  --- Just like it - Example shown above
# Inheriting and creating attribute of -- Parent_class_name -- class from -- Child_class_name -- class. While creating an attribute or calling a method, inside the child class, that is present at parent class,  write -- Parentclass1.method_name(parameter1, parameter2) -- or -- Parentclass1.attribute_name = value --
# To inherit multiple classes, pass them all to the child_class
# While calling a -- parent class -- from another -- child class -- must pass the parameter -- self -- as the first parameter.

# Nested Inheritance - Three or more level of inheritance is called nested inheritance. For example, -- class_c -- inherits -- class_B -- and -- class_B -- inherits -- class_A -- A proper practical example shown above
# Why Nesting? - It saves multiple layers of repeating attributes. For a large application you'll have several levels of inheritance

# Combined Inheritance - You can create both multiple, single and nested inheritance at a time. -- Class_A, Class_B, Class_C(Class_A, ClassB) {mulltiple inheritance}, Class_D(Class_C) {Nested Inheritance} 
# Inheritance creates a very powerful structure



