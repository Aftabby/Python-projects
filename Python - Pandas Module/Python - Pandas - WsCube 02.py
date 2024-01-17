import pandas as pd

#===========================Data Structure (DataFrame) ==========================================


    #DataFrame is a 2D array data structure in python
    #You can create dataframe with a list as well as a dictionary

#Creating DataFrame with a list
list1 = [10, 11, 12, 13]
dframe1 = pd.DataFrame(list1)
print(dframe1)
print(type(dframe1))

list2 = [[1, 2, 3, 4, 5], [11, 12, 13, 14, 15]] #Each of the single list will be a row in the dataframe, as here there will be 2 rows
dframe5 = pd.DataFrame(list2)
print(dframe5)

#Creating DataFrame with a dictionary
dict1 = {"a" : [1, 2, 3, 4, 5], "b" : [5, 6, 7, 8, 9], "c" : [10, 11, 12, 14, 15], 1 : ["a", "b", "c", "d", "e"]}      
                                    #Imp: When you a create a dataframe with the help of a dictionary, the value of each of the key should be same otherwise you might to get an error
                                            #as each of the key of the dictionary becomes the headline i.e. column, and each of the element of the value of dictionary becomes the row in the dataframe
dframe2 = pd.DataFrame(dict1)
print(dframe2)

#Creating dataframe with particular column/columns(keys) from the dictionary
dframe3 = pd.DataFrame(dict1, columns = ["a", 1])
print(dframe3)

#Changing the index number of the dataframe -- by default it is (0, 1, 2, 3, ...)
dframe4 = pd.DataFrame(dict1, index = ["a", "s", "d", "f", "g"])    #The no. of values of the index must match with the total no. of rows in the dataframe
print(dframe4)

#Accessing particular value from the dataframe
value1 = dframe4["a"]          #Accessing the full column
value2 = dframe4["a"]["s"]     #Accessing a particular value from customized index number
value3 = dframe3["a"][3]       #Accessing a particular value from dframe3 which has the default index number

print(value1)
print(value2)
print(value3)


#Creating DataFrame with series
dframe6 = {"key1" : pd.Series([1, 2, 3, 4]), "key2" : pd.Series([5, 6, 7, 8])}      #You can create dataframe with multiple series, as series is 1-D data structure, and DataFrame is 2-D data structure
print(dframe6)

