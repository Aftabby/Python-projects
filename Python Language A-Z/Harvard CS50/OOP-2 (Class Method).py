

import random

class Hat:

    #Class variable
    housesss = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]   # It is a class variable ( or property) and is shared by all the object created from this class


    #Instance Method
    def __init__(self):
        #Instance variable - In the
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] #It will be created when an object is created, and the __init__ function is called
    
    
    #Class Method (@classmethod) - It is a method that is for this specific class, no matter the valur of the property of the object
                    #It more focused on the class itself, rather than the object cretaed with itself
                    #Class method is like class variable which is shared by all the objects of that class, not differently created for each of the object made from that class, thus takes less memory
    @classmethod    #that's how you declare a class method
    def sortss(cls, name):    #As it is a class method, we used -- cls -- instead of -- self --
        houses = random.choice(cls.housesss) 
        print(f"{name} is in {houses}")


    #object method (or Instance Method) #As like class method has a decorator like, @class method , instance method has no decorator - it is by default
    #def sort(self, name):    #As it is an object method, we used self
        #house = random.choice(cls.housesss) 
        #print(f"{name} is in {house}")




# Object Method using - Below is the way to call an instance method, that comes only with object, Object method -- You gotta first create an object using that class, then use that method on that particular object
#hat = Hat()
#hat.sort("Harry")


#Class Method using - Below is the class method -- to use an class method, you don't need to create an object. It already associated with the class, so you can call it directly by calling the class
Hat.sortss("Harry")