import numpy as np

#=====  Numpy Arrays Function (Insert, Append and Delete function)


# ===  Insert ===
                # It takes three parameters, first - the array , second - index_position in which you wanna insert the value, third - The value/element
                # It returns the new array with the inserted new value
list1 = [10, 20, 40, 50]
arr1 = np.array(list1)

arr2 = np.insert(arr1, 2, 30)   # The fist parameter is the array, the second is the index position we wanna insert the value, and the third is the value itself
print(arr2)

arr3 = np.insert(arr1, (0, 3), 90)      #If you want to enter the same value to multiple index position, you can do that as well, here we are inserting the value on 0th and 3rd position
print(arr3)                             

arr4 = np.insert(arr1, 2, 99.56)        # Also keep in mind, if you wanna insert a float value, to an only integer value array, it will only take the integer part of that element, leaving the part after the decimal
print(arr4)


# 2-D Array
        #In 2-D Array you have to keep in mind two more things while inserting value
        # 1. Do you wanna add the element to each of the rows?      2. In which axis do you wanna insert the value(x,y...)? (axis=1,2..)


list2 = [[1, 2, 3], [4, 5, 6]]
arr5 = np.array(list2)

arr6 = np.insert(arr5, 2, 60, axis=0)       # np.insert(array, index_position, value, axis=0,1..) , the value will be added as another row, for the new row each element will be the value you passed, for maintaining the shape and no broadcast error
print(arr6)

arr7 = np.insert(arr5, 2, (60, 70, 80), axis=0)       #values and index_position can be multiple - pass it as a tuple
print(arr7)

arr8 = np.insert(arr5, 2, (60, 70), axis=1)       
print(arr8)










# =====  Append function in NumPy  ====      Just like list.append()
                                # np.append(array_name, value)
                                # For multi-dimensional array, the new value must be of same dimension as original array
list3 = [10, 20, 30, 40]
arr9 = np.array(list3)

arr10 = np.append(arr9, 50)     #It doesn't get appended to the original array rather it returns a new array with the appened value
print(arr10)


#2-D
list4 = [[1, 2, 3], [4, 5, 6]]
arr11 = np.array(list4)

arr12 = np.append(arr11, [[10, 20, 30]], axis=0)          # For multi-dimensional array, the new value must be of same dimension as original array      
print(arr12)                                              #You already know about the named parameter axis

arr13 = np.append(arr11, [[10], [20]], axis=1)          # The axis size must match as well as the dimension number also match
print(arr13)










# ===================   DELETE Function  ===================

list5 = [10, 20, 30, 40, 50]
arr14 = np.array(list5)
print(arr14)

arr15 = np.delete(arr14, 2)             # np.delete(array, index_position)  ----- It returns a new array with the element in the index position deleted 
print(arr15)

