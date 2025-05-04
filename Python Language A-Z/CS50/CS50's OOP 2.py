#Class Method and Class variable

import random 

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]     #It's a --class variable--, all the objects made from this class, and the class itself share the same variable, other than creating it again and again for each instance (object) 
                                                                            #It's not declared as -- self.variable_name -- as of how the instance (object) variable is created
                                                                                #It's accessible to any of the function aka method in the same -- class --
    
    @classmethod                                            #It's a decorator to indicate class method, this method is shared within all the instaces(object) made with this class, as well as the class itself
    def sort(cls, name):                                        #Here, by convention, we use -- cls -- as the first parameter(argument), it refers to the same class of its own, and we don't use -- class -- instead of -- cls -- cause it'll create conflict with the keyword -- class -- itself
        print(name, "is in", random.choices(cls.houses))            # That's how to access a -- class variable -- by using -- cls.variable_name -- inside a -- class method --


                                                                    #To access a class variable inside of an instance method, use -- Class_name.class_variable -- or you could use -- self.__class__.class_variable -- (here __class__ is not a placeholder, it's literal double underscore class double underscore)




def main():
    #hat = Hat()            #That's the method we had to use before creating a -- class method -- , Now we don't need to create the instance(object) of the class anymore
    #hat.sort("Harry")
    Hat.sort("Harry")       #Accessing the -- class method -- directly with the -- class -- name without creating an instance (object)



if __name__ == "__main__":
    main()


