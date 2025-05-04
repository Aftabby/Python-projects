#Print function mainly take 3 arguments
# print(*object, sep=' ' , end="\n")
# 1st - As much object as you give, 
# 2nd - It will separate each parameter with a ' ' by default while printing
# 3rd - After every print function finishes printing there will be an end of the line i.e. \n

sentence1 = "Hello, my name is Aftab."
sentence2 = "I've been into programming \"since my childhood."  #YOu can backslash to use escape character, computer will not end the string there
sentence3 = "Adios!"
print(sentence1, sentence2)
print(sentence3)


print(sentence1, sentence2, sep = '*separator*', end = "")
print(sentence3)


#F - String / Format string - One special kind of string that tells python to format stuff in the string in a special way
print(f"Hello {sentence1}")
print("\n\n\n")
# Formatting number in a string
num = 1000000000
print(f"{num:,}")   # IT'll add comma in the number like 1,000,000

num = 10.66666666
print(f"{num:.2f}") #10.67
print(f"{num}") #10.66666666
num = round(num, 3) #10.667
print(num)





# string_name.strip() -- Removes trailing and leading whitespaces from string by default
name = input("What's your name? ")
name = name.strip()
print(name)
#Capitalizing the first letter of a string -- string_name.capitalize
name = name.capitalize()
print(name)
# Title base capitalization , capitalizing first letter of each of the word
name = name.title()
print(name)

# Split user's name into first name and last name
first, last = name.split(" ")
print(f"hello, {first}")


print("\n\n\n")




#Pythonic way to return a value with condition
    #return "This" if True else "That"
def main():
    x = int(input("What's X?: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n%2 == 0
    #return True if n%2 == 0 else False

main()






# Conditionals using "match" keyword:
def main():
    name = input("What's your name? ")

    #Just like if else conditionals using "match" keyword
    match name:
        case "Harry" | "Hermione" | "Ron":       # like (if name == "Harry" or name == "Hermione" or name == "Ron")
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:                 #Like that "else" keyword in the if-else statement
            print("Who")
    

main()





#================ Usage of Loops in Different Scenario ==================

def main():
    num = get_number()
    meow(num)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("Meow")
    
main()










#For Loops
for _ in range(3):      # When we don't use the variable name in anywhere else, but the programs need it, pythonic convention is to use an underscore (" _ ") as variable name
    print("meow")






# Using Loops with Dictionary
students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}

for student in students:    #Looping through the dictionary, for each iteration, the loop variable(student) will be the keys of the dictionary
    print(student, students[student], sep=", ")











#List of Dictionaries
#Combining list and dictionaries for larger data - Dictionary for each element of a list
students = [
    {
        "name" : "Hermione",
        "house" : "Gryffindor",
        "patronus" : "Otter"
    },
    {
        "name" : "Harry",
        "house" : "Gryffindor",
        "patronus" : "Stag"
    },
    {
        "name" : "Draco",
        "house" : "Slytherin",
        "patronus" : None
    }
]

for student in students:    #Looping through the list
    for detail in student:  #Looping through the dictionary
        print(detail, student[detail], sep=" : ")
    print("============================")







# ============== Error Handling ======================

#SyntaxError should must be fixed and it is done manually
 




#ValueError
try:                              #In the "try" block only keep the lines of code that can raise an error, rest goes elsewhere
    x = int(input("What's X?"))
except ValueError:
    print("x is not an integer")
else:                              # The "else" only gets executed if the "try" block executes perfectly without raising an error
    print(f"x is {x}")


    #Another One

def get_int():
    while True:
        try:
            return int(input("What's X?"))
        except:
            pass

x = get_int()
print(f"x is {x}")














# Standard way to put the codes
