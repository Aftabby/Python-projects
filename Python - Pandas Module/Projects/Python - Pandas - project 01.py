import pandas as pd

#===============================================  Data Analysis Warmup Exercises  =================================

dict1 ={'Name':['Priyang','Aadhya','Krisha','Vedant','Parshv',
                'Mittal','Archana'],
                'Marks':[98,89,99,87,90,83,99],
                'Gender':['Male','Female','Female','Male','Male',
                         'Female','Male']
               }
dframe1=pd.DataFrame(dict1)
print(dframe1)






#Display Top 3 Rows of the Dataset
print("\nDisplay Top 3 Rows of the Dataset")

top1 = dframe1.head()                  #If you don't pass any parameter into head method, by default it returns the top 5 rows of the data set
print(top1)

top2 = dframe1.head(3)                  #If you pass any integer value as parameter, it returns that number of rows from the top
print(top2)




#Check Last 3 rows of the Dataset
print("\nCheck Last 3 rows of the Dataset")

last1 = dframe1.tail()                  #If you don't pass any parameter into tail method, by default it returns the last 5 rows of the data set
print(last1)

last2 = dframe1.tail(3)                  #If you pass any integer value as parameter, it returns that number of rows from the last
print(last2)





#Find Shape of the Dataset (Number of rows, Number of columns)
print("\nFind Shape of the Dataset (Number of rows, Number of columns)")

shape1 = dframe1.shape          #Shape is not a method, it is an attribute of dataframe_object ,, This attribute returns the shape in tuple data type
print(shape1)







#Get all the information about the Dataset
print("\nGet all the information about the Dataset)")

info1 = dframe1.info()
print(info1)





#Check Null Values in the Dataset
print("\nCheck Null Values in the Dataset")

null1 = dframe1.isnull()            #Returns the whole data set with boolean values, if null then True, otherwise False
print(null1)


null2 = dframe1.isnull().sum()      #Calculating the null value column-wise, by default axis=0
print(null2)

null3 = dframe1.isnull().sum(axis = 1)      #Calculating the null value row-wise
print(null3)







#Get overall statistic about the dataset
print("\nGet overall statistic about the dataset")

stats1 = dframe1.describe()         # By default Returns the statistics of numerical column only, here -- 25%  numerical_value -- means 25% of the values is below that numerical_value ,, same goes with 50% and 75%
print(stats1)
print(type(stats1))


stats2 = dframe1.describe(include = "all")   #Returns the statistics of all the columns
print(stats2)








#Find unique values from a column and also number of unique value (In here, gender column)
print("\nFind unique values from a column (In here, gender column)")

unique1 = dframe1["Gender"].unique()        #It will return the unique value (Male, Female)      
print(unique1)


unique2 = dframe1["Gender"].nunique()       #It will return the number of unique values exist
print(unique2)









#Display count of unique values in a column (in here gender column)
print("\nDisplay count of unique values in a column (in here gender column)")

unique3 = dframe1["Gender"].value_counts()
print(unique3)










#Find total Number of Students Having Marks between 90 to 100 (Inclusive) using -- between -- method
print("\nFind total Number of Students Having Marks between 90 to 100 (Inclusive) using -- between -- method")

range1 = dframe1["Marks"] >= 90         #It will return series_object as the marks column with boolean value based on the condition mentioned( >= 90)
print(range1, type(range1))       

range2 = dframe1[range1]        #You already know if we pass a list/series_object of boolean values(which has elements equal to dataframe's row number) as it's index position, we get only the rows that was True in the list,, guess what? same things happen for also the  series_object not only list 
print(range2)



range3 = (dframe1["Marks"] >= 90) & (dframe1["Marks"] <= 100)       #Combining the two conditions, always use parenthesis while declaring multiple conditions, and why they used -- &  -- instead of -- and -- I've no idea
print(range3)                                                                       #This is because ‘and‘ tests whether both expressions are logically True while ‘&’ performs bitwise AND operation - from google

range4 = dframe1[range3]    #Just like what we did with range2
print(range4)


total1 = len(range4)            #We have counted the total number of students without using -- between -- method,, now let's do it with between method
print("\n\nTotal number of students having mark between 90 to 100: ", total1) 


