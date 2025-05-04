import pandas as pd
import numpy as np

#========== Merging and Concat ===========
                                    #--merge-- works based on common column of two -- pandas_objects -- (series, dataframe etc),
                                    #whereas --concat-- just adds up -- pandas_objects -- passed into it

dict1 = {"header1" : [10, 20, 30, np.nan, 50, None, 70],         # -- np.nan -- None -- NaN -- are the same thing, missing values (not a number)
         "header2" : [51, np.nan, 53, 54, 55, np.nan, 57],
         "header3" : [None, 12, 13, np.nan, 15, None, 17],
         "header4" : [100, 200, 300, 400, 500, None, 700],
         "header5" : [np.nan, np.nan, np.nan, None, None, None, np.nan],
         "header6" : [91, 92, 93, 94, 95, None, 97]
         }

dframe1 = pd.DataFrame(dict1)
print(dframe1)



#=== MERGE ===
dict2 = {"A" : [1, 2, 3, 4],
         "B" : [10, 20, 30, 40]}
dframe2 = pd.DataFrame(dict2)
print(dframe2)

dict3 = {"A" : [1, 2, 3, 99],
         "C" : [50, 60, 70, 80]}
dframe3 = pd.DataFrame(dict3)
print(dframe3)

dframe4 = pd.merge(dframe2, dframe3, on = "A")       # -- pd.merge(dataframe1, dataframe2, on=column_header_of the_common_column_of_two_dataframes) , 
print(dframe4)                                          #merge method merges two dataframes together, based on a single common column(both data and header), which is passed through the parameter -- on -- if the common column has some different datas in two dataframes, only the row with common data will be merged

dframe5 = pd.merge(dframe3, dframe2, on = "A")      # Variation of merging, sometimes when you have only one common column_header in both the dataframes then you don't need to pass the the -- on -- parameter, if there is more than one common column_header in the two dataframes then you should specify -- on -- parameter
print(dframe5)



#Merging where one dataframe will fully exist, and other will get merged based on the common column, parameter -- how -- 
    #n.b: by default the value of -- how -- parameter is "inner" i.e not merge the uncommon rows
dframe6 = pd.merge(dframe2, dframe3, how = "left")      #left (here, dframe2) will fully exist whereas in the right dataframe(here, dframe3) the common row(at least by one column) will get merged only
print(dframe6)              #Sometimes you don't need to pass the -- on -- paramter, try with above examples

dframe7 = pd.merge(dframe2, dframe3, how = "right") #right (here, dframe3) will fully exist whereas in the left dataframe(here, dframe2) the common row(at least by one column) will get merged only
print(dframe7)              #Sometimes you don't need to pass the -- on -- paramter, try with above examples

dframe8 = pd.merge(dframe2, dframe3, how = "outer", indicator = True) #Outer means both right and left, that is common and uncommon,, by -- indicator=True -- we can check which of the left or dataframe value is present in the merged dataframe
print(dframe8)


#Getting both dataframe's common column value separately, instead of getting the common column of two dataframes merged into one
dframe9 = pd.merge(dframe2, dframe3, left_index = True, right_index = True, suffixes = ["name", "id"])     #With -- left_index=True -- we got the separate value of the common column of two dataframes, same goes for the -- right_index -- as well
print(dframe9)                                                                                                  # With -- suffix=list_name/tuple_name -- we added extra name after the original name, to the merged dataframe separated (but common) column header










# ===  CONCAT ===
    #short form of concatenation

list1 = [1, 2, 3, 4]
series1 = pd.Series(list1)               #Creating series, 1-D data structure
list2 = [11, 22, 33, 44]
series2 = pd.Series(list2)

print(series1)
print(series2)

#Concatenating multiple series_object
series3 = pd.concat([series1, series2])           # -- pd.concat(list_of_pandas_objects) -- It concatenates all the series_object passed into it in a list (keeping the column number fixed, and adding up the rows as by default --axis=0--)
print(series3)                                          #N.B: -- concat -- function takes objects in a list


#Concatenating multiple dataframe_object along the row (as by default, -- axis=0 --)
dframe10 = pd.concat([dframe2, dframe3])            # -- pd.concat(list_of_pandas_objects) -- It concatenates all the dataframe_object passed into it in a list (keeping the column number fixed, and adding up the rows, as by default --axis=0--)
print(dframe10)                                          #N.B: -- concat -- function takes objects in a list


#Concatenating multiple dataframe_object along the column
dframe11 = pd.concat([dframe2, dframe3], axis = 1)            # -- axis=1 -- that means it will concatenate along the column
print(dframe11) 


#Concatenating only the least or max number of data rows/column present among all the uneven(unmatched) shaped(not all of the same shape) dataframes
dict4 = {"A" : [1, 2, 3 ],
         "B" : [10, 20, 30]}
dframe12 = pd.DataFrame(dict4)           #dataframe with values of three rows
print(dframe12)

dict5 = {"C" : [1, 2, 3, 99, 100],
         "D" : [50, 60, 70, 80, 90]}
dframe13 = pd.DataFrame(dict5)           #dataframe with values of five rows
print(dframe13)

dframe14 = pd.concat([dframe12, dframe13], join = "inner", axis = 1)  #With -- join="inner" -- we will only concatenate the least number data rows available among all the dataframe_objects
print(dframe14)                                                             #You can also try it with -- axis=0 (along row) -- , for that you don't have to pass anything because by default it is -- axis=0 --

dframe15 = pd.concat([dframe12, dframe13], join = "outer", axis = 1)  #With -- join="outer" -- we will only concatenate the max number data rows available among all the dataframe_objects, the unavailable data will be reffered as NaN
print(dframe15)                                                             #You can also try it with -- axis=0 (along row) -- , for that you don't have to pass anything because by default it is -- axis=0 --








