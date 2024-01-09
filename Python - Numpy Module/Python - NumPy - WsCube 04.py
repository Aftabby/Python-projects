import numpy as np

#Data Type in Numpy Arrays


#To find array data type
list1 = [1, 2, 3, 4]
arr1 = np.array(list1)
print("The array 1:\n", arr1, "\nThe Data type:", arr1.dtype)         #d.type is a variable in the numpy module - in brief a variable of the array class from numpy module, that's why we didn't use () in the end


list2 = [1.0, 1.2, 1.3, 1.4]
arr2 = np.array(list2)
print("The array 2:\n", arr2, "\nThe Data type:", arr2.dtype)       #d.type is for data type


list3 = ["h", "e", "l", "l", "o"]
arr3 = np.array(list3)
print("The array3:\n", arr3, "\nThe Data type:", arr3.dtype)


list4 = ["h", "e", 1, 1, 0]
arr4 = np.array(list4)
print("The array4:\n", arr4, "\nThe Data type:", arr4.dtype)








#Converting the data type
list5 = [1, 2, 3, 4]
arr5 = np.array(list5)
print("The array5:\n", arr5, "\nThe Data typy:", arr5.dtype)

arr6 = np.array(list5, dtype= np.int8)           #converting the datatype, by another optional parameter dtype. As numpy was created by C language, the datatype also came from C language
print("The array6:\n", arr6, "\nThe Data typy:", arr6.dtype)  

arr7 = np.array(list5, dtype = "f")     #Converting to float,,, The difference between converting the data type as np.int8 and "f" for float, is, if you want to be specific you go for np.int8 (8 bit), np.int32 (32 bit), and if you just want it to convert to integer you go with the string keyword dtype = "i"
print("The array7:\n", arr7, "\nThe Data typy:", arr7.dtype)

#Converting the data type by a function
arr8 = np.float32(arr6)        #arr6 is the integer data type, now we are converting it to float32 data type by a function
print("The array8:\n", arr8, "\nThe Data typy:", arr8.dtype)

#Conveting the data type directly as a function
arr9 = arr6.astype(float)       #If we run a method - astype() - on an array with parameter of the data type -- float (as it is float here) - then the method will return the array with changed data type
print("The array9:\n", arr9, "\nThe Data typy:", arr9.dtype)

