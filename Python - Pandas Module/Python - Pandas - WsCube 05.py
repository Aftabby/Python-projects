import pandas as pd

# ============= Write CSV using Pandas =======

dict1 = {"A": [1, 2, 3, 4], "B": [5, 6, 7, 8], "C" : [10, 11, 12, 13]}
dframe1 = pd.DataFrame(dict1)
print(dframe1)

#Creating CSV file in the root folder
dframe1.to_csv("My_CSV_1.csv")      # dataframe_name.to_csv(csv_file_name)

#Creating CSV without the index in first row
dframe1.to_csv("My_CSV_2.csv", index = False)

#Creating CSV with customized head-data/column_headline
dframe1.to_csv("My_CSV_3.csv", header = [ "header1", "header2", "header3"])


