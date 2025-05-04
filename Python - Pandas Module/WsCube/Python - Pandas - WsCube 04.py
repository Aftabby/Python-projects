import pandas as pd

# ==== Insert, Slicing and Deleting Data in Pandas =====

#INSERT
    # dataframe_name.insert() has three parameters, first- the column_index_number where you wanna insert (not the column headline)
                                                    # second -  the name of the new column (column headline)
                                                    # third - the data itself (it accepts list as data), the number of element of data should be equal the the existing column numbers of data
dict1 = {"A": [1, 2, 3, 4], "B": [5, 6, 90, 8]}
dframe1 = pd.DataFrame(dict1)
print(dframe1)

list1 = [10, 20, 30, 40]
dframe1.insert(1, "New Column", list1)        #dataframe_name.insert(index, column_name, data), as the data it takes a list as you are already mentioning the new column headline in the insert method parameter (no need of a dictionary)
print(dframe1)

#Copying one column to another column with insert method
#Below two lines work the same, the only differene is in the second line you can't define the index of new column, it will just append
dframe1.insert(2, "Copy of A", dframe1["A"])
dframe1["Copyyyy of A"] = dframe1["A"]            #The column headline must be unique, that's why copy and copyyyy
print(dframe1)

#Copying a sliced column to another column by slicing
dframe1["Slicing of B"] = dframe1["B"][:3]          #The rest of the value in the new column will be NaN (Not a Number i.e missing values)
print(dframe1)
















#DELETE
    #Using the KW -- del -- or using -- dataframe_name.pop() -- the pop method takes the parameter column_headline of the column you want delete
        #This function deletes the entire column and return the deleted column as a data structure of panda.Series

deleted_column = dframe1.pop("New Column")      #dataframe_name.pop(Column_name(headline))
print(deleted_column, type(deleted_column))
print(dframe1)


#Using del keyword
del dframe1["Copyyyy of A"]       
print(dframe1)

