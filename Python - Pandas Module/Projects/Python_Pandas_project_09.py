import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Datasheet link : https://www.kaggle.com/code/priyang/data-analysis-imdb-movie-dataset
YT : Data Thinkers ,, Project 9, Case Study 9

IMDB Dataset
'''

df1 = pd.read_csv("IMDB-Movie-Data.csv")
print(df1)
print(df1.columns)



#Display top and last 10 rows of the dataset
head1 = df1.head(10)
print(head1)

tail1 = df1.tail(10)
print(tail1)





#Find The Shape of the dataset
shape1= df1.shape
print(shape1)










#Get info about the dataset like number of rows, columns, datatypes of each column and memory requirement
df1.info()












#Check Null values in the dataset
null1 = df1.isnull().sum()
print(null1)

#sns.heatmap(data=df1.isnull())
#plt.show()

















#Drop all the missing values
df1.dropna(axis=0, inplace=True)

#sns.heatmap(data=df1.isnull())
#plt.show()








#Check FOr Duplicate Data
df2 = df1.duplicated().sum()    #No Duplicates
print(df2)












#Get overall statistics about the dataframe
stats1 = df1.describe(include="all")
print(stats1)






#Display title of the movie having runtime >=180 mins
df3 = df1[df1["Runtime (Minutes)"] >= 180]["Title"]
print(df3.head())











#In Which year there was the highest average voting
df4 = df1.groupby("Year")["Votes"].mean().sort_values(ascending=False)
print(df4)






#In Which year there was the highest revenue
df5 = df1.groupby("Year")["Revenue (Millions)"].sum().sort_values(ascending=False)
print(df5)






#Find the average rating for each director
df6 = df1.groupby("Director")["Rating"].mean().sort_values(ascending=False)
print(df6)













#Display top 10 lengthy movies title

    #Below both lines work the same
df7 = df1.sort_values(by="Runtime (Minutes)", ascending=False).head(10)["Title"]
#df7 = df1.nlargest(10, "Runtime (Minutes)")["Title"].head(10)
print(df7)










#Display Number of movies per year

    #Below two lines work the same
df8 = df1.groupby("Year").count().sort_values(by="Title", ascending=False)
#df8 = df1["Year"].value_counts()
print(df8)













#Find Most Popular Movie Title (Highest Revenue)
df9 = df1[df1["Revenue (Millions)"] == df1["Revenue (Millions)"].max()]["Title"]
print(df9)












#Display Top 10 highest rated movie titles and its directors
df10 = df1.sort_values(by="Rating", ascending=False).head(10)[["Title", "Director"]]
print(df10)











#Display top 10 highest revenue movie titles
df11 = df1.sort_values(by="Revenue (Millions)", ascending=False).head(10)["Title"]
print(df11)














#Find average rating of movies year-wise
df12 = df1.groupby("Year")["Rating"].mean().sort_values(ascending=False)
print(df12)








#Does Rating affect the revenue?
#sns.scatterplot(x="Rating", y="Revenue (Millions)", data=df1)       #Answer is no, as we don't see any trend here, the maximum data is clustered together rather than showing any trend
#plt.show()

















#Classify Movies based on ratings [Good, Better and Best]
#sns.histplot(x=df1.Rating, kde=True)
#plt.show()

#sns.heatmap(df1.isnull())       #No null value
#plt.show()

df1["Movie_class"] = df1.Rating.apply(lambda x : "Good" if x < 4.5 else ("Better" if x < 7 else "Best"))   #In a lambda function, you can't directly use 'elif' like in a normal function. However, you can achieve the same effect by nesting if-else statements.

#sns.countplot(x=df1.Movie_class)
#plt.show()





















#Count Number of Action Movies
count1 = df1["Genre"].str.contains("Action", case=False).sum()
print(count1)


















#Find Unique values from Genre
unique1 = df1.Genre.unique()        #It returns a numpy array with all the genres, 
print(unique1.dtype)
unique2 = list(unique1)
unique3 = {x for element in unique2 for x in element.split(',') }       #Using set comprehension to store unique values

           
print(unique1, unique1.shape, type(unique1), type(df1), type(df1.Genre))
print(unique2, type(unique2), len(unique2))
print("\n\n =====\n", unique3, len(unique3), type(unique3))
















#How many Film of Each Genre were made?
count2 = 0
gen_count = dict()

for genre in unique3:
    for movie in df1["Genre"]:
        if genre in movie:
            count2 +=1
    gen_count[genre] = count2
    count2 = 0

print(gen_count)

    
    #Alternative
from collections import Counter
all_gen = [x for all_genre in df1["Genre"] for x in all_genre.split(",")]   #This is a list comprehension that is iterating over each element in the "Genre" column of the dataframe df1. For each element (which seems to be a string of genres separated by commas), it splits the string into individual genres using split(","), and adds each genre to the all_gen list. So, all_gen ends up being a list of all genres present in the dataframe.
print(all_gen)


unique4 = Counter(all_gen)  #This line is using the Counter class from the collections module. Counter takes an iterable (in this case, the all_gen list) and returns a dictionary-like object where the keys are the unique elements in the iterable and the values are the counts of each element. So, unique4 will be a count of each genre in all_gen.
print(unique4)

