      # # # # ALL ABOUT LIST # # #

#Two lists, one of number and another of strings
myFirstList = [ 16, 20, 45, 67, 33, 45, 252]
mySecondList = [ "one", "two" , "three", "four", "fourty Nine"]

#Adding a value at the last of the list
myFirstList.append(5)
mySecondList.append("five")

#printing a list with all elements inside it - remove # from next two lines
#print(myFirstList)
#print(mySecondList)

#removing a value from the value, for two or more same value, it will remove only the first one
myFirstList.remove(45)

# Getting the index number of a list element
index_count = mySecondList.index("three")

# To replace any element of list by index number
mySecondList[3] = "six"

# To find the value by index number of a list - listName[startIndex:endIndex]
justAVariable = mySecondList[2]
justAVariable2 = mySecondList[2:]
justAVariable3 = mySecondList[1:3]
justAVariable3 = mySecondList[:3]

#to find out the total number of elements in a list, (last index number + 1)
numOfElements = len(mySecondList)

#the minimum value from a list
minValue1 = min(mySecondList)
minValue0 = min(myFirstList)

#the maximum value from a list
maxValue1 = max(mySecondList)
maxValue0 = max(myFirstList)

#TO check if an element exists in the list or not, output in boolean type variable
doesExist = "three" in mySecondList
doesExist0 = 53 in myFirstList

#Adding two lists together, the new lists will be the combination of all the elements respectively
addedList = myFirstList + mySecondList + myFirstList

#Remove the of the list
mySecondList.pop() #By default it will remove the last element of the list
mySecondList.pop(2)  # To remove an element by index number, pass the index number as an argument of pop function

#Sorting a list, within that list - organize the elements of a list in ascending order
myFirstList.sort()
mySecondList.sort()

#Reversing all elements order of a lists - first element in last and last one in first
myFirstList.reverse()
mySecondList.reverse()

#Finding out a range of Numbers - range(start, stop) - by default start is 0 
anotherTemp = range(8)
anotherTemp1 = range( 9, 17)

#TEst
#print(justAVariable)
#print(justAVariable3)

#queries  and Important Notes
#how to determine which string is greater than one another?
#What the range(start, stop) function return?
# YOU  CAN PUT NUMBER & STRING TYPE VALUE IN THE SAME LIST, BUT THEN YOU CAN'T COMPARE THEM FOR MIN OR MAX


#-------------------------------------------------------------------------------------------------------------

# # # --------------------------ALL About Loops ------------------------ # #  #

#To do something with each element of the list run for loop
#To run a loop based on condition run while loop

#For LOOP
basket = ["Apple", "Orange", "Strawberry", "Banana"]
#here fruit is a loop variable - the value of this variable will be each element in the list,, in every iteration the value will be changing from the first element of the list to the last element -- 
# 'in' is a keyword just to check if the statement is true that the loop variable value contains among the list elements --
# the last word before colon is the name of the list variable on which you want to run the for loop -- 
# the colon and the indentation is mandatory in python
# For every iteration the elements will of the loop will be assigned to the loop variable respectively with index number, and the tasks under loop (indenation code) will perform its action
for fruit in basket:
    print("Fresh " + fruit)


# New Example of for loops
numList = [ 15, 54, -34, 22, 66, 106, 19, 67, 143]

for num in numList:
    if num > 55:
        break
    if num % 2 == 0:
        continue
    print(num)




#While LOOPS
print("While loop Started")

# Declare a loop variable 
# -- Write the while KW 
# -- Add a stopping condition after the while 
# -- Underneath while, write the repeating work 
# -- Update the loop variable
count = 0
while count < 5:
    print(count)
    count = count + 1

#while loop examples & practices
count = 0
sum = 0
while count <= 10:
    sum = sum + count
    count = count + 1

print(sum)

sum = 0
count = 0
while count < 50:
    if count % 2 == 0:
        count = count + 1 
        continue
    sum = count + sum
    count += 1 #count += 1 is count = count + 1
print(sum)


#-------------------------------------------------------------------------------------------------------------

# # # --------------------------ALL About Functions ------------------------ # #  #

print("Function Started")

#Declaring a Function


def brush_teeth(): #brush_teeth is the function name, def is used to define a function
    print("take the toothbrush") #these three print lines are function body // sub tasks
    print("Clean teeth with it")
    print("Rinse your mouth")

print("Now call the function")
brush_teeth() #call function name to execute

#Using parameter or argument in function
# Variable declared as a parameter is only available inside that function only
def five_times(num):
    print(num*5)

five_times(7)
x = 9
five_times(9)

#Using return
def add_numbers(num1, num2):
    return (num1 * num2) # You can return any type of data type

mult = add_numbers(11, 5)
print(mult)

#A function example

def factorial(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact
print(factorial(5))

#Recursive Function
# TO call the function inside of the function is called a recursive function
def factorialRecursive(num):
    if num <= 1:
        return 1
    else:
        return num * factorialRecursive(num - 1)

print(factorialRecursive(7))

#Using default value as a parameter Funtion
def defaultValueFunction(val1, val2=5):
    return val1 * val2

print(defaultValueFunction(6, 6))
print(defaultValueFunction(6))

#Argument/Parameter Order not to be maintained if you pass it by their name
def simplesub(a, b):
    return a - b

print(simplesub(10, 5))
print(simplesub(b = 5, a = 10)) #both print will give same result

#Anonymous or Lambda Function - One line function
double = lambda x: x * 2
print(double(5))

#Using global variable inside a function -- Study more about it
c = 6
def add(a, b):
    c = a + b  # this c variable is different from the global c variable
    return c
print(add(3, 6))
print(c)

def add1(a, b):
    global c # that's how to call a global variable inside a function to modify it's value
    c = a + b # this c is the global variable, it's value has been changed
    return c
print(add1(10, 5))
print(c)



#Queries
# What about variable declared in a function ( not as a parameter/argument), can we call it from outside of the function?
# When and what happens when we use function parameter as (*args) - may be in those cases when we don't know how many parameters a user might pass

#Important Notes:
# #You can call a function from another Function 
# Variable declared as a parameter is only available inside that function only
# Return KW can return any data types as well as lists, tuple, dictionary, class or a dataclass
# Recursive Function calls itself
# You can set a default value to a parameter ( def functionName (value = 5) this default value will be used if you do not pass any parameter through it)
# Your don't have to worry about parameter order, if you pass it by their name while calling functions
# All built in funtions of python: docs.python.org/3/livrary/functions.html
# Do not forget to use ANonymous function / Lambda function, where necessary