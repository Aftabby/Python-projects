# Pandas has a reference to both 'Panel data' and 'Python data analysis'


# ============ Data Structure in Pandas ===============
# Three data structures in pandas:
                # Series: 1-D labeled arrays pd.Series(data)
                # DataFrames: 2-D data structure with columns, much like a table
                # Panel: A 3-D container of data

import pandas as pd


list1 = [3, 4, 5, 6, 7, 8]

series1 = pd.Series(list1)  # Series is a single dimensional data structure array, you can create series not only with list but also dictionary, tuple etc.
print(series1)              # It contains both the value and its index number
print(type(series1))
print(series1[3])           # We can access the value by its index number


#Changing the index number
list2 = [5, 6, 7, 8]
index1 = ['a', 's', 'd', 'f']

series2 = pd.Series(list2, index = index1)      #Now the index will be -- a, s, d, f --
print(series2)


#Changing the data type of the value
series3 = pd.Series(list2, dtype = "float")
print(series3)

#Naming your data
series4 = pd.Series(list2, name = "My first series")
print(series4)

#Creating series with dictionary and tuples
dict1 = {"name": ["python", "java", "c++", "c"], "popularity" : [ 11, 12, 13, 14], "rank": [1, 2, 3, 4]}
series5 = pd.Series(dict1)
print(series5)


tuple1 = (33, 44, 55, 66)
series6 = pd.Series(tuple1)
print(series6)


#Creating multiple row in series with the same value  --- with the help of index number
value1 = 12
series7 = pd.Series(value1, index = [1, 2, 3, 4, 5, 6])     #It will create all the index position with the same value
print(series7)


#Adding to series of different shape
                    # It is not possible in numpy (broadcasting error), but in series(pandas) the extra data are added as NaN
                    #NaN (Not a Number) - It means missing data
list3 = [1, 2, 3, 4, 5, 6]
list4 = [1, 3, 4]

series8 = pd.Series(list3)
series9 = pd.Series(list4)

series10 = series8 + series9 
print(series10)



