# == Exploratory Data Analysis - Intro to Pandas ==

# Import the Pandas library
import pandas as pd
# Import the Seaborn library for plotting
#!pip install seaborn
import seaborn as sns

# Load the dataset and save it to the df variable
df = pd.read_csv('data/world_happiness.csv')

# This line will display the first few rows of the dataframe if there are no lines of code after.
df.head()

# Try uncommenting different combinations of the lines below.
# print("Cats are cool.")
# print(df.head())
# print(df)
# print("Some more text about cats being cool.")
# display(df)

# This line will display only the last two rows of the dataframe.
df.tail(2)

#In the DataFrame, the data is stored in a two dimensional grid (rows and columns). The rows are indexed and the columns are named. To see the index or the column names, you can use DataFrame.index or DataFrame.columns respectively.
df.index
df.columns

#To rename the columns, you can use DataFrame.rename() and pass the columns you want to rename in a dictionary.
# A dictionary mapping old column names to new column names. In addition to replacing spaces
# with underscores, you will make all of the text lowercase.
columns_to_rename = {i: "_".join(i.split(" ")).lower() for i in df.columns}
# Note that this dictionary is created automatically from the column names.
# You can also create it by hand and rename only the columns you want to rename
# For example, see the commented line below:
# columns_to_rename = {"Country name": "country_name", "Life Ladder": "life_ladder"}

# Rename the columns
df = df.rename(columns=columns_to_rename)
# Display the new dataframe
df.head()

#DataFrame type is that the columns of the resulting DataFrame can have different dtypes
df.dtypes

# List all of the columns that should be floats
float_columns = [i for i in df.columns if i not in  ["country_name", "year"]]
# Change the type of all float columns to float
df = df.astype({i: float for i in float_columns})
# Show the types of all columns
df.dtypes

#The df.info() provides some additional information. In addition to data types it also tells you the number of non-null values per column.
df.info()

#One way of selecting a single column is to use DataFrame.column_name. 
# Here you can see why it was a good idea that you renamed the columns to not include any whitespaces. 
# This returns a Pandas Series, which is a different datatype from a DataFrame
# Select the life_ladder column and store it in x
x = df.life_ladder

print(f"type(x):\n {type(x)}\n")
print(f"x:\n{x}")

#Another way to do this is to use square brackets and the name of the column in quortes, much as you would do when accessing an entry in a dictionary. 
# As with dictionaries, you can use double quotes or simple quotes.
x = df["life_ladder"]

print(f"type(x):\n {type(x)}\n")
print(f"x:\n{x}")

#Passing a list of labels rather than a single label selects the columns and returns a DataFrame (rather than a Series), with only the selected columns. You can use it to select one or more columns.
x = df[["life_ladder"]]
# x = df[["life_ladder", "year"]]

print(f"type(x):\n {type(x)}\n")
print(f"x:\n{x}")

#Passing a slice : selects matching rows and returns a DataFrame with all columns in your original dataframe
df[2:5]

#If you want to iterate over the rows, you can use the .iterrows() method. 
#For each row it yields a (index, row) tuple, where the row is a Series object containing the data. Note that this does not preserve the data types (dtypes) across the rows (dtypes are preserved across columns for DataFrames)
index, row = next(df.iterrows())
row

df[df["year"] == 2022]
# df[df["life_ladder"] > 5] # Select rows where life_ladder > 5
# df[df["life_ladder"] > 11] # This one should return an empty dataframe

#Note that now that you selected only the certain rows, 
# the index column does not make much sense anymore because you have a lot of gaps. 
# While this is not a problem, in some cases you might want the index to correspond to the actual row number. 
# To achieve this you can use reset_inex(). 
# In other cases you might want to keep the index as it is to more easily refer back to the original dataframe. 
# It all depends on the context of your project.
new_df = df[df["year"] == 2022]
new_df = new_df.reset_index(drop=True)
new_df

df.describe()

# To view the plotting graph you might need to use plt.show() from matplotlib.pyplot
df.plot()
df.plot(kind='scatter', x='log_gdp_per_capita', y='life_ladder')



# Create a dictionary to map the country names to colors
cmap = {
    'Brazil': 'Green',
    'Slovenia': 'Orange',
    'India': 'purple'
}

df.plot(
    kind='scatter',
    x='log_gdp_per_capita',
    y='life_ladder',
    c=[cmap.get(c, 'yellow') for c in df.country_name], # Set the colors
    s=2 # Set the size of the points
    )

df.hist("life_ladder")

#You can use other external libraries to easily produce various advanced plots. 
# One of such libraries is Seaborn. 
# You have already imported it at the beginning of this lab using import seaborn as sns. 
sns.pairplot(df)


# Create a new column which is the sum of the year and the value on the life ladder.
df["this_column_makes_no_sense"] = df["year"] + df["life_ladder"]
# Create a new column which is the difference of two columns.
df["net_affect_difference"] = df["positive_affect"] - df["negative_affect"]

df.head()

# Using df.apply() with a lambda function
# Rescale the life_ladder column to values between 0 and 1 and save it to a new column
df['life_ladder_rescaled'] = df['life_ladder'].apply(lambda x: x / 10)

# Using df.apply() with your own function
# First define a function. The function can do whatever you want. This example will double the column's values
def my_function(x):
    # do stuff to x
    y = x * 2
    return y
# Apply the function.
df['my_function'] = df['life_ladder'].apply(my_function)

# Show the new dataframe
df.head()