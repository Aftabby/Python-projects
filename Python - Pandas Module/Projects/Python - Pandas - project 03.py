import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Datasheet link : https://www.kaggle.com/datasets/wenruliu/adult-income-dataset/data
YT : Data Thinkers ,, Project 3, Case Study 3
'''

df1 = pd.read_csv("adult.csv")
print(df1, type(df1))









#Display top 10 and last 10 rows of the dataset
head1 = df1.head(10)
print(head1)

tail1 = df1.tail(10)
print(tail1)









#Find shape of the dataset
shape1 = df1.shape      #An attribute, not method
print(shape1)       # returns tuple (rows, columns)
print(f"Number of rows {shape1[0]}, Number of columns {shape1[1]}")












#Get info about the dataset (total rows, total columns, datatypes of each column and memory requirement)
df1.info()          # Calling dataframe.info() in pandas will automatically print out information about the DataFrame. This includes the number of entries, the number of non-null entries for each column, and the data type of each column. It's a useful method for getting a quick overview of your data.

print("==================================== Checking ====================== ")














#Fetch random samples from the dataset (20%)
sample1 = df1.sample(frac=0.2)              #With -- sample() -- method we can get random sample from the dataset, with named parameter -- frac -- we pass the percentage of the whole dataset we want in relative number format (i.e 0.5 means 50%)
print(sample1)                              #As every time we run the code we will get a different random number but if you want to keep the random number fixed without storing it in a variable, you can use the parameter -- random_state -- , it takes any integer value











#Check Null values in the data set
null1 = df1.isnull().sum()          #It will sum all the values in each of the column, to check row-wise pass --- axis=1 -- in -- sum() -- method
print(null1)


null2 = df1.isnull()
#sns.heatmap(null2)
#plt.show()

















#Perform data cleaning [Replace '?' with NaN]
print("==================================")


clean1 =  df1.isin(["?"]).sum()              # -- isin -- method takes a list, where the element of the list is checked with every value of dataset, if it matches then returns True in that position, else False
print(clean1)


columns = df1.columns   #To check all the the column names of the dataset
print(columns)

df1["workclass"].replace('?', np.nan, inplace=True)       #Replacing all the "?" values with NaN value, (Additional tips: we often use it, because -- dropna -- method works only on NaN value)
df1["occupation"].replace('?', np.nan, inplace=True)            #-- inplace=True -- because we want to change the original dataset
df1["native-country"].replace('?', np.nan, inplace=True)        #Alternatively you can use -- df1.replace() -- directly without mentioning any column_name

clean2 = df1.isin(["?"]).sum()      #Chacking again if the '?' still exists or not
print(clean2)


null3 = df1.isnull().sum()      # Checking the null values again
print(null3)

null4 = df1.isnull()
#sns.heatmap(null4)
#plt.show()




















#Drop all the missing values
print("==================================")
prcnt1 = (df1.isnull().sum()*100/len(df1)).round(2)        #Finding the percentage of the null value column wise, i.e per column adding all the NaN values of each row and then dividing it by total row number(len(df1)), and multiplying by 100 to get the percentage
print(prcnt1)                                       # We used -- round() -- method on dataframe_object to round up the float values up to two decimal points, We checked it to see how much data are we gonna drop, just checking
print(type(23))

df1.dropna(how="any", inplace=True)           # with -- how="any" -- means it will drop rows with any number of missing values, with -- how="all" -- we can drop only the rows whose all the column value is missing

shape2 = df1.shape
print(f"This many rows has been dropped from the dataset: {shape1[0] - shape2[0]}")





















#Check for Duplicate Data and Drop them

dup1 = df1.duplicated()         #The - duplicated() - method returns a Series with True and False values that describe which rows in the DataFrame are duplicated and not. N.B: The first time row is always False, if the row repeats, the repeated/duplicate rows are replaced as True
print(f"\n ========================== dup1 {dup1} " )

dup2 = df1.duplicated().any()           # Python -- any() -- method returns one value for each column, True if ANY value in that column is True, otherwise False.,, The -- all() -- method returns one value for each column, True if ALL values in that column are True, otherwise False
print(f"dup2 {dup2} \n ==========================" )


df1.drop_duplicates(inplace=True)   #If any row is duplicated, it will drop that row, -- drop_duplicates() -- function to remove duplicated rows(keeping the first one only) from a DataFrame. By default, this function considers all columns to identify duplicates.

shape3 = df1.shape
print(shape2, shape3)       #Change of row number




















#Get overall Statistics about the dataframe
describe1 = df1.describe()      #By default shows only the numeric column, to include all columns pass the parameter -- incluede="all"
print(describe1)













#Drop the columns: education-num, capital-gain, capital-loss
columns = df1.columns   #To check all the the column names of the dataset
print(columns)

df1.drop(["educational-num", "capital-loss", "capital-gain"], axis=1, inplace=True)  # -- axis=1 -- as we are gonna delete the column


columns = df1.columns   #To check if the column is dropped or not
print(columns)














#Univariate Analysis - taking one variable at a time(column) and perform analysis on it
#What is the distribution of age column?
columns = df1.columns   #To check all the the column names of the dataset
print(columns)

describe2 = df1["age"].describe()
print(describe2)

    #Showing graph
#describe3 = df1["age"].hist()       #When Pandas function DataFrame.hist() is used, it automatically calls the function matplotlib.pyplot.hist() on each series in the Pandas DataFrame. As a result, we obtain one histogram per column.
#plt.show()              #To view this graph you might need to uncomment the previous -- plt.show() -- as well

















#Find total number of persons having age between 17 - 48 (Inclusive) using between method

total1 = sum((df1["age"]>=17) & (df1["age"]<=48))   #Without using between method
print(total1)


total2 = sum(df1["age"].between(17, 48))     #In -- between -- method both values are inclusive, between method returns boolean series
print(total2)






















#What is the Distribution of Workclass Column?
columns = df1.columns   #To check all the the column names of the dataset
print(columns)


describe4 = df1["workclass"].describe()
print(describe4)

    #Showing graph
#plt.figure(figsize=(10, 10))       #Sizing the graph figure so that they don't overlap values
#df1["workclass"].hist()         #When Pandas function DataFrame.hist() is used, it automatically calls the function matplotlib.pyplot.hist() on each series in the Pandas DataFrame. As a result, we obtain one histogram per column.
#plt.show()





















#How many Persons having bachelor or Masters Degree?
columns = df1.columns   #To check all the the column names of the dataset
print(columns)

filter1 = df1["education"] == "Bachelors"
filter2 = df1["education"] == "Masters"

df2 = df1[filter1 | filter2]        # -- filter1 | filter2 -- will return a boolean value series_object based on the bitwise operator "or" ( | ) , 

total3 = len(df2)
print(total3)


        #Another method
df3 = df1["education"].isin(["Bachelors", "Masters"])       # In -- isin() -- method comma means 'or' not 'and'
total4 = sum(df3)
print(total4)




















#Bivariate Analysis --- Relationship between two different variables

#Find relationship between salary and age

    #Showing graph
#sns.boxplot(x="income", y="age", data=df1)
#plt.show()


















#Replace income values ['<=50k', '>=50k'] with 0 and 1

unique1 = df1["income"].unique()
print(unique1)

value1 = df1["income"].value_counts()
print(value1)

    #Showing graph
#sns.countplot(x="income", data=df1)
#plt.show()


def salary_data(income):
    if income == '<=50k':
        return 0
    else:
        return 1
    

df1["encoded_salary"] = df1["income"].apply(salary_data)
print(df1.head(10))


    #Another Method
df1["income"].replace(["<=50K", ">50K"], value=[0, 1], inplace=True)
print(df1.head(10))
print("=====================================================")






















#Which Workclass getting the highest income?
group1 = df1.groupby("workclass")["income"].mean()
print(group1)

group2 = group1.sort_values(ascending=False)
print(group2)




















#Who has better chance to get salary >50K , Male or Female?
group3 = df1.groupby("gender")["income"].mean().sort_values(ascending=False)
print(group3)




















#Convert workclass Columns Dataset to Category Datatype
info1 = df1.info()      #Checking the data types
print(info1)

df1["workclass"] = df1["workclass"].astype("category") # -- DataFrame.astype() -- method is used to cast a pandas object to a specified dtype

info1 = df1.info()      #Checking the data types
print(info1)
