import numpy as np
# Special Type of Arrays
                        # We write the shape of an array with (Row X Column), when it is 3-D we write in (Row X Row x Column) way, same way in 1-D array we can only write (Column)


# Arrays filled with Zero's
ar_zero = np.zeros(4)       # This -- zeros() -- method takes mandatory parameter, which represents the shape of the arrray
print(ar_zero, "\nDimension: ", ar_zero.ndim)   

ar_zero1 = np.zeros((3,4))      # It will create a 3 X 4 dimension array, that is it will have 3 rows and 4 elements each, and all the elements value will be zero, we passed the parameter as a tuple
print(ar_zero1, "\nDimension: ", ar_zero1.ndim)


ar_zero2 = np.zeros([4,5], dtype = int)         #If you check the upper matrix, the returned element is float that's why there is a dot (.) at the end of the 0(zero), you can pass an optional parameter dtype, which represents data type of returned value
                                                    #Also here while passing the parameter of dimension of array, we did with square bracket i.e list, which is the conventional way to do it, though in previous one we did with a tuple
print(ar_zero2, "\nDimension: ", ar_zero2.ndim)








# Array filled with One's
ar_one = np.ones(5)    # Here it will create a 1-D array of 5 elements, with all the value of elements as 1
print(ar_one, "\nDimension:", ar_one.ndim)

ar_one1 = np.ones((5, 3))
print(ar_one1, "\nDimension:", ar_one1.ndim)  #It will create a 5X3 dimension array, all filled with the value 1   (float type)

ar_one2 = np.ones([3, 5], dtype = int)       #It will create a 5X3 dimension array, all filled with the value 1 (int type)
print(ar_one2, "\nDimension: ", ar_one2.ndim)







#Creating an Empty Array

arr_empty = np.empty(4)     #Empty arrays value could be anything, depending upon the previous value stored in that location
print(arr_empty)

arr_empty1 = np.empty((5, 4))       #We can also pass in the shape as a list, here we passed it as a tuple
print(arr_empty1, "\nDimension: ", arr_empty1.ndim)








# Arange funcion (it's not arrange, it's 'a range' together) - Creating an array with a range of elements
            # Parameter : start (optional), start of interval range, by default it is 0 (including)
                        # stop, end of interval range -- (excluding)
                        # step (optional), step size of interval, by default the step size is 1
                        # dtype, type of output elements of array

arr_range = np.arange(4)    #In the parameter you give the total number of elements the matrix should have, and the elements will be automatically generated within that range maintaining sequential order
print(arr_range)
print("\n\n")

arr_range1 = np.arange(6).reshape(2, 3)     #With reshape method you declare the shape of the array, but make sure the total elements of dimension of the array should match the number of range i.e. in here 2X3=6
print(arr_range1, "\nDimension: ", arr_range.ndim, "\n\n\n")

arr_range2 = np.arange(4, 10)       # Start of the range is 4 and the stop of range is 10
print(arr_range2, "\n\n")

arr_range3 = np.arange(4, 20, 0.5)     # In the parameter we passed - Start, stop and step of the array --- If you want to pass the step size, you must pass start of the interval also
print(arr_range3, "\n\n")







# Creating an Identity Matrix - that is an array which diagonal element is filled with 1's
                            # You can also make non-square array, whose diagonal is filled with 1

arr_diagonal = np.eye(3)        #It takes the shape of the array as parameter
print(arr_diagonal, "\n\n")


arr_diagonal1 = np.eye(3, 5, dtype=int)        # In here you can pass the array shape 
print(arr_diagonal1, "\n\n")










# Creating Array with values that are spaced linearly in a same/specific interval
                                                #parameter: (start_number (included), stop_number (included), number of elements)

ar_lin = np.linspace(1, 10, num = 5)    # Here the total range is start = 1 (included), stop = 10 (included), number of elements = 5
print(ar_lin, "\n\n")

ar_lin1 = np.linspace(1, 10, num = 4)    # Here the total range is start = 1, stop = 10 , number of elements = 4
print(ar_lin1)
