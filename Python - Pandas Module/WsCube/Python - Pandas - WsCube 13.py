import pandas as pd

# ==========  Pivot Table and Melt  ===========
                                    #These two functions are used to reshape pandas dataframe_objects
                                    #Melt is a function, whereas pivot and pivot_table is a method



#====  MELT  ====
dict1 = {"Test" : [1, 2, 3, 4, 5],
         "Eng_Score" : [60, 70, 80, 90, 100],
         "Math_Score" : [51, 52, 53, 54, 55]}
dframe1 = pd.DataFrame(dict1)            
print(dframe1)          


#Reshaping a dataframe_object table from horizontally to vertically ( that is, each row will contain only one value, with its column_header)
dframe2 = pd.melt(dframe1)
print(dframe2)


#Reshaping a dataframe_object table from horizontally to vertically keeping particular columns always present in every row
dframe3 = pd.melt(dframe1, id_vars = ["Test"])    # -- id_vars = list_of_column_headers -- this parameter makes the particular column present(more like an id variable) in the dataframe_object in every row, the columns are passed in a list
print(dframe3)


#Naming the column of column_headers after reshaping a dataframe_object from horizontally to vertically
dframe4 = pd.melt(dframe1, var_name = "Subjects")       #The column_name of which was by default "variable"
print(dframe4)


#Naming the column of all_values after reshaping a dataframe_object from horizontally to vertically
dframe5 = pd.melt(dframe1, value_name = "Scores")      #The column_name of which was by default "value"
print(dframe5)














# =====  PIVOT & PIVOT_TABLE =======
dict1 = {"Test" : [1, 2, 3, 4, 5, 6],
         "Stdnt_name" : ["abc", "def", "ghi", "jkl", "mno", "pqr"],
         "Eng_Score" : [60, 70, 80, 90, 100, 110],
         "Math_Score" : [51, 52, 53, 54, 55, 56]}
dframe6 = pd.DataFrame(dict1)            
print(dframe6)


#Arranging the dataframe_object in a way where one column_value will work as a row_index and another column_value will work as a column_header/column_index
dframe7 = dframe6.pivot(index = "Test", columns = "Stdnt_name")     #Here -- index=column_header -- the values of the column_header will be working as the row_index
print(dframe7)                                                         # -- columns=column_header -- the values of the column_header will be working as the new column_header


#Getting the value of only particular columns in -- pivot -- method
dframe8 = dframe6.pivot(index = "Test", columns = "Stdnt_name", values = "Eng_Score")
print(dframe8)


#Working with -- pivot_table -- method
dframe9 = dframe6.pivot_table(index = "Stdnt_name", columns = "Test", aggfunc = "mean")         #Not Explained
print(dframe9)

dframe10 = dframe6.pivot_table(index = "Stdnt_name", columns = "Test", aggfunc = "sum")         #Not Explained
print(dframe10)

dframe11 = dframe6.pivot_table(index = "Stdnt_name", columns = "Test", aggfunc = "sum", margins = "True")         #Not Explained
print(dframe11)



