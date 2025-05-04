

# =============================   Reading contents from a file   ================================


file = open("hero.txt")         #Without passing access mode the file will by default open at only read mode
content = file.read()      
print(content)
content = file.read(5)       # file.read() -- takes an optional parameter, where you can pass an integer of how many bytes from that file to read
print(content)

file.close()        #There is an alternative way to do the same thing shown below, where you will not need to close the file


# Alternative
with open("hero.txt", "r") as file:     #This way you don't have to write file.close() to release the memory at the end, the file will automatically close once the indented code block will be executed
                                        # -- access mode -- , here "r" means only read, "r+" means read and write
                                        # If you don't pass in any argument of -- access mode -- then by default the file will open in the -- only read -- mode
    content = file.read()
    print(content, type(content))



with open("hero.txt", "r") as file:     #To take back the cursor (file pointer) at the beginning again, when we open the file as read or write , the file pointer (cursor) gets at the beginning of the file
    reading_a_line = file.readline()
    print(reading_a_line)












# ==========================================    Writing Content to a File (Overwriting)    ==========================

# -- "w" access modes open the file in writing mode, "w+" access mode open file in writing and reading mode
# While writing a file, the file pointer (cursor) gets at the beginning of the file. Since the pointer is at the beginning of the file all the file is overwritten

with open("hero.txt", "w+") as file:
    file.write("Everything is overwritten now \n Hero was all gone.")
    content = file.read()
    print(content)







#  ========================================  Appending Content to a file  ===============================
    

with open("hero.txt", "a+") as file:            # "a" access mode means appending mode, and "a+" access mode means appending and reading mode
    file.write("\n This line is appended in the file")
    content = file.read()       # We have to take the cursor again at the top by opening the file.
    print(content)


































#=================================================================  Exception Handling  =============================
    

# There are three types of error, 1) Syntax Error (The interpreter catches it), 2) Logical Error (Your logic was wrong, but the code is right) and 3) Exceptions
# Exception error is not a kind of error but a situation that the program cannot cope with
# Specially a bad data is provide, lets user inputs to devide a number by 0, or in place of a integer user inputs a string
# Though the logic and syntax is just fine, it is just for some kind of exceptional data the program might raise an error --- really unusal condition, it is also called -- runtime errors --
    
#A single try can have multiple except statement
# A try statement must follow by one expect of finally statement
# The try-exept statement:
    '''
            try: 
                    { THIS CODE }

            except  ONE_KIND_OF_ERROR:                                                                  #If you don't mention ONE_KIND_OF_ERROR (Ex - ValueError), Then by default the except block will get triggered for any kind of error
                    { RUN THIS CODE IF AN EXCEPTION OCCURS WHICH BELONGS TO ONE_KIND_OF_ERROR  }

            except  ANOTHER_KIND_OF_ERROR:
                    { RUN THIS CODE IF AN EXCEPTION OCCURS WHICH BELONGS TO DIFFERENT_KIND_OF_ERROR }
            
            else:
                    { IF THE TRY BLOCK EXECUTED PERFECTLY WITHOUT RAISING AN ERROR/ EXCEPTION, RUN THIS CODE  }
            
            finally:
                    { THIS CODE WILL RUN NO MATTER EXCEPTION RAISED OR NOT }
            
        '''

#An example:
  
numerator = 55
denominator = 0



try:
    result = numerator / denominator
except  ZeroDivisionError:
    print("Can't divide by zero, please change the denominator")
else:
    print(result)



try:
    result = numerator / denominator
except:                                                            # If you don't mention any exception that will be raise, it will by default catch all exception error
    print("Can't divide by zero, please change the denominator")
finally:
    print("This finally block will run no matter exception/ error raises or not")







# =========================================    Manually Raise an exception ================================


#Example:

age = 16
try:

    if age < 18: 
        raise ValueError("You're no adult, GO HOME!")           #We raised an error manually with a little note
except:
    print("Entry Restricted")