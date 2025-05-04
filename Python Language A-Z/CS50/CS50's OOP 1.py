#Classes, Instance(object), Getter, Setter

class Student():                                        #Classes are generally defined before main file, but it is conventional and good practice to define classes and modules in a separate file and later import it
    def __init__(self, name, house, patronus):        #Initializes an instance(object) of the class when called, it's not constructor, initializer and constructor have two different task, one creates/constructs the object in memory, the other fills/initialized it with value... It is only called when you first create an object with this class
        if not name:                                   #This error checking was writtern before setting up the getter or setter, but the problem anyone in the main function can bypass the error checking later by overwriting the value of -- name -- and -- house --
            raise ValueError("Missing name")                #But we no longer need this error check here, because in the later line, self.house is gonna call the special getter or setter method -- house --
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house                              #It will call the special setter method -- house -- and pass the argument 
        self.patronus = patronus

    def __str__(self):          #Another special method, any time if the object is called to see as a string, like print(object_name), the special method __str__ is called automatically
        return f"{self.name} from {self.house}"
    
    #Getter                         #Explained in the next getter
    @property
    def name(self):
        return self._name           #The instance (object) variable is called "_name" but the property is called "name"

    #Setter                         #Explained in the setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


    #Getter
    @property                       #That's a decorator, that's how you set a special -- getter -- method, for the name -- house --
    def house(self):                #While accessing the value of house, this -- getter -- method is called automatically
        return self._house          #The " _house " is the actual instance(object) variable name, that is stored inside the object, as the variable name and the name of the getter or setter method will collide, it is conventional to use "_" underscore before the variable name and leave the method name as it is
    
    #Setter
    @house.setter                   #That's a decorator, that's how you set a special -- setter -- method, for the name -- house --
    def house(self, house):         #While accessing and overwriting the value of house, this -- setter method is called automatically, and what is on the right hand side of the equal sign '=' is gonna pass automatically as an argument
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    

    '''
    @classmethod                    #Class method is describe in the part 2 of this file, It is the best practice to implement encapsulation everything related to one item (in this case, student) to a class
    def get(cls):                       #So here calling the -- class method -- in the main file by -- Student.get() -- we will get the name, house of the student, and crate and return an instance(object) using the data passing it to -- Student class-- which refers to -- cls -- here
        name = input("Name: ")              #In below, we didn't get rid of get_student() function and commented this class method, because class method has not been introduced yet
        house = input("House: ")
        return cls(name, house)
    '''



    def charm(self):            #Custom method
        match self.patronus:        #Another alternative of if-else condition
            case "Stag":
                return "🦄"
            case "Otter":
                return "🐌"
            case "Jack Russel terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    student = get_student()
    #print(f"{student.name} from {student.house}")      #If special method __str__ doesn't exist inside the class
    #student.house = "Number Four, Privet Drive"        #You can always access instance(object) variable and rewrite it later, if you do not use properties like-- getters -- and -- setters -- properties inside a class, thus it will not make any sense verify the input in the __init__ method.
                                                        #While using the properties like -- setter -- or --getter -- with decorator "@" , if we try to access the student.house variable, it will automatically call the -- getter -- house method for us.
                                                        #Again while accessing an rewriting the variable of an object like -- student.house -- it will automatically call the -- setter -- method for us with name -- house -- inside tha class
    #student._house = "Number Four, Privet Drive"       #We can still change the name, Python is more of an honor system, It relies more on convention rather than constrains. The convention here is if an instance(object) variable starts with an "_" underscore, no one should touch it other than the person who created it
    print(student)      #Printing an object, in the underlying hood, it is calling the __str__ method of that object, IMPRTNT: Don't call it as calling a function, like with open and close parenthesis () -- Just call it with object name
    print(f"Expecto Patronum: {student.charm()}")   #Calling custom method from an object created from Student class


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)     #Passes the argument in the special method __init__ in the class, to create an object with it
                                                #Best practice of encapsulation, is to capsulate everything related under one class, that's why we used -- @class method -- (commented) inside the class, and get rid of -- get_student() -- function 

if __name__ == "__main__":
    main()