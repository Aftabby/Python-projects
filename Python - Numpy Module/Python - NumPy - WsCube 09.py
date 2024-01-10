import numpy as np

# Iteration NumPy Arrays

# 1-D Array
list1 = [1, 2, 3, 4, 5]
arr1 = np.array(list1)

for i in arr1:
    print(i)


# 2-D Array
list2 = [[7, 8, 9], [4, 5, 6]]
arr2 = np.array(list2)

for i in arr2:          #FOr the first -for loop- the variable - i - is iterating over the rows of the array
    for j in i:         # For the second - for loop - j - is iterating over the elements of the array
        print(j)




# 3-D Array
list3 = [[[10, 11], [12, 13]], [[14, 15], [16, 17]]]
arr3 = np.array(list3)

for rows in arr3:                   #If you understand 2-D array you will also understand this one as well
    for row in rows:
        for element in row:
            print(element)




# =============================  Iteration using function (np.nditer()) ================
print("Printing using function:")
    
#1-D array
for i in np.nditer(arr1):       #You can also pass multiple parameter np.nditer() method to manipulate the iteration
    print(i)


    #Iterating with index value  -- np.ndenumerate() --
for indexx, value in np.ndenumerate(arr1):  #This function will return two value, one is index and another one is the element value
    print(indexx, value)
