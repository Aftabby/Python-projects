import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



'''
Datasheet link : https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales
YT : Data Thinkers ,, Project 13, Case Study 13

Supermarket Sales
'''

df1 = pd.read_csv("supermarket_sales - Sheet1.csv", parse_dates=["Date"])
print(df1)
print(df1.dtypes)
print(df1.columns)







#Display Top and Last 5 rows of the dataset
print(df1.head())

print(df1.tail())








#Print random 5 rows from our dataset
print(df1.sample(n=5))











#Find Shape of the dataset
print(df1.shape)        #Returns a tuple














#Check null values in the dataset
print(df1.isnull().sum())













#Display information about the dataset
df1.info()








#Get overall statistics
print(df1.describe())








#Univariate Analysis
#Find Aggregate sales among branches (Categorical column)
print("===============================================================\n")
df2 = (df1.groupby("Branch")["cogs"]).sum()
print(df2)
print(df2.shape)


#sns.barplot(df2)
#plt.show()





#Find the most popular payment method used by customers (Categorical column)
print(df1.Payment.value_counts())











#Find the distribution of customer ratings. (Numerical column)

#sns.displot(x="Rating", data=df1, kde=True)
#plt.show()







#Find the distribution of cost of good sold (Numeric column)
#sns.displot(x="cogs", data=df1, kde=True)
#plt.show()














#Bivariate Analysis / Multivariate Analysis
#Does the cost of goods sold affect the ratings that the customer provide? (Numerical - numerical)

#sns.scatterplot(x="Rating", y="cogs", data=df1)
#plt.show()                                              #Answer is no














#Does Gross income affect the ratings that the customers provide? (Numerical - numerical)
#sns.scatterplot(x="Rating", y="gross income", data=df1)
#plt.show()                                                  #Answer is no













#Find the most profitable branch as per gross income. (Numerical - Categorical)
#sns.boxplot(x="Branch", y="gross income", data=df1)
#plt.show()















#Is there any relationship between gender and gross income?(Numerical - categorical)
#sns.boxplot(x="Gender", y="gross income", data=df1)
#plt.show()

#sns.barplot(x="Gender", y="gross income", data= df1)
#plt.show()













#Find the product line that generates the most income. (Numerical - Categorical)
#sns.barplot(x="Product line", y="gross income", data=df1)
#plt.show()


#sns.boxplot(x="Product line", y="gross income", data=df1)
#plt.show()















#Find the highest unit price in the product line. (Numerical - Categorical)
#sns.barplot(x="Product line", data=df1, y="Unit price")
#plt.show()


#sns.boxplot(x="Product line", data=df1, y="Unit price")
#plt.show()











#Find different payment methods used by customers citywise. (Categorical - categorical)

df3 = pd.crosstab(df1["City"], df1["Payment"])
print(df3)

#sns.heatmap(data=df3)
#plt.show()

#sns.countplot(x="City", hue="Payment", data=df1)
#plt.show()















#Which product line is purchased in the highest quantity

count1 = df1.groupby("Product line")["Quantity"].sum()
print(count1)



#sns.barplot(data=count1)
#plt.show()










#Display Daily sales by the day of the week 
dw_map = {
    0 : "mon",
    1 : "tue",
    2 : "wed",
    3 : "thu",
    4 : "fri",
    5 : "sat",
    6 : "sun"
}

df1["Day_of_week"] = df1["Date"].dt.dayofweek.map(dw_map)

print(df1["Day_of_week"])
print(df1["Day_of_week"].value_counts())



#sns.barplot(data=df1["Day_of_week"].value_counts())
#plt.show()












#What will be the highest months for sale
month_map ={
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
    7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}

df1["Month"] = df1["Date"].dt.month.map(month_map)

count2 = df1["Month"].value_counts()
print(count2)

sns.barplot(data=count2)
plt.show()