range5 = dframe1["Marks"].between(90, 100)          #In -- between -- method both the values are inclusive,, it works same like what we assigned in the variable -- range3 --,, it returns series object with boolean values
print(range5, type(range5))

total2 = sum(range5)    #The sum will return the output based on how many True values are in the series_object
print("\n\nTotal number of students having mark between 90 to 100: ", total2)       #Found it with between method







#Find minimum, maximum and Average of the marks column
print("\nFind minimum, maximum and Average of the marks column")

min1 = dframe1["Marks"].min()
print("Minimum:", min1)

max1 = dframe1["Marks"].max()
print("Maximum:", max1)

mean1 = dframe1["Marks"].mean()
print("Average of all marks:", mean1)









#Use your custom method / function in a column of dataframe object, using -- apply() -- method
print("\nUse your custom method / function in a column of dataframe object")
def half_marks(mark):
    return mark/2           #You can also use the floor division here if you want integer value -- return mark//2 --

custom1 = dframe1["Marks"].apply(half_marks)        #Remember as a parameter in the -- apply() -- method, always pass your function without parenthesis, because we are not calling the function
                                                        #Thus the function will be applied for every value(row) of that column and returned as a series_object

print(custom1, type(custom1))


dframe1["Half_Marks"] = custom1         #We added an extra column to the original dataframe_object, with the column_name "Half_Marks"
print(dframe1)


custom2 = dframe1["Marks"].apply(lambda mark : mark/2)      #Same thing what we did in -- custom1 -- but with lambda / anonymous function
print(custom2)

len1 = dframe1["Name"].apply(len)   #Finding out the length of the name of each of the student's name, -- apply() -- method returns the series_object applying the function for each of the value
print(len1)                                 #-- len -- is a built-in function of python











#Use map function to a column
print("\nUse map function to a column")
map1 = dframe1["Gender"].map({'Male' : 1, "Female" : 0})    #In -- series_object.map() -- method, you pass a dictionary, If any -- key -- of that dictionary matches any value of the series, the value of the series gets replaced by the dict_value of that particular dictionary -- key -- ,, and returns a new series with replaced value 
print(map1)                                                     # --  dictionary_name[column_name] -- returns a series

dframe1["Male_Female"] = map1       #Adding a new column to the existing dictionary
print(dframe1)












#Drop the column(s)
print("\nDrop the column(s)")
dframe2 = dframe1.drop(["Male_Female", "Half_Marks"], axis = 1)       #As we are working along the column axis, so -- axis=1 -- ,, To drop one column no need to pass it in the list, just put the column name as the parameter
print(dframe2)                                            # Dropping doesn't mean deleting,, to modify (delete column) of the existing dataset pass -- inplace=True --,, 







#Print name of the columns
print("\nPrint name of the columns")
columns1 = dframe1.columns      # -- columns -- is an attribute not a method
print(columns1)







#Print row indexes
print("\nPrint row indexes")
index1 = dframe1.index          # -- index  -- is an attribute not a method
print(index1)











#Sort the dataset on Marks column
print("\nSort the dataset on Marks column")
sort1 = dframe1.sort_values(by = "Marks")       #By default ascending
print(sort1)

sort2 = dframe1.sort_values(by = "Marks", ascending = False)    #Now descending
print(sort2)

sort3 = dframe1.sort_values(by = ["Marks", "Gender"])   #Sorting on base of two columns, first on Marks column, If marks has similar value for more than one row, then for those similar values it will sorted according to Gender column
print(sort3)











#Display two columns (Name and Marks) only for Female Students
print("\nDisplay two columns (Name and Marks)")

#Below two lines are same
column2 = dframe1["Gender"] == "Female"     #It will return a series_object of boolean of same rows, where for all the "Female" value will be True, and for other gender_values the boolean value will be False
#column2 = dframe1["Gender"].isin(["Female"])
print(column2)

column3 = dframe1[column2]
print(column3)              #Printing the dataset only of gender female



column4 = column3[["Name", "Marks"]]        #Here column name should be passed a list if it is more than one column_name, otherwise it will take it as more than one parameter
print(column4)










