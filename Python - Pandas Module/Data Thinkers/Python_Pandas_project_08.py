import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Datasheet link : https://www.kaggle.com/datasets/rahuldogra/top5000youtubechannels
YT : Data Thinkers ,, Project 8, Case Study 8

Youtube Channel Dataset
'''

df1 = pd.read_csv("top-5000-youtube-channels.csv")


#Display All rows except the last 5 rows using head method
head1 = df1.head(-5)        # You can guess what happens after passing a negative integer to head method
print(head1)






#Display ALl rows except the first 5 rows using tail method
tail1 = df1.tail(-5)
print(tail1)








#Find Shape of Our Dataset
shape1 = df1.shape
print(shape1)








#Get Information about our dataset like total number rows, total number of columns, datatypes of each column and memory requirement
print("=========== INFO Started ===========")
df1.info()      #calling dataframe.info() in pandas will automatically print out information about the DataFrame. This includes the number of entries, the number of non-null entries for each column, and the data type of each column. It's a useful method for getting a quick overview of your data.

print("============== INFO END =============")








#Get Overall Statistics about the dataframe
pd.options.display.float_format = '{:.2f}'.format       #For large number by default in panda it shows in exponential format (10e34), so now we changed it to float format and 2 decimal after the decimal point
                                                        #options.display.float_format is an option in pandas that allows you to specify a custom formatter for floating point numbers.'{:.2f}'.format is a string formatting method in Python. Here, :.2f is a format specification for a float number. : is the start of the format specification, .2 specifies the precision of the number (2 digits after the decimal point), and f stands for fixed-point notation.So, pd.options.display.float_format = '{:.2f}'.format sets the display of floating point numbers in a pandas DataFrame to be rounded to two decimal places.


des1 = df1.describe(include="all")
print(des1)










#Data Cleaning (Replace '--' to NaN)
df1.replace(to_replace='--', value=np.nan, regex=True, inplace=True)





#Check Null Values in the Dataset
null1 = df1.isnull().sum()
print(null1)

#sns.heatmap(df1.isnull())
#plt.show()


df1.dropna(axis=0, inplace=True)        #To drop the row which contains missing value axis=0          






#Data Cleaning [Rank COlumn]
print(df1['Rank'].sample(frac=0.2))


print(df1.dtypes)       #Checking the column data types of the dataframe object



df1['Rank'] = df1["Rank"].apply(lambda x : ''.join(x[:-2].split(",")))  #takes a string x as input, splits it into a list of substrings at each comma, removes the last two elements from the list, and then joins the remaining substrings back together into a single string.
df1["Rank"] = df1["Rank"].astype(int)
print(df1["Rank"])





#Data Cleaning [Video Uploads & Subscribers]
df1["Video Uploads"] = df1["Video Uploads"].astype(int)
df1["Subscribers"] = df1["Subscribers"].astype(int)












#Data Cleaning [Grade Column]
print(df1["Grade"])

print(df1.Grade.unique())
print(df1.Grade.value_counts())

df1["Grade"] = df1["Grade"].map({"A++ ":5, "A+ ":4, "A ":3, "A- ":2, "B+ ":1})

#sns.countplot(x="Grade", data=df1)
#plt.yscale('log')       #Using logarithmic scaling in y-axis
#plt.show()

print(df1.shape)
df1 = df1[df1.Grade != '\xa0 ']     #Seems like there are some values in the Grade Column with '\xa0 ' values
print(df1.shape)

#sns.countplot(x="Grade", data=df1)
#plt.yscale('log')       #Using logarithmic scaling in y-axis
#plt.show()











#Find Average Views for each Channel
print(df1.head())



df1["Average_Views"] = round(df1['Video views']/df1["Video Uploads"], 2)
print(df1.head())

#sns.barplot(x="Channel name", y=["Average_Views"], data=df1.head(), )
#plt.yscale("log")
#plt.show()












#Find out top five channels with maximum number of video uploads
df2 = df1.sort_values(by="Video Uploads", ascending=False)
print(df2.head())

#sns.barplot(x="Channel name", y="Video Uploads", data=df2.head())
#plt.show()











#Find Correlation Matrix

df3 = df1.select_dtypes(include=[np.number])        #Only selecting the numerical column out of the whole dataframe object, to perform correlation matrix on it
                                                    #The select_dtypes() function is a pandas DataFrame method that returns a subset of the DataFrame's columns based on the data types you specify.In the code df.select_dtypes(include=[np.number]), you're asking pandas to return a DataFrame that only includes columns with numeric data types from the original DataFrame df. The np.number is a general identifier for any numeric data types (integer, float, complex, etc.).


print(df3.corr())           #Using the -- corr() -- method we can see the correlation among all the columns of the dataframe


#sns.scatterplot(x="Video views", y="Subscribers", data=df1.sample(frac=0.01))
#plt.show()

#sns.scatterplot(x="Video Uploads", y="Video views", data=df1.sample(frac=0.01))
#plt.show()















#Which Grade has a maximum number of video uploads
df3 = df1.groupby('Grade')['Video Uploads'].sum().sort_values(ascending=False)
print(df3)

sns.barplot(data=df3)
plt.show()






#Which Grade has the highest average views
df4 = df1.groupby('Grade')['Average_Views'].max().sort_values(ascending=False)
print(df4)

sns.barplot(data=df4)
plt.show()





#Which Grade has the highest number of subscribers
df5 = (df1.groupby('Grade')['Subscribers'].sum()).sort_values(ascending=False)
print(df5)


sns.barplot(data=df5)
plt.show()




#Which Grade has the highest video views?
df6 = df1.groupby('Grade')['Video views'].sum().sort_values(ascending=False)
print(df6)

sns.barplot(data=df6)
plt.show()

