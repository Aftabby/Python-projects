import pandas as pd
import numpy as np

# =======  Join & Append ====

dict1 = {"A" : [1, 2, 3, 4],
         "B" : [10, 20, 30, 40]}
dframe1 = pd.DataFrame(dict1)               #dataframe with values of four rows
print(dframe1)

dict2 = {"C" : [5, 55, 555, 5555],
         "D" : [50, 60, 70, 80]}
dframe2 = pd.DataFrame(dict2)               #dataframe with values of four rows
print(dframe2)

dict3 = {"E" : [6, 66],
         "F" : [100, 200]}
dframe3 = pd.DataFrame(dict3)               #dataframe with values of two rows
print(dframe3)




# ===  JOIN  ===
                # In --join() -- method, if there is a common column_header between two dataframe_objects, then you will find an error of overlapping (suggested to use --merge -- method in that case), at that scenerio you can use --lsuffix-- or --rsuffix-- parameter

#Joining two dataframe_objects with same number of rows
dframe4 = dframe1.join(dframe2)         # -- dataframe_object_01.join(dataframe_object_02) --
print(dframe4)


#Joining two dataframe_objects with different(uneven) number of rows
dframe5 = dframe1.join(dframe3)             #if the --dframe1-- has more rows than --dframe2-- the extra values will be returned as NaN -- how="outer" --, in vice versa condition the extra value will not be joined -- how="inner" --
print(dframe5)

dframe6 = dframe3.join(dframe1)
print(dframe6)                              #It only join the number of rows available in dframe3, we can make it join all the rows by passing the parameter -- how="outer"  -- (you already know how --how-- parameter works)

dframe7 = dframe3.join(dframe1, how = "outer")     #Now it joins max number of rows that is available between the two dataframe_objects
print(dframe7)                                          #You can also pass -- how="left" -- or -- how="right" -- then according to the left(in first case) dataframe or right(in second case) dataframe available rows, the function(join()) will join the rows


#Joining two dataframe_objects with common column_header name
dict4 = {"A" : [1, 2, 3, 4],
         "G" : [10, 20, 30, 40]}
dframe8 = pd.DataFrame(dict4)               #dataframe with values of four rows
print(dframe8)

dframe9 = dframe8.join(dframe1, lsuffix = "_left", rsuffix = "_right" )     #As both the -- dframe8 -- and -- dframe1 -- has a common column header name -- "A" -- , the -- join() -- method will raise an error as it cannot join having two column_header name of different dataframe_objects with same value
print(dframe9)                              #To resolve the error, we have to add suffix to the common column header name, for adding suffix(an extra name after the original name) to the right dataframe_object(here dframe1) use the parameter -- lsuffix --
                                                    # For adding suffix to the left dataframe_object(here dframe8) use the parameter -- rsuffix -- ; if the value of both the suffix parameter is the same , it will still work



















# ===  APPEND   ===
                    
    #As of pandas 2.0, append (previously deprecated) was removed.
    #You need to use concat instead (for most applications)

    #Tips:
    #Using append or concat repeatedly is not a good idea (this has a quadratic behavior as it creates a new DataFrame for each step).
    #In such case, the new items should be collected in a list, and at the end of the loop converted to DataFrame and eventually concatenated to the original DataFrame.