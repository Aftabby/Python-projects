'''     Till 12:28:00     '''

class Student:
    def __init__(self, name, house): #instance method, the __init__ initializes or only called when the object is creating
        if not name:
            raise ValueError("Name Missing.")   #--raise -- is just another kind of KW to raise an error, so that you can later try & except handle it.
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")

        self.name = name    #Here -- self -- is the object that just created
        self.house = house  #But here the property(or variable) is not the name or the house, rather it calls the name and house method, which is below, (getter/property & setter)
    
    def __str__(self):  #A special kind of string that makes the object (while creating from the class) like an string while accessed from outside, like -- print(object_name) -- 
        #return "a student" #Comment it off, just to get the idea
        return f"{self.name} from {self.house}"


    #Getter
    @property   #Is telling the python to work the below method as a getter, that is, when the variable will be called from outside(which must be the same name as the method), it will run the method and return the value from the method, that prevents direct accessing of the variable
    def house(self):    #THough you can access the variable very easily, but the conventional way to do is - when you access or modify a variable you do it through a method
        return self._house   #Name the method, here --- house --- exactly like the property (or variable)

#Imp : Here actually the parameter name is ---  _house  --- , as we can't have same name for both the method and variable. but when we call object_name.house or self.house , we are actually calling either the getter or the setter (depending upon if we want to set a new value or jest get the value), and in the method the new value is assigned in the --   _house  --- variable (or property)

    #Setter
    @house.setter   #It is telling the python to work the below method as a setter of the the property (or variable) which is the same name as the -- house -- variable name is _house, method name is house, and setter name is @house.setter, you can only set setter, after you set getter -- it is called python decorator. 
    def house(self, new_house):     #THough you can access the variable very easily, but the conventional way to do is - when you access or modify a variable you do it through a method, so that we can run a block of code to check if the new value is valid or not
        # Whenever anyone will try to change the value of the property (or variable ) -- house -- the method will automatically be called, from the main() function or the first time from __init__() method, each and every time.
        # The second parameter ( new_house ) will be the value after the assignment operator while assigning a new value to the property(or variable) -- house --
        if new_house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = new_house

     
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError
        self._name = new_name


    @classmethod    #This is a class method, we can call the class method without creating an object - TO know more detail about the class read the -- OOP-2.py -- in the same directory
    def get(cls):
        name = input("Enter name: ")
        house = input("Enter house: ")  
        return cls(name,house)      #Here cls is the class itself, so it is returning an object from the very class Student itself,,, it means cls(name, house) is equals to Student(name, house)
                                    # -- self -- it the object itself and -- cls -- is the class itself
        
    
    



 
def main():
    #student = get_student()    #Using the function we are getting the details of the student. More conventional way to do is, all the methods, variable needed just for student should be inside a class - SO we will use a -- class method -- here
    
    #Usine a -- class method -- details is in OOP-2.py - file
    student = Student.get()     #That's how you call class method (it is not an object method(instance method))

    #print(f"{student.name} is from {student.house}")

    #WE can change the attribute by accessing the object variable from here, but it actually triggering a method -- house -- from @house.setter -- the actual object variable is --  _house  ---
    student.house = "Slytherin"

    print(student)  #When we try to access the whole object, it runs a special method from the object called __str__  ;; See the class definition above for more info




def get_student():
    name = input("Name: ")
    house = input("House: ")

    student = Student(name, house)      #Constructor call to create an object called -- student -- from Student class --
    return student



if __name__ == "__main__":
    main()