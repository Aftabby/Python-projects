import numpy as np

#Shape and Reshape in Numpy Arrays

#Shape
#Checking the shape of an array
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
arr1 = np.array([list1, list2])
print("Array 1:\n", arr1, "\nShape of Array1: ", arr1.shape)      # shape is a array method variable which shows (row, column) of an array


arr2 = np.array(list1, ndmin = 4)       #With the help of named parameter we are making 4 dimensional array here
print("Array 2:\n", arr2, "\nShape of Array2: ", arr2.shape, "\nThe dimension of the Array2:", arr2.ndim)       #Shape explained, here in this particular 4D array, number of rows is 1, the next number of rows is also 1, the next number of rows is again 1, and then the number of column is 4, so the shape is (1,1,1,4)









#Reshape 
    # Changing the dimension of array

list3 = [1, 2, 3, 4, 5, 6]
arr3 = np.array(list3)
print("Array 3:\n", arr3, "\nShape of Array3: ", arr3.shape, "\nThe dimension of the Array3:", arr3.ndim)

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
arr4 = np.array(list4)
print("Array 4:\n", arr4, "\nShape of Array4: ", arr4.shape, "\nThe dimension of the Array4:", arr4.ndim)

#rashaping the array
arr5 = arr3.reshape(3, 2)      #As parameter we pass the new shape of the array as (row, column)
                                    #But remember the elements number of previous array and new array should match that is , 
                                    #in array3 the element is 1X6 = 6 (row * column) and in the newer reshaped array the element number is 3X2 = 6 , the element numbers matched

print("Array 5:\n", arr5, "\nShape of Array5: ", arr5.shape, "\nThe dimension of the Array5:", arr5.ndim)


#reshaping an 1-D array to 3-D array:
arr6 = arr4.reshape(2, 3, 2)    # From the left of the parameters, we wanted 2 rows, 2 rows, 3 columns
print("Array 6:\n", arr6, "\nShape of Array6: ", arr6.shape, "\nThe dimension of the Array:", arr6.ndim)    


#reshaping a 3-D array to 1-D array:
    #below two lines work the same
arr7 = arr6.reshape(12)     #There is a shortcut to make 1 dimensional array from a multidimensional array, just pass the paramete as negative one (-1)
#arr7 = arr6.reshape(-1)
#arr7 = np.reshape(arr6, 12)        #It also does the same thing
#arr7 = np.reshape(arr6, -1)        #It also does the same thing
print("Array 7:\n", arr7, "\nShape of Array7: ", arr7.shape, "\nThe dimension of the Array7:", arr7.ndim)