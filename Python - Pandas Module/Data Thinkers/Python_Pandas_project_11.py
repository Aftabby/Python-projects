#1. Import The Libraries And Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Datasheet link : https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset
YT : Data Thinkers ,, Project 11, Case Study 11

Heart Disease dataset
'''
#1. Import The Libraries And Dataset
df1 = pd.read_csv("heart.csv")   
print(df1)
print(df1.columns)
print(df1.dtypes)







#2. Display Top 5 Rows of The Dataset
print(df1.head())






#3. Check The Last 5 Rows of The Dataset
print(df1.tail())








#4. Find Shape of Our Dataset (Number of Rows And Number of Columns)
print(df1.shape)






#5. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
print(df1.info())












#6. Check Null Values In The Dataset
print(df1.isnull().sum())










#7. Check For Duplicate Data and Drop Them
print("Is there any duplicated value in the dataset?", df1.duplicated().any())






#8. Get Overall Statistics About The Dataset
print(df1.describe())









#9. Draw Correlation Matrix 
print(df1.corr())

#plt.figure(facecolor="#8E7AB5", edgecolor="#EEA5A6",figsize=(8, 5))
#sns.heatmap(data=df1.corr(), annot=True)
#plt.show()













#10. How Many People Have Heart Disease, And How Many Don't Have Heart Disease In This Dataset?
print(df1["target"].value_counts())











#11. Find Count of  Male & Female in this Dataset
print("Male:", (df1["sex"] == 1).sum())
print("Female:", (df1["sex"] == 0).sum())
print(df1["sex"].value_counts())        #Alternative

#plt.figure(facecolor="#8E7AB5", edgecolor="#EEA5A6",figsize=(10, 5) )
#sns.countplot(x="sex", data=df1)
#plt.xticks([0, 1], ["Female", "Male"])
#plt.show()














#12. Find Gender Distribution According to The Target Variable

#plt.figure(facecolor="#8E7AB5", edgecolor="#EEA5A6",figsize=(8, 5) )
#sns.countplot(x="sex", data=df1, hue="target")
#plt.xticks([0, 1], ["Female", "Male"])
#plt.legend(labels=["No-Disease", "Disease"])
#plt.show()














#13. Check Age Distribution In The Dataset

#plt.figure(facecolor="#8E7AB5", edgecolor="#EEA5A6",figsize=(8, 5))
#sns.countplot(x="age", data=df1)
#plt.show()


#plt.figure(facecolor="#8E7AB5", edgecolor="#EEA5A6",figsize=(8, 5))
#sns.distplot(x="age", data=df1, bins=20)
#plt.show()
















#14. Check Chest Pain Type
#plt.figure(facecolor="#8E7AB5", edgecolor="#EEA5A6",figsize=(8, 5))
#sns.countplot(df1.cp)
#plt.show()







#15. Show The Chest Pain Distribution As Per Target Variable

#plt.figure(facecolor="#8E7AB5", edgecolor="#EEA5A6",figsize=(8, 5))
#sns.distplot(x="cp", data=df1, hue="target")
#plt.legen(labels=["No-Disease", "Disease"])
#plt.show()












#16. Show Fasting Blood Sugar Distribution According To Target Variable

#plt.figure(facecolor="#8E7AB5", edgecolor="#EEA5A6",figsize=(8, 5))
#sns.distplot(x="fbs", data=df1, hue="target")
#plt.legen(labels=["No-Disease", "Disease"])
#plt.show()












#17.  Check Resting Blood Pressure Distribution

#df1.trestbps.hist()
#plt.show()








#18. Compare Resting Blood Pressure As Per Sex Column

#plt.figure(facecolor="#8E7AB5", edgecolor="#EEA5A6",figsize=(8, 5))
#sns.barplot(y="restecg", x="sex",data=df1)
#plt.show()



grid1 = sns.FacetGrid(df1, hue="sex", aspect=4)
grid1.map(sns.kdeplot, 'trestbps', fill=True)
plt.legend(labels=["Male", "Female"])
plt.show()














#19. Show Distribution of Serum cholesterol
df1.chol.hist()
plt.show()














#20. Plot Continuous Variables
categorical_value = list()
continous_value = list()

for column in df1.columns:
    if df1[column].nunique() <= 10:
        categorical_value.append(column)
    else:
        continous_value.append(column)


df1.hist(continous_value, figsize=(15, 6))
plt.tight_layout()
plt.show()

