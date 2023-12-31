'''     Till 11:28:00     '''

class Student:
    def __init__(self, name, house): #instance method, it initializes the object while creating
        if not name:
            raise ValueError("Name Missing.")   #--raise -- is just another kind of KW to raise an error, so that you can later try & except handle it.
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")

        self.name = name    #Here -- self -- is the object that just created
        self.house = house
    
    def __str__(self):  #A special kind of string that makes the object (while creating from the class) like an string while accessed from outside, like -- print(object_name) -- 
        #return "a student" #Comment it off, just to get the idea
        return f"{self.name} from {self.house}"

     



 
def main():
    student = get_student()
    #print(f"{student.name} is from {student.house}")
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")

    student = Student(name, house)      #Constructor call to create an object called -- student -- from Student class --
    return student

if __name__ == "__main__":
    main()