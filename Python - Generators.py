# =======================================   GENERATORS    ===================================

# Generator generates iterators.
# Main difference between generator kw -- yield -- and -- return -- keyword:
    # return statement terminates a function, whereas -- yield -- statement pauses the function saving all its states and later continues from there on successive calls.



# A PROBLEM
# We need 5 random numbers

# A try to solve:
import random

def data():
    for i in range(5):
        return random.randint(1, 10)
    
print(data())           
print("Problem didn't solve!")
# But we are getting only one data


# THE  ACTUAL SOLUTION
def data():
    for i in range(5):
        yield random.randint(1, 10)         # Whenever you use atleast one -- yield -- kw in your statement, it becomes generator function

for num in data():
    print(num)