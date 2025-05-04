#name = input("What's your name?")

#file = open("name.txt", "w")
#file.write(f"{variable_name} any other info")
#file.close()       #Now you have to close the file manually



#Or you can also open the file like below - which is the best practice
#with open("names.txt", "a") as file:   #If you open a file like -- with open("file_name_in_pc", "read/write/append_mode") as variable_name:  --- then the file automatically closes when not indented, you don't have to close it manually
    #file.write(f"{name}\n")    #You don't have to close the file manually

with open("names.txt", "r") as file:
    lines = file.readlines()

for _ in lines:
    print(_, end='')
    #print(_.rstrip())  Does the same thing except it removes any trailing white space that is present in the string



# To read file 
with open("names.txt", "r") as file:
    for line in file:   #that means you can  iterate over file, and each time the loop variable will be a variable
        print(f"hello, {line.rstrip()}") 



#sorting the file - And modifying the contents of the file
names= []
with open("names.txt") as file: #By default it will read the files, that is "r"
    for line in file:
        names.append(line.rstrip())   #rstrip removes the white spaces and new line from the beginning and end of an element
    #names.sort()
    #print(names)
    
    for name in sorted(names):
        print(f"yoyo, {name}")



#sorting the file - easily
with open("names.txt") as file:
    for line in sorted(file):
        print(line.rstrip())

#---------------------------------------------------------------------------------------#
#Upper files were created of txt format, but to store multiple information that are related to each other, we use csv format

print("\n\n\n")

with open("students.csv") as file:      # access mode "r" is by default
    print(type(file))
    for line in file:
        row =line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]} {type(row)}")

# Or another way to approach
students =[]
with open("students.csv") as file:      # "r" is by default
    for line in file:
        name, house =line.rstrip().split(",")   #Unpacking the value into two variable from list
        student = {"name": name, "house": house}    #Creating a dictionary with the value name and house
        students.append(student)    #appending the dictionary of details about each student to the list named students

for student in students:
    print(f"{student['name']} is in {student['house']}")
print("\n\n\n")

#if you want it sorted
def get_key(student):
    return student["name"]

for student in sorted(students, key = get_key): #the key parameter is used when you want a sort a list whose element is dictionary, and you want the sort the list on the basis of dictionary value, the -- key -- argument takes a function #The sorted function will call every dictionary on the list and sort the list on the base of the value (function we passed to the parameter --key -- ) of -- key --
    print(f"{student['name']} is in {student['house']}")


# Or you can do the same thing in different approach - with lambda function ( a function that we won't be needing more than once, so we don't define it, rather do it with lambda in one line) 
for student in sorted(students, key = lambda each_student: each_student["name"]): #the key parameter is used when you want a sort a list whose element is dictionary, and you want the sort the list on the basis of dictionary value, the -- key -- argument takes a function #The sorted function will call every dictionary on the list and sort the list on the base of the value (function we passed to the parameter --key -- ) of -- key --
    print(f"{student['name']} is in {student['house']}")




# _--___--_-----------------------------------------------------

#Accessing the same way but with importing -- csv -- library 
import csv  #This library has functions that work with csv file

students = []
with open("students1.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:  # Now you're not itering over the file rather the reader variable, which has some of it's useful method #unpacking name and home
        students.append({"name": name, "home": home})

for student in students:
    print(f"{student['name']} is from {student['home']}")
    
# The best approach of the previous block of code
print("best approach")
students = []
with open("students1.csv") as file:
    reader = csv.DictReader(file) #in csv.dictreader -- if you swap the rows it will not output any error to the code itself
    for row in reader:      # In -- csv.DictReader(file_name) -- the file automatically takes the first row of the file as a dictionary key
        students.append(row)
    
for student in students:
    print(f"{student["name"]} is from {student["home"]}")





#--------------Writing in an CSV file ------------------

name = input("What's your name?")
home = input("What's your home?")

with open("students1.csv", "a") as file: #opening the file in append mode
    writer = csv.writer(file)
    writer.writerow([name, home])
