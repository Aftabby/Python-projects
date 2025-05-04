import numpy as np
import pandas as pd

filepath = "./winemag-data-130k-v2.csv"
df1 = pd.read_csv(filepath, index_col=0)
pd.set_option("display.max_rows", 5)

# == RENAMING ==

#Renaming a column
df2 = df1.rename(columns={'points': 'score'})       #rename() lets you rename index or column values by specifying a index or column keyword parameter, respectively.
print(df2.score)

#Renaming a row index
df3 = df1.rename(index={0: 'firstEntry', 1: 'secondEntry'})
print(df3.head())

#Naming both column name/index, and row index 
df4 = df1.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')
print(df4)



#== Combining == ( concat(), join(), merge() )

# Combining with concat() - used to concatenate (glue together) DataFrames along a specified axis (rows or columns).
df5 = pd.concat([df1.title, df1.price], axis=1)     #with axis=1, performing column cobining
print(df5)

#Combining with join() - used to combine DataFrames based on their indices or a specified column. It is primarily used for relational database-style joins.
df6 = df1[['title', 'taster_name']].join(df1['price'])      #Use attribute "lsuffix" and "rsuffix" if column names overlaps
print(df6)

