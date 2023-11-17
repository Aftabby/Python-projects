#Birthday remaining:
import random
random import randint 









#Simple Digital Clock
import time

hour = int(input("Enter hour: \n"))
min = int(input("Enter min: \n"))
sec = int(input("Enter sec: \n"))

def show_clock():
   # global hour
   # global min
   # global sec

    print(f"{hour} hour : {min} min : {sec} sec")

def update_time():

    global hour
    global min
    global sec

    sec += 1
    if sec == 60:
        sec = 0
        min += 1
    if min == 60:
        min = 0
        hour += 1
    if hour == 13:
        hour = 1


while True:
    show_clock()
    time.sleep(1)
    update_time()

    













#changing a global variable inside of a function

x = 5

def double_global_x():
    global x              #To call the variable outside of the function and update it
    x = 2 * x
    return x

print("Global variable before: ", x)
print(" function variable : ", double_global_x(), "\n")
print("Global variable after: ", x )







#Important Notes:
# use the KW -- global variable_name -- to call/update a variable that is outside of a function from inside of the function
# global - If you don't wanna update a global variable, just to view, print or read global function you don't need to use -- global variable_name-- inside a function 
# time module - use time.sleep(seconds) to pause the function for certain numbers of seconds (the second parameter passed into it )
# import random -- means importing random module --- random import randint -- means importing randint method separately -- so that we can use randint(num1, num2) instead of random.randint(num1, num2)