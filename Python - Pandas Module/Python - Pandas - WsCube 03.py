import pandas as pd

# ============ Arithmatic Operators in Pandas  =============== 

#Arithmatic operationg between two columns of the same dataframe and storing it into another column of that same dataframe
dict1 = {"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]}
dframe1 = pd.DataFrame(dict1)
print(dframe1)

dframe1["A+B"] = dframe1["A"] + dframe1["B"]
print(dframe1)
dframe1["B-A"] = dframe1["B"] - dframe1["A"]
print(dframe1)
dframe1["A*B"] = dframe1["A"] * dframe1["B"]
print(dframe1)
dframe1["B/A"] = dframe1["B"] / dframe1["A"]


#Checking a column with comparison operator, and assigning the value into another column of the same dataframe
dframe1["Is B >= 7 ??"] = dframe1["B"] >= 7
print(dframe1)