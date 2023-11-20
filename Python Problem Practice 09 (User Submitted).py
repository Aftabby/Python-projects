#Birthday remaining:
from random import randint #importing randint method from random module

def find_a_date():        #This code isn't working, find the bug and fix it
    date = randint(1, 31)
    bdate = randint(1, 31)
    month = randint(1,12)
    bmonth = randint(1, 12)

    return [date, month, bdate, bmonth]


def calculate_birthdays(todate, tomonth, birthday, birthmonth):
    norm_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day_remaining = 0
    same_month = 1
    

    while True:
        if tomonth == birthmonth & same_month == 1:
            day_remaining += birthday - todate
            break
        elif tomonth == birthmonth & same_month == 0:
            day_remaining += birthday
            break
        else:
            same_month = 0
            if tomonth == 1:
                day_remaining += 1

            if day_remaining == 0:
                day_remaining += norm_year[tomonth-1] - todate

            else:
                day_remaining += norm_year[tomonth-1]

        if tomonth == 11:
            tomonth = 0
        else:
            tomonth += 1
    
    return day_remaining



dates = find_a_date()
print(dates)
days_remaining = calculate_birthdays(dates[0], dates[1], dates[2], dates[3])

print("Birthday date: ")
print(dates[2], dates[3])
print("Today's date:")
print(dates[0], dates[1])

print(f"\n\ndates remaining: {days_remaining}\n")
#---------Another approach------
from datetime import datetime   #importing the datetime method from datetime module
import time
 
def get_user_birthday():
 date_str = input("Enter your birth date in DD/MM/YYYY: ")
 try:
   birthday = datetime.strptime(date_str, "%d/%m/%Y") #Converting it into python date by using datetime.strptime() function
 except TypeError:
   birthday = datetime.datetime(*(time.strptime(date_str, "%d/%m/%Y")[0:6]))
 return birthday
 
def days_remaining(birth_date):
  now = datetime.now()   #This function gets the time when you run code
  current_year = datetime(now.year, birth_date.month, birth_date.day)
  days = (current_year - now).days
  if days < 0:
    next_year = datetime(now.year+1, birth_date.month, birth_date.day)
    days = (next_year - now).days
  return days
 
birthday = get_user_birthday()
next_birthday = days_remaining(birthday)
print("Your birthday is coming in: ", next_birthday, " days")





















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
# Use the datetime method from datetime module for more functionability
# use the KW -- global variable_name -- to call/update a variable that is outside of a function from inside of the function
# global - If you don't wanna update a global variable, just to view, print or read global function you don't need to use -- global variable_name-- inside a function 
# time module - use time.sleep(seconds) to pause the function for certain numbers of seconds (the second parameter passed into it )
# import random -- means importing random module --- random import randint -- means importing randint method separately -- so that we can use randint(num1, num2) instead of random.randint(num1, num2)
