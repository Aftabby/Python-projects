import numpy as np

#==========  Indexing of an arrray  =============

# 1-D Array
list1 = [2, 3, 4, 5]
arr1 = np.array(list1)

print(arr1[1], arr1[3], arr1[-2])     #Indexing just like we used to do in list list, it also take negative indexing


# 2-D Array
list2 =[[1, 2], [3, 4]]     #The first row will have indexing 0, and the second row will have index 1
arr2 = np.array(list2)

print(arr2[1][0])       #Here we chose the second row (whose index is 1), and then the first element (whose index is 0) from the second row


# 3-D Array
list3 = [
        [[1, 2],    
         [3, 4]],
        [[5, 6],
         [7, 8]]
                ]
arr3 = np.array(list3)
print("You'll get the idea if you follow the printed indexing below:")
print(arr3[0])
print(arr3[0][1])
print(arr3[0][1][1])    






#===============================================  Slicing Array  =================================
    # slicing -- array[start : stop : step]
    # In slicing the stop value is not included, the slicing stops excluding the stop value


#1-D Array
list4 = [1, 2, 3, 4, 5, 6]
arr4 = np.array(list4)

print("Slicing 1-D Array:", arr4[1:4], "\n", arr4[:3])      # just like we used to do in list list, it also take negative indexing slicing

print("Printing with Step: ", arr4[::2])        # slicing -- array[start : stop : step]



# 2-D Array
list5 = [[11, 12, 13], [14, 15, 16]]
arr5 = np.array(list5)

print("2-D Array Slicing", arr5[0, 1:], "\nAnother way: ", arr5[0][1:])     #Both are the same thing
print("2-D Array Slicing", arr5[1, :2], "\nAnother way: ", arr5[1][:2])     #Both are the same thing   #In slicing the stop value is not included, the slicing stops excluding the stop value




