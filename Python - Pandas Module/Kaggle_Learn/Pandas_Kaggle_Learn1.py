import numpy as np
import pandas as pd

#To create a dataframe with column name
df1 = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
df2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful'], 'Sue':['Pretty good.', 'Bland']})

print(df2)

#Create dataframe with row index name
df3 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful'], 'Sue':['Pretty good.', 'Bland']},
                    index = ['Product A', 'Product B'])
print(df3)


#Create a series
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([20, 30, 40], 
                index=['Sale1', 'Sale2', 'Sale3'],
                name = 'Product A')
print(s2)


#Read data as pandas object(Dataframe) from csv file
filepath = "My_CSV_4.csv"
df4 = pd.read_csv(filepath)
print(df4)


#Shape of a dataframe
shape1 = df4.shape              #An attribute, not a method
print(shape1)                   #In (column, row) format


#Access first n rows
head1 = df4.head(3)             #If no parameter passed, by default it's 5
print(head1)


#Using a column as index of rows
index1 = pd.read_csv(filepath, index_col=0)         #Each value of the first column will be used as the index of their corresponding row


#Saving dataframe as a CSV file
filename = "kaggle_learn.csv"
csv1 = df4.to_csv(filename)


#Setting pandas to display 5 rows (at max) when dataframe is printed
pd.set_option('display.max_rows', 5)
print(df4)


#Accessing a column of the dataframe
col1 = df4.header2
col2 = df4["header2"]           #Works the same
print(col1, col2)


#Accessing specific row(s) by indexing/slicing in an specific column
row1 = df4["header2"][3]
print(row1)


#Accessing specific row and column by index/name using loc and iloc (Both loc and iloc are row-first, column-second. This is the opposite of what we do in native Python, which is column-first, row-second)
row2 = df4.iloc[4]
print(row2)

col3 = df4.iloc[:, 2]
print(col3)

row3 = df4.iloc[:3, 2]
print(row3)

row4 = df4.iloc[[0, 1, 2], 2]               #All the rows that matches the index of the list's elements
print(row4)

col4 = df4.iloc[-2:]
print(col4)

    #Label based selection
val1 = df4.loc[0, 'header3']
print(val1)

val2 = df4.loc[:, ['header2', 'header4', 'header1']]
print(val2)
                                            #NOTE: iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.
                                                    #This is particularly confusing when the DataFrame index is a simple numerical list, e.g. 0,...,1000. In this case df.iloc[0:1000] will return 1000 entries, while df.loc[0:1000] return 1001 of them!

                        
#Conditional Selection
con1 = df4['header2'] > 50
print(con1)

con2 = df4.loc[df4['header2'] > 50]
print(con2)

con3 = df4.loc[(df4.header2 > 50) & (df4.header3 < 50)]
print(con3)

con4 = df4.loc[(df4.header2 > 50) | (df4.header4 < 50)]
print(con4)

values = [54, 55]
con5 = df4.loc[df4.header2.isin(values)]
print(con5)

con6 = df4.loc[df4.header2.isnull()]
print(con6)

con7 = df4.loc[df4.header2.notnull()]
print(con7)


#Assigning Data
df4['header2'] = 404
print(df4['header2'])