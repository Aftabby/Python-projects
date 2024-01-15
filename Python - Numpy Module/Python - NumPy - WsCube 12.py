import numpy as np

# Numpy Array Functions (Search, Sort, Search-Sorted, Filter)


#=======  Search array  =========
list1 = [14, 16, 19, 23, 14, 16]
arr1 = np.array(list1)

index1 = np.where(arr1 == 16)    #this -- np.where( array_name == searching_element ) -- function will return all the index positions where the searching_element is present in that particular array
print(index1)                           # But while searching the element in multidimensional array, the index value is returned in each of the tuple, in a column format

   # You can also perform mathematical operation in parameter of -- np.where() -- function, example shown below:
index2 = np.where(arr1%2 == 0)  #Finding all the index number of the postive elements present in that particular array
print(index2)

index3 = np.where(arr1/2 == 8)  #Finding all the index number of the elements where if it's divided by 2, the result will be 8
print(index3)










#====== Search Sorted Array =======
        #It performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order

list2 = [1, 2, 3, 4, 6, 7, 8, 9]
arr2 = np.array(list2)

search_sort_index1 = np.searchsorted(arr2, 5)    #It will return the index in where if we place the element -- 5 -- , the array will still be sorted
print(search_sort_index1)

  #This function moves from left to right in the array and finds the suitable sorted place for our new element in the array
        #If you want to move the funcion from right to left through the array elements then you can pass an extra parameter to the function, shown below:

search_sort_index2 = np.searchsorted(arr2, 5, side="right")     #Though the returned value will be same here, it is needed when the new value might exist multiple times in the array
print(search_sort_index2)









# ==========  Sorted Array  ============
        #It makes the array sorted or in ordered sequence - numerically or alphabetically - ascending or descending way

list3 = [6, 3, 1, 52, 5, 9, 3]
arr3 = np.array(list3)

print(arr3)
arr4 = np.sort(arr3)    #THis function returns a sorted function of this array, it can also sort alphabetic array
print(arr4)












# ====== Filter Array  ==============
        # Getting some elements out of an existing array and creating a new array out of them

list4 = [10, 11 , 12, 13]
arr5 = np.array(list4)

filter_elements = [True, False, False, True]    #For every element/value you don't want to filter out you put False in that position, for every value you want to filter out you put True in that postion

filtered_array = arr5[filter_elements]          

print(filtered_array)
