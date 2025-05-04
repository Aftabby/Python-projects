#Greatest Common Divisor
def GCD(num1, num2):
    if num1 >= num2:          #Or to find smaller, use---- min(num1, num2)
        smaller = num2 
    else:
        smaller = num1
    while smaller > 0:
        if num1 % smaller == 0 and num2 % smaller == 0:
            return smaller
        smaller -= 1
    
num1 = int(input("Enter first number: \n"))
num2 = int(input("Enter second number: \n"))

#print(f"The {num1} is {num2}")                   #To use variable value inside a print funtion string - print(f"The normal string {varibale_name} string continues") --- f{string}

print("The GCD of ", num1, "and", num2, "is : ", GCD(num1, num2), "\n")
#---------Another approach--------
import math

num1 = int(input("Enter first number: \n"))
num2 = int(input("Enter second number: \n"))
gcd = math.gcd(num1, num2)                  #Python has a built-in gcd function inside math library
print(gcd)











#Armstrong Number
def digit_finder(num):
    i = 0                  # or you can use i = len(str(num))
    while num > 0:
        num = num // 10
        i += 1
    return i

def armstrng_num(num):
    pow = digit_finder(num)
    temp = num
    sum = 0
    for i in range(pow):
        sum += (num % 10) ** pow
        num = num//10   # or use ---- num //= 10
    return sum == temp

num = int(input("Enter a number: \n"))
if armstrng_num(num):
    print(num, "is a armstrong number.\n")
else:
    print(num, "is not an armstrong number. \n")




# Cube SUM
num = int(input("Enter a number:\n"))
sum = 0
for i in range(1, num+1):
    sum += i**3
print("The sum of the cube is ", sum)








#Check Palindrome of a word
def check_palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[(i+1)*((-1))]:   #The M and m will be different , change it to make every letter small letter.
            return False
    return True

a_word = input("Enter any word: \n")
print("The palindrome of this word is", check_palindrome(a_word))
#--------------ANother approach---------
b_word = input("ENter the word: \n")
rev_word = b_word[::-1]   # It reverses the string
if(b_word == rev_word):
    print("palindrome")
else:
    print("Not palindrome.")



#Queries:
# What is set? how you convert a list to set using set(list_name)?
# How to intersect set? and get the common element by intersecting of two sets -- set1&set2



#Important notes:
# Python has a built-in gcd function inside math library
# You can convert to list by using list(name_of_variable)
# To get the highest element use --- max() --- function, works both for lists and individual parameters
# print(f"string {variable_name}")-----------To use variable value inside a print funtion string - print(f"The normal string {varibale_name} string continues"