import pandas as pd
import numpy as np

# ==== CSV File Function using Pandas ====

csv1 = pd.read_csv("E:\\Programming\\Python projects\\Python - Pandas Module\\My_CSV_3.csv")    #Reading csv file
print(csv1)

# Getting just the index number of a csv file
total_index1 = csv1.index       
total_index2 = csv1.index.array     #Getting all the index inside an pandas array
print(total_index1, type(total_index1))         #start, stop, step ; stop value is always the (total number of index + 1)
print(total_index2, type(total_index2))



# Getting the name/header of all the columns
all_columns = csv1.columns
print(all_columns)


# Getting -- count, mean, std, min, 25%, 50%, 75%, max -- of each of the columns (only for the numerical column, other data type columns will be ignored)
describe_cols = csv1.describe()
print(describe_cols)


# Accessing only the initial rows and the last rows of the csv file -- (it is needed for the big data)
initial_rows = csv1.head(2)     # pass the number of initial rows you want to access, If you don't pass any parameter, by default it will show the first five rows of the csv
print(initial_rows)

last_rows = csv1.tail(2)        # pass the number of last rows you want to access, If you don't pass any parameter, by default it will show the last five rows of the csv
print(last_rows)


# Slicing rows - or accessing particular rows of the csv
particular_columns = csv1[:1]
print(particular_columns)


# Converting the csv to a numpy array
    #Below two lines does the same thing
arr1 = csv1.to_numpy()
arr2 = np.asarray(csv1)
print(arr1)
print(arr2)


#Sorting The csv file in descending order based on index number     
            #axis=0 means according to row, axis=1 means according to column
reverse_csv = csv1.sort_index(axis = 0, ascending = False)
print(reverse_csv)


# Changing a particular value from the csv
csv1["header2"][2] = 70         #csv_object[column_header][row_index] = new_value       #N.B: It is not the right way to change the value
print(csv1)

csv1.loc[2, "header2"] = 700    # csv_object.loc[row_index, column_header] = new_value     #N.B: It is the right way to change the value
print(csv1)


#Accessing particular rows and columns from the csv
partial_csv1 = csv1.loc[[0, 2], ["header1", "header3"]]      # csv_object.loc[list_of_all_row_index, list_of_all_column_header]
print(partial_csv1)

partial_csv2 = csv1.loc[ : , ["header1", "header3"]]        # Here colon(:) means all the rows
print(partial_csv2)

partial_csv2 = csv1.loc[[0, 2], :]        # Here colon(:) means all the columns
print(partial_csv2)


#Accessing a single data from the csv
value1 = csv1.iloc[2, 3]            # csv_object.iloc[row_index, column_index]  --- column index not column header
print(value1)


#Dropping a particular row or column
partial_csv3 = csv1.drop("header2", axis = 1)       #For dropping a column, --  csv_object.drop(column_header, axis = 1)
print(partial_csv3)

partial_csv4 = csv1.drop(2, axis = 0)       #For dropping a row, -- csv.object.drop(row_index, axis = 0)
print(partial_csv4)




