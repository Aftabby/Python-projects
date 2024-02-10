import pandas as pd
import numpy as np

#Data Analysis on San Fransisco city salary dataset- YT: Data Thinkers
#Data sheet link: https://www.kaggle.com/datasets/kaggle/sf-salaries


df1 = pd.read_csv("Salaries.csv")           #To read csv file and return it as a panda_object



#Display first and last 10 rows of the dataset
head1 = df1.head(10)
print(head1)

tail1 = df1.tail(10)
print(tail1)





#Find shape of the dataset
shape1 = df1.shape  #not method, an attribute,, #Returns tuple (row, column)
print(f"Rows: {shape1[0]}, Column: {shape1[1]}")       





#Getting information about the dataset like total number rows, column, datatypes
info1 = df1.info()              
print(info1)

info2 = df1.describe()          #Statistical information of the dataset
print(info2)







#Check Null Values in the dataset
null1 = df1.isnull()        #Returns True if there is Null, else False, returns dataframe_object
print(null1)

null2 = df1.isnull().sum()      #All True values are added column-wise, i.e all Null values
print(null2)

print(True + True + False)      #True is count as 1, False as 0




#Drop ID, Notes, Agency and Status Columns
column1 = df1.columns           #not method, an attribute
print(column1)                  #Checking the column name first to understand in which column we have to perform the operation

drop1 = df1.drop(["Id", "Notes", "Agency", "Status"], axis=1)   #by default it works row-wise(axis=0), you can pass the parameter -- inplace=True -- if you want to modify the original dataset(dataframe_object)
print(drop1, "\n4 less columns this time" ,drop1.shape)


#df1.drop(["Id", "Notes", "Agency", "Status"], axis=1, inplace=True) #We are dropping these columns from original dataset(dataframe_object), as we don't need them for data analysis and these will increase the burden of machine, algorith and decrease efficiency
                                                                                #For no reason, I commented it out












#Get Overall Statistics about the datframe
describe1 = df1.describe()              #Numerical columns only
print(describe1)


describe2 = df1.describe(include="all")     #All columns, numerical and categorical
print(describe2)












#Find occurance of the employee names Top 5
column2 = df1.columns           #not method, an attribute
print(column2)                  #Checking the column name first to understand in which column we have to perform the operation


occ1 = df1["EmployeeName"].value_counts().head()
print(occ1)














#Find the number of unique job titles
column3 = df1.columns           #not method, an attribute
print(column3)                  #Checking the column name first to understand in which column we have to perform the operation

unique1 = df1["JobTitle"].unique()          #It will only return the unique value
print(unique1)


unique2 = df1["JobTitle"].nunique()         #It will return the number of unique value present
print(unique2)




















#Total number of job titles contain captain

print(len(df1))
job1 = df1["JobTitle"].str.contains("captain", case=False)      #By default, case=True (case sensitive),, It will return the series_object of boolean values based on the condition


job2 = len(df1[job1])             #either use len() function or also you can use -- count() -- method on it ,, also you can use the -- sum() -- method on the boolean series object
print(job2)








#Display All the Employee Names From Fire Department
column4 = df1.columns           #not method, an attribute
print(column4)                  #Checking the column name first to understand in which column we have to perform the operation


employ1 = df1["JobTitle"].str.contains("Fire Department", case=False)   #Returns boolean value series_object
print(employ1)

employ2 = df1[employ1]["EmployeeName"]
print(employ2)
















#Find Minimum, Maximum and Average of Basepay
column5 = df1.columns           #not method, an attribute
print(column5)                  #Checking the column name first to understand in which column we have to perform the operation

#max1 = df1["BasePay"].max()    #These methods won't work as basepay column contains some strings as well, so use -- describe() -- method here to find out min,max,mean
#print(max1)

#min1 = df1["BasePay"].min()
#print(min1)

#mean1 = df1["BasePay"].mean()
#print(mean1)























#Replace 'Not Provided' in EmployeeName column to NaN

fillna1 = df1["EmployeeName"].fillna("Not Provided")    #First we filled all NaN values with Not Provided
print(fillna1)

fillna3 = df1["EmployeeName"].replace(np.nan, "Not provided")   #It also works same as the -- .fillna -- method above , as there is np.nan as first parameter
print(fillna3)


