import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Datasheet link : https://www.kaggle.com/datasets/gustavomodelli/forest-fires-in-brazil
YT : Data Thinkers ,, Project 10, Case Study 10

Forest Fires in Brazil Dataset
'''

df1 = pd.read_csv("amazon.csv", parse_dates=["date"])   #The parse_dates parameter in pandas.read_csv() is used to specify columns that should be parsed as dates.
print(df1)
print(df1.columns)
print(df1.dtypes)


#1. Display Top 5 Rows of The Dataset
print(df1.head())

#2. Check Last 5 Rows
print(df1.tail())

#3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
print(df1.shape)

#4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
df1.info()


#5. Check For Duplicate Data and Drop Them
print(df1.duplicated().sum())
df1 = df1.drop_duplicates()
print(df1.duplicated().sum())




#6. Check Null Values In The Dataset
print(df1.isnull().sum())

#sns.heatmap(data=df1.isnull())
#plt.show()



#7. Get Overall Statistics About The Dataframe
print(df1.describe())



#8. Rename Month Names To English
print(df1.columns)

print(df1.month.unique())
print(df1.month.value_counts())

month_name = {"Agosto": "August", "Setembro": "September", "Outubro": "October", "Novembro": "November", "Junho":"June", "Julho":"July", "Janeiro":"January", "Fevereiro": "February", "Mar�o":"March", "Abril":"April", "Maio":"May", "Dezembro":"December"}

df1["month"] = df1.month.map(month_name)
print(df1.month.unique())





#9. Total Number of Fires Registered
print(df1["number"].sum().round(2))







#10. In Which Month Maximum Number of Forest Fires Were Reported?
df2 = df1.groupby("month")["number"].mean().sort_values(ascending=False)
print(df2)


#plt.figure(figsize=(16, 5))
#sns.barplot(x="month", y="number", data=df1)    #Bar plot by default shows the mean value for each of the unique values
#plt.show()


    #Alternative
df2 = df1.groupby("month")["number"].sum().reset_index()
print(df2)














#11. In Which Year Maximum Number of Forest Fires Was Reported?
df3 = df1.groupby("year")["number"].sum().reset_index()
print(df3)


#plt.figure(figsize=(16, 5))
#sns.barplot(x="year", y="number", data=df3)    #Bar plot by default shows the mean value for each of the unique values
#plt.show()









#12. In Which State Maximum Number of Forest Fires Was Reported?
df4 = df1.groupby("state")["number"].sum().sort_values(ascending=False)

print(df4)

#sns.barplot(data = df4)        #It shows the total value for each of the state
#plt.xticks(rotation=60)
#plt.show()


#sns.barplot(x="state", y="number", data = df1)     #It shows average or mean value of each of the state
#plt.xticks(rotation=60)
#plt.show()










#13. Find Total Number of Fires Were Reported In Amazonas
total1 = df1[df1["state"] == "Amazonas"]["number"].sum().round(2)
print(total1)












#14. Display Number of Fires Were Reported In Amazonas (Year-Wise)
df6 = df1[df1["state"] == "Amazonas"]
df7 = df6.groupby("year")["number"].sum().reset_index()

print(df7)

plt.figure(figsize=(16, 5))
sns.barplot(x="year", y="number", data=df7)
plt.show()








#15. Display Number of Fires Were Reported In Amazonas (Day-Wise)

df8 = df1[df1["state"] == "Amazonas"]
df9 = df8.groupby(df8["date"].dt.dayofweek)["number"].sum()

print(df9)


import calendar

df9.index = [calendar.day_name[x] for x in range(0, 7)]
print(df9)

df10 = df9.reset_index()
print(df10)


plt.figure(figsize=(16, 5))
sns.barplot(x="index", y="number", data=df10)
plt.show()












#16. Find Total Number of Fires  Were Reported In 2015 And Visualize Data Based on Each ‘Month’

df11 = df1[df1["year"] == 2015].groupby("month")["number"].sum().reset_index()
print(df11)


plt.figure(figsize=(16, 5))
sns.barplot(x="month", y="number", data=df11)
plt.show()











#17. Find Average Number of Fires Were Reported From Highest to Lowest (State-Wise)
df5 = df1.groupby("state")["number"].mean().sort_values(ascending=False)
print(df5)


sns.barplot(x="state", y="number", data=df1)
plt.show()













#18.  To Find The State Names Where Fires Were Reported In 'dec' Month
df12 = df1[df1["month"] == "December"]["state"].unique()
print(df12)




