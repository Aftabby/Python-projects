import numpy as np  #np is standard alias of numpy

#TO create a numpy array -- np.array(list_name)     -- the list_name is a list which contains one type of data as elements, like only integer or only string

my_list = [1, 2, 3, 4]
numpy_array = np.array(my_list)

print(my_list, type(my_list))
print(numpy_array, type(numpy_array))



# Dimensions in Arrays
# You can create multiple dimensions of array in numpy
# Numpy doesn't represent comma between the elements of array, like a list, it merely puts a space between the elements
# For more than one dimensional array, the number of elements in is array/list should be same - ex: each list/row of a 2D array should contain the same number of elements
# The number of open square bracket at the beginning represent the dimension of array


# 1-D Array  ->  [1 2 3]
# 2-D Array ->   [[1 2 3], [4 5 6]]
# 3-D Array ->   [[[1 2 3], [4 5 6]] [7 8 9] [10 11 12]]


#To check the dimension of Array
print("Dimension of array :", numpy_array.ndim)

list1 = [1, 2, 3, 4]
list2 = [3, 4 , 5, 6]

another_array = np.array([list1, list2])
print(another_array)
print("Another dimension of array:", another_array.ndim)        # ndim is a variable in numpy module, that's why we do not use --  ndim() -- rather we use -- ndim  --



# To create a multi-dimensional array, that is n-D Array

# Creating a 10 dimensional array
array2 = np.array([1, 2, 3, 4], ndmin = 10) # ndmin is an optional named parameter, which takes the value of how many dimensional array you wanna create

print("10 dimensional Array:\n", array2)       # printing a 10 dimensional array, in which we passed only one element
print("Dimension of the above array:", array2.ndim)  




#Important NOtes:
# SOme function takes the shape of the array as parameter, be careful different function takes it different way, 
    #some as a tuple -- (2, 3) -- some as list -- [2, 3] -- some as another parameter --  2, 3  --