fillna2 = df1["EmployeeName"].replace("Not provided", np.nan)   #Getting it back to NaN value
print(fillna2)











#Drop the rows having only 3 missing values
drop2 = df1.isnull().sum(axis=1)        #As -- sum -- works on column by default(axis=0),, so we changed it into rows by (axis=1) ,, inverted rule here - no idea why
print(drop2)                                #Returns a numerical series_object

drop3 = drop2 == 3           #Returns boolean value series_object based on the condition
print(drop3)

drop4 = df1[drop3]      # Returns Only the rows with 3 NaN values
print(drop4)

drop5 = df1.drop(drop4.index, axis=0)       #Dropping the row with -- drop() -- method takes rows_index / column_names as first parameter but here row_index,, because by default the axis=0(i.e row wise)
print(drop5)                                                # To make changes permanent pass -- inplace = Trues --


drop6 = drop5.isnull().sum(axis=1)          #To check that the rows with 3 missing values are now dropped
print(drop6)










#Find Job Title of ALbert ParDini and How much Albert Pardini make (include benefites)
column6 = df1.columns           #not method, an attribute
print(column6)                  #Checking the column name first to understand in which column we have to perform the operation

job3 = df1["EmployeeName"].str.upper()  == str.upper("Albert Pardini")  #We don't know the uppercase or lowercase of name exist in dataset, so we uppercased both side string to check,, We could have also use -- str.contains("Text", case=False) --
print(job3)                                                                 #Returns boolean series object


job4 = df1[job3]["JobTitle"]            #Job Title of Albert pardini
print(job4)

job5 = df1[job3]["BasePay"] + df1[job3]["Benefits"]
print(job5)



















#Display name of the person having the highest basepay
column6 = df1.columns           #not method, an attribute
print(column6)                  #Checking the column name first to understand in which column we have to perform the operation


df1["BasePay"] = df1["BasePay"].replace("Not Provided", np.nan)     #To perform -- max() -- method we first have to remove all the string, that's why we replaced "Not Provided" with NaN value
df1["BasePay"] = pd.to_numeric(df1["BasePay"])                      # Now converting all the values of full column to numeric (by default float64)

salary1 = df1["BasePay"].max()  #Gettinng the max amount
print(salary1)

salary2 = df1[df1["BasePay"] == salary1]["EmployeeName"]        #Based on the condition and boolean value, then from the employeename column we got the name
print(salary2)





















#Find Average BasePay of all employee per year
salary3 = df1["BasePay"].mean()     #Basepay mean of all year
print(salary3)




salary4 = df1.groupby('Year')     #First we grouped the value based on the unique value of column "year" 
print(salary4, type(salary4))                                      #It will return the average basepay of all the employee PER YEAR
print([(type(i), i) for i in salary4])          #As salary4 is a pandas_groupby_object, in that object each element is a tuple which repesents all the values associated with a particular group
                                                #We used list comprehension here to iterate over the groupby object, and make a list of tuples, where each tuple contains -- type(particular_group), particular_group -- i is the particular group here


salary5 = df1.groupby('Year')["BasePay"].mean()     #First we grouped the value based on the unique value of column "year" and secondly we selected only the basepay column of each group through indexing column_name,, lastly we applied the -- mean() -- method on the basepay column of each of the group(based on year value)
print(salary5, type(salary5), salary5.shape, salary5.iloc[2])       # -- By --iloc-- method we can access row by its index










#Find Average BasePay of All Employee per JobTitle
column7 = df1.columns           #not method, an attribute
print(column7)                  #Checking the column name first to understand in which column we have to perform the operation


job6 = df1.groupby("JobTitle")["BasePay"].mean()            # You can also apply -- .sort_values(ascending=False) -- if you want sort the values in descending order    #Same as the previous one
print(job6)














#Find Average Basepay of employee having jobtitle ACCOUNTANT
print(column7)

ave1 = df1[df1["JobTitle"] == "ACCOUNTANT"]["BasePay"].mean()       #Already explained above
print(ave1)










#Find Top 5 Most Common Jobs
job7 = df1["JobTitle"].value_counts()[0:5]              # Or you can use -- head() -- method here
print(job7)











