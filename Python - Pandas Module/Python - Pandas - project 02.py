import pandas as pd

#Datasheet : https://www.kaggle.com/datasets/utkarsharya/ecommerce-purchases

dframe1 = pd.read_csv("Ecommerce Purchases")
print(dframe1, type(dframe1))            #Viewing the data (total 10,000 rows)



#Display top 10 and last 10 rows of the dataset
top1 = dframe1.head(10)
print(top1)

last1 = dframe1.tail(10)
print(last1)




#Check Datatype of each column
dtype1 = dframe1.dtypes         #Not a method , an attribute of dataframe_object
print(dtype1)






#Check Null Values in the dataset
null1 = dframe1.isnull()        #It returns same number of values as the original dataframe, but with boolean value, True for Null and False for any other value
print(null1)

null2 = null1.sum()         #We summed up all the True values in each column, to get the idea about how many null value is in each column
print(null2)





#How many rows and columns in the dataset

number1 = dframe1.columns   #an attribute,, returns a list of all the column_name in each element
print(number1)
number4 = len(number1)      #Counting the number of column
print(number4)

number2 = dframe1.index     #an attribute,, returns the index number of data in start, stop, step, way
print(number2)
number5 = len(dframe1)      #Returns the total number of rows (not index)
print(number5)

number3 = dframe1.shape     #Full shape of the dataframe_object (row, column)
print(number3)

number6 = dframe1.info()    #Getting all the info about the dataframe_object
print(number6)










#Find the highest and lowest purchase price

num1 = dframe1["Purchase Price"].max()
print(num1)

num2 = dframe1["Purchase Price"].min()
print(num2)








#Find Average purchase price
num3 = dframe1["Purchase Price"].mean()         #Returns the arithmatic mean of all the values of a column
print(round(num3, 2))








#How many people have French 'fr' as their language
column1 = dframe1.columns       #An attribute
print(column1)          #Checking the column name first to understand in which column we have to perform the operation

lang1 = dframe1["Language"] == 'fr'     #It will return series_object, with boolean values, if the column_value is 'fr' it will be True, Otherwise False
print(lang1)

lang2 = lang1.sum()     #Summing up the true values
print(lang2)

#Alternative
lang3 = dframe1[lang1]  #It will return a dataframe_object, For each row, if the passed value is True, the row will be added, if False that indexed row will be dropped,, i.e only the rows with language 'fr' will exist only
print(lang3)

lang4 = len(lang3)      #Now we can get the length (total row number) of the dataframe_object
print(lang4)            #Thus we got the value



#Alternative
lang5 = lang3.count()       #It will also return the total number of rows that exist in the dataframe_object, for all columns individually
print(lang5)









#Find Job title which contains Engineer
column2 = dframe1.columns       #An attribute
print(column2)          #Checking the column name first to understand in which column we have to perform the operation

job1 = dframe1["Job"] == "Engineer"         #There is no value as of engineer as a full string in the data, but it has partially engineer (like, drilling engineer, energy engineer)
print(job1)                         #These have been already explained before

job2 = dframe1[job1]
print(job2)

job3 = dframe1["Job"].str.contains("engineer", case = False)  # -- str.contains() -- is a mothod of string, it returns boolean value based on if the parameter passed within it contains on the object_value(in here, each row of series_object) or not
print(job3)                                     #we will get a series.object with boolean values based on whethed the original series_object value of each row contained "engineer" or not
                                                #By default the --str.contains() -- method is case sensitive, to make case insensitive search we passed the parameter -- case=False --

job4 = dframe1[job3]        #We will get only the rows of the dataframe_object based on the boolean value of passed series_object(job3)
print(job4)

job5 = len(job4)        #Finding the length (total number of rows) of the dataframe
print(job5)























#Find the Email of the person with the following IP Address 132.207.160.22

column3 = dframe1.columns       #An attribute
print(column3)          #Checking the column name first to understand in which column we have to perform the operation


check1 = dframe1["IP Address"].dtype    #Not a method, an attribute     ,, finding the data type of the value IP Address column_name contains (string or float)
print(check1)


ip1 = dframe1["IP Address"] == "132.207.160.22"         # It will return the same shape series_object with all the Value False, except for the rows where the condition is True
print(ip1)          
ip2 = dframe1[ip1]  #When we pass a series_object or list of boolean values, in dataframe_object index position both having same rows(for list, elements) , we only get that index_position rows in which index_positions the passed parameter is True 
print(ip2)
ip3 = ip2["Email"]      #As we have filtered the dataframe_object , we can get the email value by indexing the column_name "Email"
print(ip3)


















#How many people have Mastercard as their Credit Card Provider and made a purchase above 50

column4 = dframe1.columns       #An attribute
print(column4)          #Checking the column name first to understand in which column we have to perform the operation

