class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError
        
        self.name = name

#As in Harry Potter movie - both studedent and the professor is a wizard
        

class Student(Wizard):  #Here Student is the subclass of Wizard class, which means Student inherits everything from the Wizard class
                                #That means we can use every characteristics of the wizard class
                                    #Wizard is the parent of this(Student) class -- or -- Super class of this class -- And this Student class is the subclass/child class of the parent class Wizard39
    def __init__(self, name, house):
        super().__init__(name)  # -- super() -- is programmatic approach of calling the super(or parent class) class of this current class, then we called the special method of that class which is -- __init__ -- passing a argument to it -- the variable -- name --
        self.house = house
    


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")    #This line will ensure that the __init__ method of both the Student() and Wizard() class has been called
professor = Professor("Severus", "Defense Against the Dark Arts")