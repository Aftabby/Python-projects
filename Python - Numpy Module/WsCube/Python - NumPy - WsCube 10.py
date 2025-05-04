import numpy as np

# ===========  Copy vs View  ========================

list1 = [1, 2, 3, 4]
list2 = [10, 11, 12, 13]
arr1 = np.array(list1)

#Copy the arr1
arr1_copy = arr1.copy()
print("Array 1:\n", arr1, "\nCopy of Array 1:\n", arr1_copy)


#Viewing the arr1
arr1_view = arr1.view()
print("View of Array1\n", arr1_view)


# Difference between copy and view:
    # Copy owns the data where view does not own the data
    # The copy of the array is a new array, view is the view of the original array
    # The changes made in the -- copy -- data does not reflect in the original array, any changes made to the -- view --  will affect the original array, vice versa, changes in original array will affect -- view --


#Checking the change in value:
arr1[2] = 50                                #This change means you only change some indexed elements (arr1[3] = some_value), not completely create a new array by np.array() , if you create a completely new array view and copy nothing will be affected
print("\nThe change is none in 'copy':\n", arr1_copy)
print("\nThe changes in 'view' :\n", arr1_view)

    #Vice-Versa
arr1_view[1] =  40
print("\nThe change in original array also made the change in view:\n", arr1)

