import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Datasheet link : https://www.kaggle.com/c/titanic
YT : Data Thinkers ,, Project 4, Case Study 4

Titanic DataSet
'''

df1 = pd.read_csv("train.csv")
print(df1, type(df1))



#Display Top 5 rows and last 3 rows of the Dataset
head1 = df1.head()
print(head1)

tail1 = df1.tail()
print(tail1)




#Find shape of the dataset
shape1 = df1.shape
print(f"The rows: {shape1[0]}, The column:{shape1[1]}")









#Get information about the dataset like total number rows, total number of column, datatypes of each column and memory requirement
info1 = df1.info()
print(info1)












#Get overall statistics about the dataframe
stats1 = df1.describe()         # pass -- include="all" -- to see the stats of numerical and categorical column, by default it shows numerical column
print(stats1)














#Data Filtering
columns1 = df1.columns
print(columns1)         #To see all the columns name

df2 = df1[["Name", "Age"]]      #Remember while passing more than one column pass the columns_names in a list, it returns a dataframe_object
print(df2)


male1 = sum(df1["Sex"] == "male")       #TO see how many males were there
print(male1)


male2 = df1[df1["Sex"] == "male"]   #Getting all the rows with "Male"
print(male2)

survive1 = sum(df1["Survived"] == 1)    #Checking how many people survived 
print(survive1)















#Check Null values in the dataset
print(columns1) 

null1 = df1.isnull()
print(null1)

    #Showing the graph
#sns.heatmap(null1)
#plt.show()

null2 = null1.sum()
print(null2)


percentage_missing = (null2*100/len(df1)).round(2)        #Checking the missing values percentage of each of the column, round method rounds the floating value of the series_object up to two decimal values
print(percentage_missing)














#Drop the column with max missing value
print(columns1) 

df1.drop(["Cabin"], axis=1, inplace=True)

columns2 = df1.columns
print(columns2)













#Handle Missing Values
print(columns2)

df3 = df1["Embarked"]
print(df3)

mode1 = df3.mode()      # To check the statistical mode (most frequent value), because we will replace the NaN values of this column with the mode value
print(mode1)

df1["Embarked"].fillna("S", inplace=True)   #The NaN values will be replaced with "S" , which was the mode value of this column

df4 = df1["Embarked"]
null3 = df4.isnull().sum()
print(df4, "\n", null3)


df1["Age"].fillna(df1["Age"].mean(), inplace=True)  #Replacing the missing values of the - Age - column, with its statistical mean value

null4 = df1.isnull().sum()
print(null4)















# Categorical Data Encoding 
            #We do categorical data encoding for providing the datas to machine learning algorithm in future, which doesn't operate on categorical value(object)
                #Before encoding we gotta know how many categorical values are there in the column

unique1 = df1["Sex"].unique()
print(unique1)


df1["Gender"] = df1["Sex"].map({"male" : 1, "female" : 0})     # -- map -- method takes a dictionary, with existing value as key and new value as dictionary value, and replace value for each of the row
print(df1)

df1.insert(5, "Gender_New", df1["Gender"])      # -- dataframe.insert(index_of_column, Name_of_new_column, The_value) -- we inserted a new column with a new name to the dataframe_object in a specific column index
print(df1.head(5))




    #Alternative Encoding
unique2 = df1["Embarked"].nunique()
unique3 = df1["Embarked"].unique()
print(unique3, unique2)

df4 = pd.get_dummies(df1, columns=["Embarked"])     #In here the original Embarked column will be deleted and for each unique values new column will be created(with boolean Values), it takes dataframe_object as first positional parameter,  and in -- column -- parameter list of column names
print(df4)

df5 = pd.get_dummies(df1, columns=["Embarked"], drop_first=True)    #As we can guess the value of first column by the rest two column's value we can delete the first column by passing the parameter -- drop_first = True -- which is by default False
print(df5)














# Univariate Analysis
#How many people survived and how many died
print(columns2)
print(df1.head(10))

survive2 = (df1["Survived"] == 1).sum()
print(survive2)

survive3 = (df1["Survived"] == 0).sum()         #Number of dead people
print(survive3)

survive4 = df1["Survived"].value_counts()
print(survive4)

    #Showing graph
#sns.countplot(x="Survived", data = df1)
#plt.show()












#How many passengers were in first class, second class, and third class
columns3 = df1.columns
print(columns3)

unique4 = df1["Pclass"].value_counts()
print(unique4)

    #Showing graph
#sns.countplot(x = "Pclass", data=df1)
#plt.show()











#Number of Male and Female Passengers
gender1 = df1["Sex"].value_counts()
print(gender1)

    #Showing graph
#sns.countplot(x="Sex", data=df1, palette="Accent")  # WARNING : Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
#plt.show()

#sns.histplot(x="Age", data=df1, palette="Accent")   # WARNING : Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
#plt.show()

















#Bivariate Analysis
#Who has better chance of survival Male or Female?

chance1 = df1[df1["Sex"] == "male"]
chance2 = (chance1["Survived"] == 1).sum()*100/len(chance1)     # males_survive/total_male -- and *100 for percentage
print(round(chance2, 2), "%")

chance3 = df1[df1["Sex"] == "female"]
chance4 = (chance3["Survived"] == 1).sum()*100/len(chance3)     # females_survive/total_female -- and *100 for percentage
print(round(chance4, 2), "%")

    #Showing graph
#sns.countplot(x="Sex", data=df1, hue="Survived", palette="Accent")
#plt.show()





















#Feature Engineering
                #Is a process of using domain knowledge to extract features from raw data via data mining techniques, for future machine learning process

df1["Family_Size"] = df1["SibSp"] + df1["Parch"]        #  SibSp means number of Sibling and Parents, and Parch means number of Parents and Children
print(df1.head(10))


df1["Fare_per_person"] = df1["Fare"]/(df1["Family_Size"]+1)        # +1 is for the person himself
print(df1["Fare_per_person"])


