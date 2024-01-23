# ============================================= SET ===================================
#Set - set is a data type that doesn't take any duplicate data

students = [
    {"name" : "Hermoine", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"},
    {"name" : "Padma", "house" : "Ravenclaw"}
]


#house = list()     #You can create an empty  list like that


houses = set()   #That's how you create an empty set

for student in students:
    houses.add(student["house"])        #In list you use -- list_name.append() -- in set you use -- set_name.add()  --

for house in sorted(houses):
    print(house)                # set don't take any duplicate value, so we will get each house only once.









#===========================   A programme practice of Bank and Account =========================

#If you don't understand anything here check out the OOP.py files for elaborate explanation


class Bank:
    def __init__(self):
        self._balance = 0

    #Getter
    @property               #If you don't understand anything here check out the OOP.py files in the same directory for elaborate explanation
    def balance(self):
        return self._balance
    
    #Setter
    @balance.setter                 #If you don't understand anything here check out the OOP.py files in the same directory for elaborate explanation
    def balance(self, amount):
        print("Don't try to hack my system!")

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
        


def main():
    print("\nBank System Started:'\n")
    holder1 = Bank()
    print(holder1.balance)
    holder1.deposit(5000)
    print(holder1.balance)
    holder1.withdraw(500)
    print(holder1.balance)
    holder1.balance = 10000 #It will call the setter property function, and thus the variable value will not change



if __name__ == "__main__":
    main()

print("End of Bank\n\n")




#===================================== Constant variable  ==================================


#there is no KW in python to declare constant variable
# but generally the variables which should remain constant is declared with all Capital letter (CAT = 3)
# It is an honor method of python, that when a variable name in python is all capitalized, all programmers treat it as a constant
# in the same way when a variable name starts with underscore( _ ) , that means, no one should change the value of it, " don't touch variable " other than the one who created it.
# And when a variable name starts with  double underscore ( __ ) , that means, it is a speacial type of variable built in by python developers
# It is a good practice to keep the constant value in a variable name and define it at the top of the code, rather than hardcoding the constant in the programme, so later it will be easy to find it. Like the example below



class Cat:  # By convention, the first letter of a class name should be capital
    #Class Variable (Constant Variable as the name is all capitalized, by means the other programmers will treat it as a constant, but the programme will treat it as a normal variable)
    MEOW = 4

    def meow(self):
        for _ in range(Cat.MEOW):   #As we are using a class_variable, we wrote -- Cat.meow -- if we have used an object variable we have used -- self.variable_name --
            print("Meow")



def main():
    MEOWS = 3           #Read the comments of the constant variable segment for better understanding of what happened here

    for _ in range(MEOWS):  #We did not hardcode the constant  -- 3 -- here, rather we declared a variable (which is in all caps, means it should remain constant), and put the variable here
        print("Meow")
    cat = Cat()
    cat.meow()

if __name__ == "__main__":
    main()












# =============================   Type hint  ============================

# As in python, we don't have to specify what type of data we are gonna store in a variable, just like in C language ( int variable_name = 3)
# But there is a way where you can type hints to python that what type of data to be expected in a particular variable. Though python will not do anything if you assign a different type value other than the hinted one, but you can use that hint for yourself by a package for debugging
# For that you have to instal a package, -- pip install mypy -- from terminal
# It is actually used to find out bugs, and for debugging
# Though while running the code by -- py file_name.py  -- we will not see anything in particular, other than error
# But to find that specifically, we need to run the code on mypy, that is run --  mypy file_name.py  --  in the terminal we will find there will be an error specifically mentioning where we messed up data types


def meow(n: int)-> None:   #Here we can see that -- variable_name: expected_data_type  --- is a way to find out what type of data we are expecting
                        # --   -> None    --- It is a kind of type hint for functions and methods -- means it is hinting that the function will return the KW --  None  -- though it does not affect the code in any way, but it is used for debugging, (let's say via mypy)
                        # after using the type hint for the function, you can catch any debugging error by running the code -- mypy file_name.py  -- in the terminal
                        # To use a type hint for a function return value type -- def function_name(argumet_name : argument_data_type_type_hint) -> function_return_data_type_type_hint:     --- use it like that
    for _ in range(n):
        print("meow") 

#When you don't return anything from a function, it by default return the Keyword -- None --
        

def meow_2(n : int) -> str: #it is a type hint that the parameter of this function will be expecting integer, and the function will be returning a string
    return "meow \n" * n


#Below you can remove the int() typecasting/ conversion to get a better understanding
number: int = int(input("Number : "))  #We need a number, but input function returns a string   # Here the -- number : int -- means the variable -- number -- is expecting a integer , it is for the debugging purpose 
                         #Here we can see that -- variable_name: expected_data_type  --- is a way to find out what type of data we are expecting -- number : int  ----
meow(number)
catt : str = meow(number)  #Though the function will return the KW -- None -- not a string  # Here the -- catt : str -- means the variable catt is expecting a string , it is for the debugging purpose 
print(catt) #It will print -- None --

catt : str = meow_2(number)
print(catt, end="")

#Run the program in terminal -- mypy fine_name.py ---
#It is only used to check by programmers while debugging the code mainly








# ============================    ArgParse  =======================================
#TimeStamp: 14:30:00

# IT is like the sys.argv but we can use flag (-n, -d, etc.) in the command line while running the programme.




















# ====================================   Unpack  ======================================


def money_exchange(usd, pound, bdt):
    return (usd * 110) + (100 * pound) + bdt


my_wallet = [20, 30, 70]


# The below two lines work as same, and same thing
# total = money_exchange(my_wallet[0], my_wallet[1], my_wallet[2])
total = money_exchange(*my_wallet)              # It is called unpacking, putting an asterisk sign (*) infront of the data structure list, 
                                                # we are unpacking the list based on it's total element, here the list has 3 elements, it got unpacked and each element acted as a parameter to the function money_exchange()
                                                # unpacking can also be used for dictionaries, tuples and lists as well, not for sets (set doesn't have any order)
print(total, "BDT")






my_wallet ={"usd" : 30, "pound" : 40, "bdt" : 80}

#Dictionary Unpacking
#The below two lines work as same, and same thing
#total = money_exchange(pound=40 , usd = 30, bdt = 80)       #Order doesn't matter here, as we are passing the parameter with their (name=value) format , same name as the function parameter
total = money_exchange(**my_wallet)         #In dictionary you have to put two asterist before the dictionary_name (**) , as it is passing key and value by unpacking, by the format of -- dict_key = dict_value  -- 
                                            # Must remember the key of the dictionary and the parameter (or argument) name of the dictionary should match, the order need not to match, also the total element of the dictionary should match the number of element of parameters expected by the function/method

print(total, "BDT")




#Example
hello = ["Hello", "How", "Are", "You"]
print(hello)    #It will print the list
print(*hello)   #It will unpack the list, and pass each element of the list as a parameter to the print funtion, so a sentence will be printed


















#=============================== Functions with unlimited paramters / variable no. of parameters  ====================#

# In function or method we define how many parameter (or argument) there should be
# But there is a way by which we can define we want variable numbers of parameter into a function. example - print(a,b,c) - we can pass as many argument as we want in print
# 


#Positional Argument
def f(*args):       #Here one asterisk(*) before the variable_name means, there could be any number of parameters
                    #The parameter_name could be anything, but conventional way to do so is using -- args -- short form of arguments
    print("Postional:", args)   #The args automatically become a tuple, where the elements are the arguments passed in the function - maintaining the order
                                # As the tuple args maintains the order of position of the way arguments has been passed into the function. It is called the postional argument

f(100, 200, 300)
f(500)
f(800, 900) #We can pass any number of arguments to the function -- f --






#Named / Keyword Argument
def f(**kwargs) -> None:
    print("Named: ", kwargs)       #Named argument is almost same like positional argument, there are only three difference
                                    # One: You have to put two asterisks (**) before the parameter_name while defining functions, the parameter name could be anything but the conventional way is to use --  kwargs  -- which stand for keyword arguments
                                    # One: While calling You have to pass the parameter with a name and value , example --- function_name(unit = 2, price = 130) --
                                    # Two: -- kwargs -- will be a dictionary within the function/method, where key of each element will be the name of the parameter you passed, and the value will be the value of the parameter you passed, maintaing the order

f(shirt = 500, pants = 450, kurti = 100)
f(discount = 100)




#Using both Positional Argument and Named Argument
def f(*args, **kwargs):     #It is the conventional way to define the positional argument first, and then the named argument
    ...                 # ---   ...   --- dot dot dot is another of saying the keyword -- pass --















# ============================================== map function =======================
    # map(function_name, an_iterable_variable)
    # map function takes two variable one is function (without the open and closed parenthesis, because we are just passing it not calling it), then another any data structure that is iterable type variable
    # then the map function takes each element from the list (let's say list is that iterable variable for now) and applies that parameter function for each of the element
    # and then it returns a list of all the elements that has been returned from passing the initial parameter list to the function -- example shown below


hello = ["Hello", "How", "Are", "You"]

hello_uppercase = map(str.upper, hello)  #here we will convert all the words into uppercase, and the method upper is in the -- str -- class, so str.upper ,, and we didn't put parenthesis after the str.upper because we are not calling the method, rather we are passing the function as a parameter to the map function
                                        # The map function will return a list of all the words as elements but everything in uppercase
                                        # We operate like this when we want to perform same function for every element of the list and save the return value also a list
print(*hello_uppercase)     #We are not printing a sentence here, that's why unpacked the list with an asterisk(*)



















# =======================================================  List Comprehension  =================================

hello = ["Hello", "How", "Are", "You"]

hello_uppercase = [word.upper() for word in hello]     #It will basically run the function -- word.upper() -- where word is the variable whose value iterates over the elements of the list
                                                        # Then as the return value will be saved inside a list, each return value as an element of the new list
                                                        # We operate like this when we want to perform same function for every element of the list and save the return value also a list
                                                        # Lastly all the new elements will be stored in a new list, as the comprehension is inside square bracket, which represents list


# List Comprehension With Conditional
students = [
    {"Name" : "Abdul", "Age" : 28},
    {"Name" : "Hasib", "Age" : 17},
    {"Name" : "Farin", "Age" : 22},
    {"Name" : "Zahid", "Age" : 15},
    {"Name" : "Nabib", "Age" : 19}
]

adult = [ student["Name"] for student in students if student["Age"] >= 18 ]  #There are three parts to focus on,, first -- for student in students --- just iterating over each of the dictionary_item, which are the elements of the list
                                                                            #Second, -- if student["Age"] >= 18  -- it is checking just like not condiotionals, if True going to the third step, other wise it is moving back to the first step
                                                                            # Third, -- student["Name"] -- This value is storing as an element of the new list
print(*adult)
print(adult)











# ==========================================  filter function ===================================

# The difference between map function and filter function is filter function takes only boolean value from it's parameter function
# And when it comes as True, it appends that value to the new_list as an element, if it is False, then it skips that element, and iterate over the next one
# Also, it also doesn't return the new values as a list data type like map_funcion, rather it return in filter object, which is iterable
# Thus how the filtering works

students = [
    {"Name" : "Abdul", "Age" : 28},
    {"Name" : "Hasib", "Age" : 17},
    {"Name" : "Farin", "Age" : 22},
    {"Name" : "Zahid", "Age" : 15},
    {"Name" : "Nabib", "Age" : 19}
]

def is_adult(student):
    return student["Age"] >= 18

adult_students = filter(is_adult, students) 

#sorting the elements which are dictionary type, based on it's key
adult_students = sorted(adult_students, key= lambda s: s["Name"])   # Google how to sort a dictionary via sorted function, also you have issue with lambda function, google it as well,,, Or you can skip this line, it is just sorted the elements

print(*adult_students)



















# ================================================  Dictionary Comprehension ==============================

students = ["Abdul", "Farin", "Nabib"]


adult_students = { student : "Is Adult" for student in students}    #It works just like the list comprehension,
                                                                    # Here first part, -- for student in students -- just like normal loop, and for every iteration it will go to the next step
                                                                    # Second part, a dictionary element will be created , from the part -- student : "Is adult"
                                                                    # Lastly, a new dictionary will be created with all the new -- key:value -- pairs as element, as this comprehension is inside curly braces, which represents a dictionary

print(adult_students)



















# =======================================================  Enumerate function  ======================================

# Enumerate takes in an iterable_item (list, tuple etc) and returns two value, first one is the index number and the second one is the value of that index positioned element.
# It returns an enumerate object, where each of the element has two value, (index_number , value_of_that_index_positon), and each element is in tuple data type


alphabets = [ "a", "b", "c", "d", "e"]

print(*enumerate(alphabets))

for serial, alphabet in enumerate(alphabets):
    print(serial+1, alphabet)




















# ========================================   Generators    ===================================
    
# The keyword used for generator is -- yield  ---
# As sometimes we need to return a massive amount of data from a function, which puts too much pressure on memory
# And we can't return the massive value partially as if we return a value we are already out of the function

# That's why we use the keyword -- yield -- as it returns the value from a function to the main function, part by part (not taking too much memory at a time), 
                    #at the same time unlike return it doesn't quit the function immediately once called
    


# THe best practice is to use every thing in different function, and keep the main function clean, just getting the value in main function, it is the conventional way. Also, it helps in unit test debugging
    

def main() -> None:
    n = int(input("What is n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield " 🐑 " * i       # if we have created an empty list and appended all the value and then returned it into the main function, that would work if n= smaller value, if n is 1 million the programmer will crush
                                # That's why we use yield to return partial value at a time.
        


if __name__ == "__main__":
    main()


