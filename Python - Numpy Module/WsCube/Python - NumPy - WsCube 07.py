import numpy as np

# Broadcasting using numpy
        #To perform arithmatic operation on two array, both array should be of same dimension and same shape
        #For different dimensions of arrays, the both shape must contain one common no. of value, that is a.shape = (1X3), b.shape = (4X1) ,, both have one common no. of value i.e one (1) ,, The new array shape will be (the_greater_row_from_both_of_the_array ,  the_greater_column_from_both_of_the_array) -- this rules only applies when the common no. of value is one (1), not for any other common no. of values

list1 = [1, 2, 3, 4]    #The shape of this array is 1X4, and dimension 1-D
list2 = [5, 6, 7]       #The shape of this array is 1X3, and dimension 1-D

arr1 = np.array(list1)
arr2 = np.array(list2)

#print(arr1 + arr2)     #This line will show broadcasting error as two array are not of the same shape but same dimension, though there is an alternative



#============================== Alternative =====================================
list3 = [[1],[2],[3]]
list4 = [7, 8, 9]

arr3 = np.array(list3)      #The shape of this array is 3X1, and dimension 2-D
arr4 = np.array(list4)      # The shape of this array is 1X3, and dimension 1-D

print(arr3 + arr4)      # Though of different shape and dimension, the arithmatic operation is showing no broadcasting error



list5 = [[3], [4], [5], [6]]    #The shape of this array is 4X1, and dimension 2-D
list6 = [9, 10, 11]         #The shape of this array is 1X3, and dimension 1-D

arr5 = np.array(list5)
arr6 = np.array(list6)

print(arr5 + arr6)

# So what we learned from here, For different dimensions of arrays, the both shape must contain one common no. of value (that common no. of value must be 1), that is a.shape = (1X3), b.shape = (4X1) ,, both have one common value i.e one (1)
                        # It could also be a.shape = (1, 6) and b.shape = (1, 3)  -- and as there is a common no. of value which is one (1) in both the shape, therefore it will not show any broadcasting error 





