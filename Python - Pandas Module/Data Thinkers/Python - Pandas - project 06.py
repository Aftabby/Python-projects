import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Datasheet link : https://www.kaggle.com/datasets/andrewmvd/udemy-courses
YT : Data Thinkers ,, Project 6, Case Study 6

Udemy Courses DataSet
'''

df1 = pd.read_csv("udemy_courses.csv")
#df1 = pd.read_csv("udemy_courses.csv", parse_dates=["published_timestamp"])        # ***  parameter -- parse_dates -- takes the column name of the column whose value we want to treated as date and timestamp, and the column data type will be converted into dattime data type
print(df1, df1.columns, type(df1))
print(df1[['is_paid', 'price', 'num_subscribers', 'num_reviews', 'num_lectures', 'level']])


#Display Top 10 Rows and the last 5 rows of the dataset
head1 = df1.head(10)
print(head1)

tail1 = df1.tail()
print(tail1)












#Find shape of the data
shape1 = df1.shape
print(shape1)









#Get info about the dataset like total number of rows, columns, datatypes of each column and memory requirement
info1 = df1.info()
print(info1)










#Get overall statistics about the dataframe
stats1 = df1.describe()
print(stats1)
















#Check Null Values in the dataset
null1 = df1.isnull().sum()
print(null1)




    #Alternative
null2 = df1.isnull().values.any()       #The --  .values -- attribute in pandas is used to return a Numpy representation of the DataFrame. That is, it will return a 2D Numpy array, with each item corresponding to a cell in the DataFrame. This can be useful when you want to perform some operation that requires a Numpy array rather than a pandas DataFrame.
print(null2)                               
















#Check for duplicate data and drop them
dup1 = df1.duplicated().sum()
print(dup1)


df1 = df1.drop_duplicates()

dup2 = df1.duplicated().sum()
print(dup2)










#Find out number of courses per subject
column1 = df1.columns
print(column1)

print(df1["subject"])

df2 = df1.groupby("subject")["course_title"].count()
print(df2)


    #Alternative
count1 = df1["subject"].value_counts()
print(count1)



    #SHowing Graph
sns.countplot(x = df1["subject"])
plt.xlabel("Subjects", fontsize=13)
plt.ylabel("Number of courses", fontsize=13)
plt.xticks(rotation=5)
plt.show()








#For which levels udemy courses providing the courses
unique1 = df1["level"].unique()
print(unique1)




    #SHowing Graph
sns.countplot(x = df1["level"])
plt.xlabel("Level", fontsize=13)
plt.ylabel("Number of courses per level", fontsize=13)
plt.xticks(rotation=5)
plt.show()









#Displays the count of Paid and Free Courses
print(column1)
print(df1["is_paid"])

value1 = df1["is_paid"].value_counts()

paid1 = value1.iloc[0]
free1 = value1.iloc[1]
print(f"Paid courses are {paid1}, Free courses are {free1}")




  #SHowing Graph
sns.countplot(x = df1["is_paid"])
plt.xlabel("Is Paid?", fontsize=13)
plt.ylabel("Number of courses", fontsize=13)
plt.xticks(rotation=5)
plt.show()










#Which Course has more lectures (Free or Paid)?

df3 = (df1.groupby("is_paid")["num_lectures"]).sum()
print(f"Paid courses has {df3.iloc[1]} lectures, and Free courses has {df3.iloc[0]} lectures") 












#Which Courses have a higher number of subscribers (Free or Paid)?
print(column1)

df4 = (df1.groupby("is_paid")['num_subscribers']).sum()
print(df4)



sns.barplot(x="is_paid", y="num_subscribers", data=df1)
plt.show()














#Which level has the highest number of subscribers?
df5 = (df1.groupby("level")['num_subscribers']).sum().sort_values()
print(df5)





sns.barplot(x="level", y="num_subscribers", data=df1, palette=["red", "green", "blue"])
plt.show()










#Find most popular course title
title1 = df1[df1['num_subscribers'].max() == df1['num_subscribers']]["course_title"]
print(title1)

















#Display 10 most Popular Courses as per number of subscribers

title2 = df1.sort_values('num_subscribers', ascending=False).head(10)
print(title2)


sns.barplot(x="num_subscribers", y="course_title", data=title2, palette=["red", "green", "blue"])
plt.show()














#Find the course which is having the highest number of reviews
rev1 = df1[df1["num_reviews"] == df1["num_reviews"].max()]
print(rev1)



plt.figure(figsize=(10, 4))
sns.barplot(x="subject", y="num_reviews", data=df1, palette=["red", "green", "blue"])
plt.show()










#Does price affect number of reviews?

    #Showing the graph
plt.figure(figsize=(15, 3))
sns.scatterplot(x = "price", y="num_reviews", data=df1)
plt.ylim(0, 20000)
plt.show()
















#Find total number of courses related to Python
total3 = (df1['course_title'].str.contains("python", case=False)).sum()
print(total3)




























#Display 10 most popular python courses as per number of subscribers
print(column1)

total4 = df1[df1["course_title"].str.contains("python", case=False)]
print(total4)

total5 = (total4.sort_values("num_subscribers", ascending=False)).head(10)
print(total5, total5["num_subscribers"])





sns.barplot(x="num_subscribers", y="course_title", data=total5, palette=["red", "green", "blue"])
plt.show()



#In which year the highest number of courses were posted?
print(column1)
print(df1["published_timestamp"], type(df1["published_timestamp"]))

df1["year"] = df1["published_timestamp"].apply(lambda x : x[:4])
print(df1["year"])

df6 = (df1.groupby("year")["year"].count()).sort_values(ascending=False)
print(df6)










#Display Count of posted Subjects (Year wise)
print(column1)


df7 = df1.groupby("year")["subject"].value_counts()
print(df7)



