import pandas as pd

# ========= Read CSV using Pandas  =============

#Reading a CSV file
csv1 = pd.read_csv("E:\\Programming\\Python projects\\Python - Pandas Module\\My_CSV_3.csv")    #pd.read_csv(file location)
print(csv1)
print(type(csv1))


#Accessing number of rows in csv from the beginning of the file
csv2 = pd.read_csv("E:\\Programming\\Python projects\\Python - Pandas Module\\My_CSV_3.csv", nrows = 2)     # pd.read_csv(file_location, nrows = number of rows), it will return that many rows from the beginning of the file
print(csv2)
print(type(csv2))


#Accessing particular columns from csv file
csv3 = pd.read_csv("E:\\Programming\\Python projects\\Python - Pandas Module\\My_CSV_3.csv", usecols = ["header2", "header3"])    #pd.read_csv(file_location, usecols = list of column_headers/column_index) , you can use either column_header or column_index(0,1,2..)
print(csv3)


#Skipping particular rows while reading the csv file
csv4 = pd.read_csv("E:\\Programming\\Python projects\\Python - Pandas Module\\My_CSV_3.csv", skiprows = [2])    #pd.read_csv(file_location, skiprows = list of row indexes), the index 0 of row is the column_header
print(csv4)


#Making a particular column work as the index of all rows of the csv file
csv5 = pd.read_csv("E:\\Programming\\Python projects\\Python - Pandas Module\\My_CSV_3.csv", index_col = "header2")     #Now each of the value of this column will work as the index of their respective row
print(csv5)


#Making a particular row work as the header of all columns of the csv file
csv6 = pd.read_csv("E:\\Programming\\Python projects\\Python - Pandas Module\\My_CSV_3.csv", header = 2)   #Now each of the value of this row will work as the header/headline of their respective column
print(csv6)                                                                                                     #Note: When you make a row the column heading, the other rows above the new heading is not read then i.e only under the new_column heading rows are read by pandas


#Creating new heading for each of the column
csv7 = pd.read_csv("E:\\Programming\\Python projects\\Python - Pandas Module\\My_CSV_3.csv", names = ["NewHeader1", "NewHeader2", "NewHeader3"])    #This new header will go above the row of old header, and old header will still exist
print(csv7)
 

#Creating Customized header 
            #The first row is always count as header when you read a csv file, if you don't want to do that rather use the default index(0, 1, 2..) for the header, you can do that as well
            # By using parameter (header = None) The first row will no more be counted as header of the column, rather the header will be the default index value (0, 1, 2 ..)
csv8 = pd.read_csv("E:\\Programming\\Python projects\\Python - Pandas Module\\My_CSV_3.csv", header = None)     #The existing header will be counted as the first row, and the header will be column default index number
print(csv8)


#Changing the data type of particular columns
csv9 = pd.read_csv("E:\\Programming\\Python projects\\Python - Pandas Module\\My_CSV_3.csv", dtype = {"header2" : "float"})     # -- dtype -- parameter takes dictionary where the keys are the column_header and the values are the data_type
print(csv9)
