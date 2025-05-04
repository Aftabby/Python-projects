#Generate Sentence

#MUST PRACTICE Permutation and Generate sentences
#>programming hero> python programming beginner to advanced > Problem solving > Harder > Permutation & Generate Sentence








#Permutation

#MUST PRACTICE








#Password Generator with Requirements
import string
import random

all_chars = string.ascii_letters + string.digits + string.punctuation
upper_case = string.ascii_uppercase 
lower_case = string.ascii_lowercase
digits = string.digits
punc = string.punctuation

def pass_gen_req(num):
    pass_req = ''
    if num > 3:
        pass_req += random.choice(upper_case)
        pass_req += random.choice(lower_case)
        pass_req += random.choice(digits)
        pass_req += random.choice(punc)
    else:
        return "not enough long to fulfill requirement.\n"

    num = num - 4
    while num > 0:
        pass_req += random.choice(all_chars)
        num -= 1
    return pass_req

num = int(input("How many characters do you want for your random password with requirements? (Min: 4 chars)\n"))

print(pass_gen_req(num), "\n")











#Password Generator
import string
import random

def pass_gen(num):
    all_chars = string.ascii_letters + string.digits + string.punctuation  #See important notes below to how it works
    password = ''
    while num > 0:
        password += random.choice(all_chars)
        num -= 1
    return password

num = int(input("How many characters do you want for your random password?\n"))

print(pass_gen(num), "\n")













#Simple Calculator
def multiply(num1, num2):
    return num1*num2

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2

num1 = float(input("Enter the number:\n"))
num2 = float(input("Enter another number\n"))

operation = input("What operation you wanna do??\nExample  +, -, *, /, %")
#Now complete the rest of the code




#Query
# Must practice permutation


#Important Notes
# String Module - You can use -- string.ascii_letters (to get all the characters from A-Z & a-z, as a string),
# String Module - You can use -- string.digits (to get all the single digits, as a string)
# String Module - You can use -- string.punctuation (to get all the special characters, as a string )
# Random Moudule - You can use -- random.choice(string_name) -- to get select a random character from a prvided string