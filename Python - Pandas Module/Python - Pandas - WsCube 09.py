import numpy as np
import pandas as pd

# =====  Handling Missing Data (Replace and Interpolate)
                            #Notes: Some method returns the edited dataframe_object, while others change the originar dataframe_object, be cautious

#=== REPLACE ===
csv1 = pd.read_csv("E:\\Programming\\Python projects\\Python - Pandas Module\\My_CSV_4.csv")    #Reading csv file
print(csv1)

#Replacing any value (like find and replace in ms word/excel)
csv2 = csv1.replace(to_replace = 10, value = 1000)  #-- dataframe_object.replace(to_replace=the_value_you_wanna_replace, value=the_new_value) --
print(csv2)

csv3 = csv1.replace(to_replace = [91, 30, 55], value = 99999)   #Replacing multiple data
print(csv3)

csv4 = csv1.replace([100, 300], 7878787)    #You can also pass the parameter without the name of the argument
print(csv4)


#Replacing any value of particular columns
csv5 = csv1.replace({"header2" : [53, 54], "header1": 20}, 9999)  #By the dictionary as --to_replace-- parametervalue, pass the column header as key and to be replaced datas(single or as list) as dictionary value
print(csv5)


#Replacing any value with its previous or after value, both along row or column (axis=0 or axis=1), by default axis=0 i.e row wise
csv6 = csv1.replace(54, np.nan).ffill()      #-- dataframe_object.replace(the_value_to_be_replace, np.nan).ffill() -- ffill means forward fill, it will replace its value with its previous row value of the same column
print(csv6)                                          # -- np.nan -- is missing value(NaN) ,  as -- ffill() -- method works only on NaN value, so we first replaced the value with np.nan

csv7 = csv1.replace(54, np.nan).ffill(axis = 1)      # it will replace its value with its previous columm value of the same row
print(csv7)

csv8 = csv1.replace(54, None).bfill()      #-- dataframe_object.replace(the_value_to_be_replace, np.nan).bfill() --  bfill means backward fill, it will replace its value with its after row value of the same column
print(csv8)

csv9 = csv1.replace(54, np.nan).bfill(axis = 1)      # it will replace its value with its after column value of the same row,, -- None -- Keyword and np.nan does the same task,s
print(csv9)



#Limit the value to be replaced on each row or each column (axis=0 or axis=1, by default it is axis 0)
csv10 = csv1.replace(np.nan, 99999, limit = 3)  #Limiting the value to be replaced (though --limit-- kw in replace --method-- will not be available in future version of pandas, no alternative still found)
print(csv10)



#Replacing the original dataframe_object value instead of return a copy of edited dataframe_object
csv11 = csv1.copy()                 #We don't want to edit the original dataframe object so we made a copy
csv11.replace(55, 999999, inplace=True)     #Replaced the dataframe_object value with -- inplace=True -- rather than returning a copy of edited dataframe_object
print(csv11)





















#INTERPOLATE
        #Interpolate method only works on numerical values, alphabetic value doesn't change
        #It fills all the NaN values of the dataframe_object with random number but the random number is relevant linearly(by default method="linear" i.e linear) to the previous and after value of the NaN data 
        # By default axis=0 (along row) that is relevancy will be maintained with the previous and after row of the same column
        # You can also use -- limit=any_integer -- parameter to limit the data to be interpolated in each column or row
        # You can also use -- limit_direction="forward" -- or -- limit_direction="backward" -- or -- limit_direction="both" to set the direction of limit from top(column)/left(row) , or, from bottom(column)/left(row), or, from both/side
        # You can also use -- limit_area="inside" -- or -- limit_area="outside" -- to select the most outer/inner row or column, 
        # With -- inplace=True -- you can change the original dataframe_object instead of returning the modified dataframe object, by default -- inplace=False --

csv12 = csv1.interpolate(method = 'linear')     #You don't need to pass the parameter method here, as by default -- method='linear'
print(csv12)                                       #By default axis=0

csv13 = csv1.interpolate(axis = 1)      #To interpolate along column, all column should have same data_type (numerical)
print(csv13)

csv14 = csv1.copy()
csv14.interpolate(limit = 2, limit_area = "inside", limit_direction = "forward", inplace = True, axis = 1)
print(csv14)






