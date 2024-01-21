# Module and Library is the same thing
# Generally a module is made of bunch of functions and features
# When you install python, there comes different types of default modules that you can import any time, example: import random
# Package -- is the module/libraries that are third-party -- are called packages. pypi.org has almost all the packages
# TO install a package, type in command line -- pip install package_name -- pip is a programme that installs third party packages



#Using import keyword
# By using the KW import, we load all the functions and features of the module
import random

coin = random.choice(["heads", "tails"])   #We called a function choice which belongs in the random module, that's why we called random.choice, although there is an alternative way to call.
print(coin)


#Alternative of using keyword import  
# We use -- from -- KW, when we want to be more specific, like importing only a function from module
# By using the KW from, we we load only specific functions from the module, not the whole module
from random import choice   #It adds the function -- choice -- into the current namespace/scop

coin = choice(["heads", "tails"])   #As we have imported the function specifically, not the whole library, so we don't need to write random.choice -- anymore

number = random.randint(1, 10)  #We have to call it random.randint() because we did not import it as a specific function, thus this function belongs the the random module scope, which we imported earlier
print(number)


cards = ["jack", "queen", "king"]
print(cards)
random.shuffle(cards)
print(cards)



''' Multi line comment
Below there is the statistics module
'''

import statistics

print(statistics.mean([100, 90]))

print("\n\n\n")




'''
Importing --sys-- module below
'''
import sys 

'''
THis time while running the program from the command line, run -- py file_name.py input1 input2 --- 
no more prompt for user input.
the input that has been provided while running the program (input1, input2) 
will be in the varable -- sys.argv -- as a form of a list i.e. sys.argv = [name_of_the_file, input1, input2, ....]
'''
print("hello, my name is", sys.argv[1]) # run -- py file_name.py your_name -- as the first element of -- sys.argv -- is the name of the file, so we print the second element i.e index number 1


#If the user don't provide name while running the code, to avoid error - 
try:
    print("hello, my name is", sys.argv[1])             #Handling exception
except IndexError:
    print("Too few arguments")

#OR
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv)>2 : 
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])


#OR
if len(sys.argv) < 2:
    sys.exit("Too few arguments")   #Sys.exit -- stops or exits the system(programme) with a message as an argument
elif len(sys.argv)>2 : 
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])








'''
Importing a package (third-party module) cowsay, after installing -- pip install cowsay -- in the command line

'''
import cowsay
import sys

if len(sys.argv) == 2:  # run in the command line-- py file_name your_name --
    cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])





