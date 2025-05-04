def my_decorator(func):  # Step 1: my_decorator takes a function as an argument
    def wrapper():       # Step 2: Define a wrapper function inside it
        print("Before the function runs")
        func()           # Step 3: Call the original function
        print("After the function runs")
    return wrapper       # Step 4: Return the wrapper function

@my_decorator  # Step 5: This is equivalent to: say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello, World!")

'''
OUTPUT:
Wrapper One: Before function runs
Hello, World!
Wrapper One: After function runs

Flow of Execution in Detail:
@my_decorator modifies say_hello(), my_decorator(say_hello), which in terms calls wrapper.
Now say_hello() is no longer the original function but instead points to wrapper().
When you call say_hello(), Python actually runs wrapper(), which:
Prints "Before the function runs"
Calls func() (which is the original say_hello())
Prints "After the function runs"
'''


#Using multiple wrapper functions
def decorator_one(func):
    def wrapper():
        print("Decorator One: Before function runs")
        func()
        print("Decorator One: After function runs")
    return wrapper

def decorator_two(func):
    def wrapper():
        print("Decorator Two: Before function runs")
        func()
        print("Decorator Two: After function runs")
    return wrapper

@decorator_one  # Runs first
@decorator_two  # Runs second
def say_hello():
    print("Hello, World!")

say_hello()

'''
OUTPUT:
Decorator One: Before function runs
Decorator Two: Before function runs
Hello, World!
Decorator Two: After function runs
Decorator One: After function runs

TIPS:
If you define multiple wrappers inside one decorator, only the one that gets returned will execute.
If you want multiple wrappers to execute, use multiple decorators.
'''