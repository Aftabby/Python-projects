import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Datasheet link : https://www.kaggle.com/datasets/lava18/google-play-store-apps
YT : Data Thinkers ,, Project 5, Case Study 5

Google Play Store DataSet
'''

df1 = pd.read_csv("googleplaystore.csv")
print(df1, type(df1))

df2 = df1[["App", "Size", "Installs", "Type", "Price", "Content Rating"]]   #To get a better idea
print(df2)








#Display Top 5 rows and last 3 rows
head1 = df1.head()
print(head1)

tail1 = df1.tail(3)
print(tail1)












#Find shape of the data
shape1 = df1.shape
print(shape1)

column1 = df1.columns
print(column1)











#Get info about the dataset like total number of rows, columns, datatypes of each column and memory requirement
info1 = df1.info()
print(info1)










#Get overall statistics about the dataframe
des1 = (df1.describe()).round(2)
print(des1)

des1 = (df1.describe(include="all")).round(2)
print(des1)












#Total number of app titles contain Astrology

df3 = df1["App"].str.contains("Astrology", case=False)

total1 = df3.sum()              #You can also use the -- len() -- function
print(total1)           








#Find Average App rating
ave1 = df1["Rating"].mean()
print(round(ave1, 2))











#Find total number of unique category
print(column1)

unique = df1["Category"].nunique()
print(unique)









#Which Category getting the highest average rating

val1 = df1["Rating"].value_counts()
print(val1)
                        #In here it seems like we have one rating value of 19, which is not possible, because the highest value of rating is 5
                        # So, we are gonna remove it and finding its index by a condition and by using -- drop -- method
index1 = df1.index[df1["Rating"] > 5.0]
print("==\n", index1, type(index1))

df1.drop(index1, inplace=True)      #Dropping the rows with rating more than 5

val2 = df1["Rating"].unique()       #Checking again
print(val2)

df4 = df1.groupby("Category")["Rating"].mean().sort_values(ascending=False)  #Returned series object (though groupby method returns groupby object, but as we applied more methods we got return value of series_object)
print(df4)                                                                  #Here, first we grouped the data according to each unique value of the "Category" column, then chose the ["Rating"] column of each of the group and performed arithmatic mean on it, and the sorted the group as per the value(mean) in descending order
                                                                            #We got a returned series object in -- df4 -- whose row index_label is the category name(we grouped earlier) and the value of the rows is the mean of rating value of that group

category1 = df4.index[0]        #As we sorted the value in descending order we know the index_label of the first row is the category with highest average rating, that's how we got the index_label of the row -- label = df.index[row_number] --
print(category1)













#Find total number of apps having 5 star rating

total2 = (df1["Rating"] == 5).sum()     # -- df1["Rating"]==5 -- returns a series object with boolean values, and the -- sum() -- adds up every element considering True as 1, and False as 0
print(total2)







#Find average Value of Reviews

df5 = df1["Reviews"].astype("int")  #Converting the column data type to int
print(df5.dtype)

ave2 = df5.mean()
print(round(ave2, 2))

















#Find total number of Free and Paid Apps
print(column1)

val3 = df1["Type"].value_counts()
print(val3, type(val3))















#Which App has maximum reviews

max1 = df1[df1["Reviews"] == df1["Reviews"].max()]["App"]
print(max1)






print("==============================")










#Display Top 5 Apps having Highest Reviews

dup1 = df1.duplicated()     # Series object of boolean values depending upon the if the row is unique or repeated previously
print(dup1, type(dup1))

dup2 = dup1.sum()        #Total number of duplicate rows
print(dup2)

df1 = df1.drop_duplicates() #By default it will include all the columns to check duplication
print((df1.duplicated()).sum())         #Checking if there is still any duplicate rows exists or not

print("=================================")
df6 = (df1.sort_values("Reviews", ascending=False)).head()
print(df6, type(df6))














#Find Average rating of Free and Paid Apps
print(column1)
print(df1["Rating"].dtype)

ave3 = df1.groupby("Type")["Rating"].mean().round(2)
print(ave3)









#Display top5 apps having Maximum Installs
df7 = df1.sort_values("Installs", ascending=False).head()
print(df7, df7["Installs"])

