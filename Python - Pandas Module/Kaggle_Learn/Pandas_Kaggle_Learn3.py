import numpy as np
import pandas as pd

filepath = "./winemag-data-130k-v2.csv"
df1 = pd.read_csv(filepath, index_col=0)
pd.set_option("display.max_rows", 5)


#Data types of all the columns in the dataset
dtype1 = df1.dtypes
print(dtype1)

#Data type of a column
dtype2 = df1["price"].dtype
print(dtype2)

#Changing a columns's dtype
dtype3 = df1.points.astype('float64')
print(dtype3)

#Data type of a series/dataframe's index
dtype4 = df1.index.dtype
print(dtype4)

#Checking the null values of the column (NaN value)
dtype5 = df1[pd.isnull(df1.country)]
print(dtype5)

dtype6 = df1[pd.notnull(df1.country)]
print(dtype6)

#Replacing missing values (NaN)
null1 = df1.region_2.fillna("Unknown")
print(null1)

#Replacing any value
replace1 = df1.taster_twitter_handle.replace("@kerinokeefe", "@kerino")
print(replace1)



