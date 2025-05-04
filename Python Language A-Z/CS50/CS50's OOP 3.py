#Inheritance

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name!")
        self.name = name

class Student(Wizard):                  #Here, the -- Student -- inherits from (or) the sub-class of the class -- Wizard -- (or) the --Wizard -- class is the superclass of the -- Student -- class
    def __init__(self, name, house):
        super().__init__(name)          #By calling -- super() -- a child class can access all the functionality(methods, variable, etc.) of its parent class
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)              #All the student and teachers are also wizards, so we don't need to do the error checking twice for their name, rather we did in the -- Wizard -- class and inherited that class to the -- Student -- and -- Professor -- class
        self.house = subject

def main():
    wizard = Wizard("Albus")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Severus", "Defense Against the Dark Arts")

if __name__ == "__main__":
    pass