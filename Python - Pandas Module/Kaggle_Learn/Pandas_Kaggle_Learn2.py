import numpy as np
import pandas as pd

filepath = "./winemag-data-130k-v2.csv"
df1 = pd.read_csv(filepath, index_col=0)
pd.set_option("display.max_rows", 5)
print(df1.head())

#Summary of the dataset/specific column - For numerical column (count, mean, std, min, max etc,)
des1 = df1.points.describe()
print(des1)

des2 = df1.taster_name.describe()
print(des2)


#Statistical functions
stats1 = df1.points.mean()
print(stats1)

#Unique values of a series
uni1 = df1.taster_name.unique()
print(uni1)


#Unique values with the count of occurance
uni2 = df1.taster_name.value_counts()
print(uni2)

#Using groupby function to count occurances of unique values
uni3 = df1.groupby('points').points.count()
print(uni3)



#== Maps ==

#Applying a function to each element of the pandas series
map1 = df1.points.map(lambda p: p*10)
print(map1)

#Applying a function to each element of the pandas dataframe/series
map2 = df1.points.apply(lambda p: p*10)     #While using .apply() on dataframe, pass (axis='columns') parameter to indicate row wise operation. To transform each column use (axis = 'index')
print(map2)

#Aggregation directly on each rows of a series
to_scale = 100
map3 = df1.points * to_scale                #You can also add, subtract, divide, etc.
print(map3)

#Concatenating directly on each rows of a series
map4 = df1.country + "-" + df1.region_1
print(map4)

"""
These operators are faster than map() or apply() because they use speed ups built into pandas. 
All of the standard Python operators (>, <, ==, and so on) work in this manner.
However, they are not as flexible as map() or apply(), which can do more advanced things, 
like applying conditional logic, which cannot be done with addition and subtraction alone.
"""


#Finding the index lavel of the maximum value within the series
index1 = (df1.points/df1.price).idxmax()                        #Row id of the maximum points-to-price ratio
print(index1)



# == Groupby ==

#Using groupby function to count occurances of unique values
grp1 = df1.groupby('points').points.count()                 #Alternatively, you can use " .size() " method.
print(grp1)

#Using groupby to group rows based on matching row values of a column and find the minimum of another column
grp2 = df1.groupby('points').price.min()
print(grp2)

#Using groupby and apply method to find the name of the first wine reviewed from each winery in the dataset
grp3 = df1.groupby('winery').apply(lambda df: df.title.iloc[0])
print(grp3)

#Group by more than one column
grp4 = df1.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
print(grp4)

#Using agg() with groupby() to run a bunch of different function on the group
grp5 = df1.groupby('country').price.agg([len, "min", "max"])            #Use strings for Pandas' built-in aggregation functions (min, max, mean, sum, etc.) to leverage their optimized implementations. Use the function object (variable) for any other functions (including Python built-ins) that you want to apply.
print(grp5)

#Groupby often retruns multi-index object
grp6 = df1.groupby(['country', 'province']).description.agg([len])
print(grp6)
print(type(grp6))

#Converting groupby multi-index object to regular index object
grp7 = grp6.reset_index()
print(grp7)
print(type(grp7))



# === Sorting ===

#Sorting values by column name in ascending order
sort1 = grp7.sort_values(by = 'len')                #"len" is the column name of "grp7" dataframe
print(sort1)

#Sorting values by column name in descending order
sort2 = grp7.sort_values(by='len', ascending=False)
print(sort2)

#Sorting based on index values
sort3 = grp7.sort_index()
print(sort3)

#Sorting by multiple column at a time
sort4 = grp7.sort_values(by=['country', 'len'])
print(sort4)

#
