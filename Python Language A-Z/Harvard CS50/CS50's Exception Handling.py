x = int(input("What's X? "))

# If the user inputs a string that is not a number, then it would be a value error
# Let's see how we can avoid that

while True: #So that we can ask for the right input from the user again and again
    try:
        print("Try started..")
        y = int(input("What's Y? ")) #Error Found here and the interpreter moved to the except block
        print(f"Y is {y}")  #Good practice is to put this line in the else block below
    except ValueError:  #if you leave the ValueError empty, just -- except: -- then by default the except kw will catch any type of error 
        #print("Y is not an integer. Put an integer.")
        pass #passing is just like -- continue -- 
    else:
        print("everything went smoothly. Thanks")  #If the try block doesn't have error (in this case ValueError), the else block will get executed
        break