card1 = (dframe1["CC Provider"] == "Mastercard")  & (dframe1["Purchase Price"] > 50)        #When we use two or more conditions at a time to compare datframe/series objects, we use the bitwise operator -- & -- not the logical operator -- and --
print(card1)                                                                                    #Also we have to partition each condition with a parenthesis, It returns the boolean value series_object

card2 = dframe1[card1]   #Filtering the values (rows) based on boolean values   
print(card2)

card3 = len(card2)  #Finding the total length (row number),, also we could have use -- card2.count() --
print(card3)


















#Find Email of the person with the following Credit Card Number: 46648258997302

column5 = dframe1.columns       #An attribute
print(column5)          #Checking the column name first to understand in which column we have to perform the operation

print(dframe1["Credit Card"].dtype )        #Checking the data type of credit card column



cc1 = dframe1[dframe1["Credit Card"] == 4664825258997302]["Email"]      #Performing everything in one line now, as the process of how it works has already been described
print(cc1)


















#How many people purchase during the AM and how many during the PM

am1 = dframe1[dframe1["AM or PM"] == "AM"]["AM or PM"].count()      #  counting the rows using the -- count -- method,, though it gives the result for all the columns individually, for that we chose only one column and added at the end ["AM or PM"]
print(f"AM: {am1}")

pm1 = len(dframe1[dframe1["AM or PM"] == "PM"])         # counting the rows using the -- len -- function
print(f"PM: {pm1}")


#Alternative
ampm1 = dframe1["AM or PM"].value_counts()      # -- value_counts() -- method returns use how many times each unique value has been repeated (count of each individual value)
print(ampm1)



















#How many people have a credit card that expires in 2020

column5 = dframe1.columns       #An attribute
print(column5)          #Checking the column name first to understand in which column we have to perform the operation

print(dframe1["CC Exp Date"], type(dframe1["CC Exp Date"]))         #The value is in MM/YY format , so we have to split the data on '/' to get the year

exp1 = dframe1["CC Exp Date"].str.split("/")        #Now each row has a list value which has two elements [MM, YY] 
print(exp1)

exp2 = list(exp1)   #Converting series_object into list
print(exp2)

exp3 = [year[1] for year in exp2 if year[1] == "20"]    #Using list comprehension and accessing the second element, because first element is the Month an second Year
print(len(exp3))            #Getting the total number



#Alternative
def exp4():
    count = 0
    for date in dframe1["CC Exp Date"]:      #Iterating over a global variable (series_object), as we don't overwrite it we don't need to declare kw -- global --
        if date.split("/")[1]  == "20":      #As -- date -- (each row value of the series_object) is itself a string, we called -- split() -- instead of -- str.split() -- and the index position 1 because in the returne value from string mehod there will be 2 elements, one month second year
            count += 1
    return count

print(exp4())



#Alternative
exp5 = dframe1["CC Exp Date"].apply(lambda x : x[3:] == "20")   #You know how lambda / anonymous function works -- lambda input_value : output_value --  Also you know how apply method works, it runs the passed function for each value of the series_object, and returns new series with the passed funcions return value
print(exp5)                                                     # as the string is like -- 06/20 -- if we slice it from index_position 3 (included) then we get the year, here the returned series_object will be of boolean values

exp6 = len(dframe1[exp5])   #Finding the length of the filtered dataframe object (filtered based on boolean value)
print(exp6)




















#Find Top 5 most popular Email Providers (e.g. gmail.com, yahoo.com)
column6 = dframe1.columns       #An attribute
print(column6)          #Checking the column name first to understand in which column we have to perform the operation

email1 = dframe1["Email"].str.split("@")    #Splitting the email column into two string parts, and returned a series_object where each row contains a list of those two parts
print(email1)

email2 = [email[1] for email in list(email1) ]      #Using List comprehension getting only the name providers
print(email2)

email3 = pd.Series(email2)  #Converting again to series_object
print(email3)

email14 = email3.value_counts()     #With -- value_counts() -- we can find many times each unique value occured in an descending manner
print(email14.head(5), type(email14))



#Alternative
list1 = list()      #Creating an empty list

for row in dframe1["Email"]:            #Iterating over the series object, the loop_variable is the email of each row each time
    list1.append(row.split("@")[1])      # Splitting the loop variable with '@' and appending the second element to list, (index 1 , because there is where the name provider is)

dframe1["Name_Provider"]  = list1   #Creating a new column in the dataframe_object
print(dframe1)

email5 = dframe1["Name_Provider"].value_counts().head(5)        #With -- value_counts() -- we can find many times each unique value occured in an descending manner,, and head(5) for most popular 5, though by default it will also show top 5 rows if no parameter passed
print(email5)




#Alternative
email15 = dframe1["Email"].apply(lambda x : x.split("@")[1]).value_counts().head()      #All explained already
print(email15)

