import pandas as pd
import numpy as np

# ==============  Group By  ===========
dict1 = {"Grade" : ["A", "B", "C", "F", "C", "C", "B", "A", "B", "A", "A", "B", "C"],
         "Absence" : [12, 13, 12, 14, 15, 13, 12, 15, 19, 20, 22, 12, 14],
         "Presence" : [94, 91, 95, 91, 90, 94, 93, 91, 91, 92, 98, 92, 90]}
dframe1 = pd.DataFrame(dict1)               #dataframe with not_unique random values
print(dframe1)


#Grouping the random values by a category(any column_values, we can call it category column_values here)
dframe2 = dframe1.groupby("Grade")      # -- dataframe_object.groupby(column_header) -- pass the column_header according to which column_values you want to use as category to group
print(dframe2)                  #Here, we can see the type of the object because it is data, not the values, to get the group_by values, we need use a for loop and extract each value (because the dataframe_groupby_object contains multiple dataframe_object based on each unique values of category column_header)

for unique_value, datas in dframe2:
    print("This is unique_value:")
    print(unique_value)                #The unique value of the category column_values
    print("This is all the datas(as a dataframe_object) assciated with the unique values (data):")
    print(datas)                #The dataframe/datas/columns associated only with that unique column_value



#Getting all the datas associated with only an unique_value(could exist multiple times in the original dataframe) of the dataframe_groupby_object made from original dataframe_object
dframe3 = dframe2.get_group("A")        # -- get_group(category_column_value) -- only works with dataframe_groupby_objects not the dataframe_object
print(dframe3)


#Getiing the min, max, mean,  value from each of the group of the dataframe_groupby_object made from original dataframe_object
dframe4 = dframe2.min()
print(dframe4)

dframe5 = dframe2.max()
print(dframe5)

dframe6 = dframe2.mean()
print(dframe6)


#Converting dataframe_groupby_object (made from original dataframe_object) to a list
                            #Then you can apply all the method you can use on a list
list1 = list(dframe2)
print(list1)                #In the list each of the grouped dataframe_object will be in a tuple
print(type(list1[0][0]))    #First element of the tuple is the unique_value of the dataframe_group_object
print(type(list1[0][1]))    #Second element of the tuple is the grouped/categorized dataframe_object





