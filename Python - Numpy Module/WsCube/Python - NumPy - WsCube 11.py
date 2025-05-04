import numpy as np

# ==  Join and Split function in NumPy arrays =====


# Joining of  two or more arrays 
        # To join two arrays the numbers of dimensions of two array should match
        # For more than 1D array, the elements number of each row of two array should match, but the total row number doesn't matter
        # As in concataning in multiple dimension array, by default the concatetion happens column wise (axis = 0), but if you want to change that you can pass an extra parameter (axis) with value = 0,1,2.. 


#1-D Array
list1 = [1, 2, 3, 4]
list2 = [5, 6, 8]

arr1 = np.array(list1)
arr2 = np.array(list2)

arr3 = np.concatenate((arr1, arr2))     #Beaware, this function takes parameter as tuple

print("Array1:\n", arr1, "\nArray2:\n", arr2, "\nArray1 + Array2:\n", arr3)




#2-D Array
list3 = [[10, 11], [12, 13]]
list4 = [[14, 15], [17, 19]]

arr4 = np.array(list3)
arr5 = np.array(list4)

arr6 = np.concatenate((arr4, arr5))
print(arr6)

#Concatening in rows
list5 = [[20, 21], [22, 23]]
list6 = [[24, 25], [27, 29]]

arr7 = np.array(list5)
arr8 = np.array(list6)

arr9 = np.concatenate((arr7, arr8), axis=1) # As in concataning in multiple dimension array, by default the concatetion happens column wise (axis = 0), but if you want to change that you can pass an extra parameter (axis) with value = 0,1,2.. 
                                            # Here we are adding it row wise, axis parameter is described above
print(arr9)


#Alternative function - stack() - it also merges array but in a different way
print("\nStack funcion started")
arr10 = np.stack((arr7, arr8), axis = 1)            #Check and compare the results to see the difference between stack and concatenate
print(arr10)                                        #There are three different types of sub-stack function, horizontally, vertically and dimensionally

arr11 = np.hstack((arr7, arr8))         #Horizontally, that is merging along rows
print(arr11)
arr12 = np.vstack((arr7, arr8))         #Vertically, that is merging along columns
print(arr12)
arr13 = np.dstack((arr7, arr8))         #Dimensionally, that is merging along height or dimension
print(arr13)









# =============================  Split Array : Splitting breaks one array into multiple  ==========================
print("Split array started:\n")
list7 = [30, 31, 32, 33]
arr14 = np.array(list7)

ar15 = np.array_split(arr14, 3)      #spliting the function, the parameter is (array, no. of parts), no. of parts is into how many parts you want to split the array, it returns all the splitted array inside a list.
print(ar15)
print(type(ar15))
print(ar15[0])                         # you can access each of the splitted array through indexing of list

# 2-D Array
ar16 = np.array(list5)
ar17 = np.array_split(ar16, 2)
print(ar17)
ar18 = np.array_split(ar16, 2, axis=1)          #Splitting along axis (0, 1, 2..) i.e (x, y,..) i.e (row, column, dimension)
print(ar18)

