#Multiple line string -- Extra
any_string = '''This is a line
This is another line
This is third line'''   #You can write multiple line inside ''' -- triple quote

print(any_string)



#Sum of Digit
digits = input("Enter the digits:\n")
sum = 0
for i in digits:
    sum += int(i)
print(sum)
# ---- Another way of approach
def sum_of_digit(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum
sum = sum_of_digit(int(digits))
print(sum)






#Divisible by 3 and 5
num = int(input("Enter a number\n"))
div = []
for i in range(0, num):
    if i % 3 == 0 and i % 5 ==0:
        div.append(i)
print(div)






#Finding the average of a number
totalNumbers = int(input("How many numbers do you want to enter?\n"))
sumofNums = 0
allNumbers = []
while totalNumbers > 0:

    allNumbers.append(int(input("Enter Number\n")))
    totalNumbers -= 1

for element in allNumbers:
    sumofNums += element

average = sumofNums / len(allNumbers)
print("Average", average)
#-------Another Approach
len1 = int(input("Total element:\n"))
allNumbers = []

for i in range(0, len1):  #Study about range moree
    element = int(input("Enter Element"))
    allNumbers.append(element)

total = sum(allNumbers)  #Sum function returns the addition of all the elements in the list
average = total / len1
print("Average of elements you entered", round(average, 2))





#Find the largest number 
num1 = 10
num2 = 15

largest = max(num1, num2) #Use max to find out the large number
print(largest)
# ------- Finding the largest among three numbers
num3 = 25
largest = num1

if num1 <= num2:
    largest = num2
if largest <= num3:
    largest = num3
print(largest)
#---------Another Approach
largest = max(num1, num2, num3)
print(largest)






#Swapping two variable
num1 = 5
num2 = 10

temp = num1
num1 = num2
num2 = temp
print(num1, num2)
# ----- Another important approach
num1 = 5
num2 = 10
num1, num2 = num2, num1  #That's shortcut of python for interchanging the value of two variable
print(num1, num2)
#--------ANother approach
num1 = 5
num2 =10
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(num1, num2)




#Find the quotient(result without the remainder, that is without fraction) of any division 
num1 = int(input("Enter a number\n"))
num2 = int(input("Enter another number\n"))

quotient = num1 // num2  #Use // to find quotient that is 37//10 = 3 -- the fraction will not be calculated

print(quotient)
#-----------ANother approach
import math    # requires math library to call methods regarding mathematical operation

quotient = math.floor(num1/num2)  # You know what floor does , it takes 4.3 and returns 4
print(quotient)






#Pick up a Random Number
import random   #importing built in library random to call randint method

random_int = random.randint(0, 100)
print(random_int)







# Math Power
power = int(input("Enter the power number\n"))
base = int(input("Enter the base number\n"))
total = base ** power #USe ** to calculate power
print(total)
#---Another approach
total = pow(base, power)
print(total)
#---Another approach
total = 1
while power > 0:
    total *= base
    power -= 1
print(total)






#Multiplation Table
def multiplicationTable(num):
    i = 1
    while i <= 10:
        print(num, "*", i, "=", num * i)
        i += 1
multiplicationTable(int(input("Please enter a number to see it's multiplication table\n")))




#Merging lists and Sorting the elements
def merge_sort(list1, list2):
    newList = list1 + list2
    newList.sort() #sorting the list and save it inside the same list
    return newList

list1 = [ 12, 5, 11, 35, 64, 2, 5]
list2 = [ 33, 3, 535, 3, 23, 643]

newList = merge_sort(list1, list2)
print(newList)
        
        



#Fibonacci Series 
def fibonacci(num):
    series = [0, 1]
    while num > 0:
        series.append(series[(len(series)-2)] + series[(len(series)-1)])
        num -= 1
    return series

print(fibonacci(int(input("Please enter the number to find fibonacci series upto that number.\n"))))





#Remove duplicate from a list while appending
aList = []
i=1
while i == 1:
    name = input("Please enter your name:\n")
    if name in aList:
        print("The name is in the list already.\n")
        i = int(input("To add more name press 1 or to quit press 0\n"))
    else:
        aList.append(name)
        print("The name has been added.\n")
        i = int(input("To add more name press 1 or to quit press 0\n"))
print(aList)
#-----------Another way of approach ----
def removeDuplicate(bList):
    uniqueList = []
    for item in bList:
        if item in uniqueList: #That's a way to check an item if it exists in a list or string
            continue
        uniqueList.append(item)
    return uniqueList

bList = [66, 69, 365, 59, 42, 66, 59] #Given List
print(removeDuplicate(bList))


#Count vowels in a sentence
aSentence = input("Input any sentence to check vowels in it.\n")

def count_vowel(aSentence): #the global aSentence variable and the aSentence variable inside the function is not same
    vowel = 0 #the global vowel variable and the vowel variable inside the function is not same
    for char in aSentence:
        if char == 'a' or char == 'e' or char == 'i' or char == "o" or char == 'u':
            vowel += 1
    return vowel

vowel = count_vowel(aSentence)
print("The total number of vowel in that sentence is", vowel)
#----Another approach to solve it --
vowelList = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
def count_vowel1(aSentence):
    vowel = 0
    for char in aSentence:
        if char in vowelList: #To check if the char is in the vowelList
            vowel += 1
    return vowel
print(count_vowel1(aSentence))




# Check Word limits of input
yourBio = input("Please write anything between 10 words about yourself\n")

wordCOunt = 1

for letter in yourBio:
    if(letter == " "):
        wordCOunt += 1

if wordCOunt > 10:
    print("The bio should be within 10 words but it is of", wordCOunt,     "words")
else:
    print("Good job! Writing it within 10 words")






# Leap Year USING Exception Handling in Python - (Try - Exception)
print("Leap year test using Try-Exception handling")
year = input("Enter the name of the year\n")

while True:
    try:
        year = int(year)
        break
    except:
        year = input("Please enter a valid year")

if year%4 == 0:
    print("The year", year,"is a leap year")
else:
    print("The year", year,   " is not a leap year")






#Queries
# How to print number type data and string type data, how space gets automatically added in between these two data type
# Study more about calling global variables in function
#What does round function do?



#Important Notes
# To print multiple line in string use \n or use triple quote ---'''  This is a line *enter* This is another line ''' 
# The indexing number of a string type variable also work as the index number of list
# For more problem solving visit HeckerRank and LeetCode
# Assigning a value by mathematical division to a variable, the variable data type automatically becomes float -- ( a = 10/5, here a is float data type)
# To see data type of a variable ( print(type(variable_Name)))
# It is best practice to write veriable name is Snake format i.e the_new_variable
# String is immutable and Lists are mutable. Mutable means elements can be changed individually