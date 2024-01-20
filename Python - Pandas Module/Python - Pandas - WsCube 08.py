import pandas as pd

# ===== Handling Missing Data (DropNA & FillNA)  =======

    #Let's say you have a csv file, where some of the datas are missing or empty(NaN), we'll learn how to put any_value in that blank space, or remove that blank data
        #Notes: Some method returns the edited dataframe_object, while others change the originar dataframe_object, be cautious
csv1 = pd.read_csv("E:\\Programming\\Python projects\\Python - Pandas Module\\My_CSV_4.csv")    #Reading csv file
print(csv1)

# == DROPNA == 
#Dropping the row which contains any number of NaN value,  with dropna() method
csv2 = csv1.dropna()    #It will return the dataframe/csv object dropping rows that contains NaN value, by default it will take axis=0(along the row)
print(csv2)                 #If there is any column which entire value is NaN(value of all element of that column), then you will get an empty dataframe object


#Dropping the column which contains NaN value with dropna() method
csv3 = csv1.dropna(axis = 1)    #It will return dataframe/csv object dropping column that contains NaN value, the parameter is axis=1(which means along column axis)
print(csv3)                         #If there is any row which entire value(value of all element of that row) is NaN, then you will get an empty dataframe object



#Dropping the row basesd on any data that is NaN in the row, or -- all -- data in the row is NaN
csv4 = csv1.dropna(how = "any")     # Though by default the value of the parameter --how -- is -- any -- , check csv2, it will drop the row which has any NaN value, 
print(csv4)                                #If there is any column which entire value in NaN, then you will get an empty dataframe object
csv5 = csv1.dropna(how = "all")     #It will only drop the row in which all the data is NaN(missing)
print(csv5)


#Dropping the column based on any data that is NaN in the column, or -- all -- data in the column is NaN
csv6 = csv1.dropna(how = "any", axis = 1)     # Though by default the value of the parameter --how -- is -- any -- , check csv3, it will drop the column which has any NaN value 
print(csv6)                                         #If there is any row which entire value in NaN, then you will get an empty dataframe object
csv7 = csv1.dropna(how = "all", axis = 1)     #It will only drop the column in which all the data is NaN(missing)
print(csv7)


#Dropping the row based on NaN value of a particular column, other column's NaN value stays unaffected
csv8 = csv1.dropna(subset = "header3")  #The parameter subset=column_header
print(csv8)


#Dropping row based on the condition, minimum number of NaN(Null value) values must be present in the row -- I'm not sure how it works
csv9 = csv1.dropna(thresh = 2)              #Google it
print(csv9)








#== FILLNA ==
print("\n\n============= FILLNA  ===========")
#Replacing all the NaN value in the dataframe/csv object with any_value
csv10 = csv1.fillna("Filled Value")    # -- dataframe_object.fillna(replaced_new_value) -- 
print(csv10)
csv16 = csv1.copy()
csv16.fillna(999999, inplace = True)    #The difference between this way to fill with an -- inplace=True -- parameter is, it will change the original version of the dataframe instead of  return the modified dataframe.
print(csv16)                                                # -- inplace=True -- doesn't copy the data and return the manupulated version like other method and parameter, it manipulates/changes the data



#Replacing all the NaN value in particular_columns in the dataframe/csv object with any_value
csv11 = csv1.fillna({"header2" : "H2 Filled Value", "header6" : "H6 Filled Value"})
print(csv11)


#Replacing the NaN value with each of its previous or after row value (from the same column) , by default the axis=0
csv12 = csv1.ffill()    #dataframe_object.ffill(), ffill = forward fill, means the NaN value will take its previous row value of the same column
print(csv12)

csv13 = csv1.bfill()    #dataframe_object.bfill(), bfill = backward fill, means the NaN value will take its after row value of the same column
print(csv13)


#Replacing the NaN value with each of its previous or after column value (from the same row), by default the axis=0
csv14 = csv1.ffill(axis = 1)    #dataframe_object.ffill(axis=1), axis=1(means along the column) , the NaN value will take its previous column value of the same row
print(csv14)
csv15 = csv1.bfill(axis = 1)    #dataframe_object.bfill(), axis=1(means along the column), the NaN value will take its after column value of the same row
print(csv15)


#Replacing upto a fixed number of NaN value in each row or each column, as here by default axix=0 i.e row wise
csv16 = csv1.fillna("poishumaik", limit = 2)    # -- limit -- parameter takes the number of how many NaN value you want to replace each row of every column ( axis=0 works along row, so limit_number of rows in every column)
print(csv16)
csv17 = csv1.fillna("Dhishumaik", limit = 2, axis = 1) #-- limit -- parameter takes the number of how many NaN value you want to replace in each column of every row (as we passed axis=1, so works along column, limit_number of column in every rows)
print(csv17)


