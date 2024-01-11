import numpy as np

# NumPy Arithmatic Funcions (Shuffle, Unique, Resize, Flatten, Ravel)


# ===  Shuffle Array  ===
list1 = [1, 2, 3, 4, 5]
arr1 = np.array(list1)

np.random.shuffle(arr1)     # Remember: this np.random.shuffle function does not return the shuffled array, rather it shuffles the original array which is its parameter

print(arr1)














# === Unique Array  ===
        #It returns the value only once in the array, if there's any repeatitive value it will put that value once, and return an array out of it

list2 = [50, 60, 70, 50, 90, 60, 30]
arr2 = np.array(list2)

unique_value_array1 = np.unique(arr2)        # It also sorts the unique values in an ascending order
print(unique_value_array1)   


# You can also get the index number for each of the unique element
unique_value_array_with_index = np.unique(arr2, return_index=True)      #By default the -- return_index -- parameter is False

print(unique_value_array_with_index)


#You can also count how many times each element/value is present in the array
unique_value_array_with_index_and_count = np.unique(arr2, return_index=True, return_counts=True)    #By default the -- return_counts -- parameter is False

print(unique_value_array_with_index_and_count)
















# ===  Resize an Array  ===

list3 = [1, 2, 3, 4, 5, 6]
arr3 = np.array(list3)

resized_array = np.resize(arr3, (2, 3))     #In the parameter first pass the array, and then the new shape you want to resize it to (row, column)
print(resized_array)















# ====  Flatten and Ravel Function  ===
        # *Skipped * 









