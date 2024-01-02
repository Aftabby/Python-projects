import sqlite3  #importing library that will help to use database sqlite by python

# SQL is case insensitive, but here we will follow SQL Queries will all uppercase


#Creating table and INserting data
conn = sqlite3.connect("just_a_database_name.db")    #connecting to the database name

cursor = conn.cursor()  #The cursor for CRUD data in database

#Add queries below
#cursor.execute("CREATE TABLE Users (Id INTEGER PRIMARY KEY, Email TEXT UNIQUE, Password TEXT NOT NULL, Friends INTEGER)")   #The query is in SQL, here we created a table named user, and mentioned the columun and column data type  #Creating table is applicable for the first time only, if you have created a table already then trying to create it again while running the code multiple time might give an error
                                                                                                            # -- NOT NULL  -- is a rule for the column (Column Constrains), you put these rule after the column_name and column_data type, Here if while inserting data if you inserting NULL value to this column, the database will throw an exception
                                                                                                            # Another Rule (Constraint) is -- UNIQUE -- it means you can't repeat one value twice ,, you don't want any duplicate email address in the email column
                                                                                                             # -- PRIMARY KEY -- is another column constraint (column rule), it creates an unique id for each row (like your varsity student id number), PRIMARY KEY is used to find a row very quickly
                                                                                                                # only difference between PRIMARY KEY and UNIQUE is that in UNIQUE you can create one NULL value (you can't duplicate any value),, but PRIMARY KEY constraints don't allow any NULL value


#Adding data row to the table
cursor.execute("INSERT INTO Users VALUES(1, 'ca@aftabby.com', 'paaasssword', 227)") #Inserting value/data to the table as rows
cursor.execute("INSERT INTO Users VALUES(2, 'sukumar@gmail.com', 'sukuuuumaar', 5667)")
cursor.execute("INSERT INTO Users VALUES(3, 'hello@aftabby.com', 'kalakala', Null)")   #Null means None, it means empty or no value
cursor.execute("INSERT INTO Users VALUES(4, 'hunott@gmail.com', 'apass1234', 334)")


#saving the changes in database
conn.commit()
#closing the connection to the database
conn.close()














#Reading/Selecting the data as a query from the database
conn = sqlite3.connect("just_a_database_name.db")
cursor = conn.cursor()

#Reading Data
cursor.execute("SELECT * FROM Users")   #Here we are reading all the columns and rows from the table -- Users -- asterisk means all (*), but if you wanna read a particular columns, just put the column name in the place of asterisk, (COLUMN 1, COLUMN 2)
                                        # If you want to read a any data that doesn't exist (example an email) , then you will get the Keyword -- None --

#To see the data you have to call the fetchall method on the cursor, and store it inside a variable like below-
users = cursor.fetchall() # Once you have fetch all the data, you can print all the data.
                        #The fetchall method gives you all the data in the query, if you want to get only the first matching row use -- fetchone() -- method
                        # Also using -- fetchone -- method you can read columns by index - example given below

cursor.execute("SELECT * FROM Users")   #Again selecting all the data to use the fetchone method
user = cursor.fetchone()    #fetchall retrieves all selected row, whereas the fetchone method returns the first matched selected row object

#Printing the read data
print("\nUsing fetchall")
print(users, type(users))   #If you wanna see all the users
for each_user in users:     #If you wanna see by the row, that mean each user
    print(each_user)
    print(each_user[2], each_user[1])   #You can access any column of a particular row ;; the index comes as the order of the columns in the select statement, if you use -- * -- to select all the column, then the order will be the order defined while declaring the table (creating the table)

print("\nUsing fetchone")
print(user)
print(user[3], user[1], user[2])    #While using fetchone method to retrieve data, the index comes as the order of the columns in the select statement, if you use -- * -- to select all the column, then the order will be the order defined while declaring the table (creating the table) - You can access any column


#Data Retrieve by ORDER
# SQLite doesn't guarantee order of the row as you have added it - but there are keywords to do that
cursor.execute("SELECT * FROM Users ORDER BY Id")   # To get the data row just as the order as you have added it, you can use the keyword -- ORDER BY -- just like the example
cursor.execute("SELECT * FROM Users ORDER BY Id ASC")   # Here ASC means ascending order, that means you'll get the data by the value of - Id - from smallest value to largest value order
cursor.execute("SELECT * FROM USers ORDER BY Friends DESC") # Same As before, just in descinding order by the value of column - Friends


#Committing and closing the database
conn.commit()
conn.close()
















#Updating data queries of the database

conn = sqlite3.connect('just_a_database_name.db')
cursor = conn.cursor()


cursor.execute("UPDATE Users SET Password = 'updated password' where Id = 3")


conn.commit()
conn.close()













#Deleting the User
conn = sqlite3.connect('just_a_database_name.db')
cursor = conn.cursor()


cursor.execute("DELETE FROM Users WHERE Id = 4")    #IT will delete an entire row
cursor.execute("DELETE FROM Users") #Deleting all the data so that we don't write same data over and over each time we run the programme, and the database will be remain empty

conn.commit()
conn.close()