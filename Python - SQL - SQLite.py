import sqlite3  #importing library that will help to use database sqlite by python


#Creating table and INserting data
conn = sqlite3.connect("just_a_database_name.db")    #connecting to the database name

cursor = conn.cursor()  #The cursor for CRUD data in database

#Add queries below
cursor.execute("CREATE TABLE Users (Id INTEGER, Email TEXT, Password TEXT, Friends INTEGER)")   #The query is in SQL, here we created a table named user, and mentioned the columun and column data type  #Creating table is applicable for the first time only, if you have created a table already then trying to create it again while running the code multiple time might give an error
cursor.execute("INSERT INTO Users VALUES(1, 'ca@aftabby.com', 'paaasssword', 227)") #Inserting value/data to the table as rows
cursor.execute("INSERT INTO Users VALUES(2, 'sukumar@gmail.com', 'sukuuuumaar', 5667)")
cursor.execute("INSERT INTO Users VALUES(3, 'hello@aftabby.com', 'kalakala', 12)")
cursor.execute("INSERT INTO Users VALUES(4, 'hunott@gmail.com', 'apass1234', 334)")


#saving the changes in database
conn.commit()
#closing the connection to the database
conn.close()














#Reading/Selecting the data as a query from the database
conn = sqlite3.connect("just_a_database_name.db")
cursor = conn.cursor()

#Reading Data
cursor.execute("SELECT * FROM Users")   #Here we are reading all the columns and rows from the table -- Users --

#To see the data you have to call the fetchall method on the cursor, and store it inside a variable like below-
users = cursor.fetchall() # Once you have fetch all the data, you can print all the data.
                        #The fetchall method gives you all the data in the query, if you want to get only the first matching row use -- fetchone() -- method
                        # Also using -- fetchone -- method you can read columns by index - example given below

user = cursor.fetchone()    #fetchall retrieves all selected row, whereas the fetchone method returns the first matched selected row object

#Printing the read data
print(users, type(users))   #If you wanna see all the users

for each_user in users:     #If you wanna see by the row, that mean each user
    print(each_user)
    print(each_user[0], each_user[1])

print(user)
print(user[0], user[1], user[2])    #While using fetchone method to retrieve data, theindex comes as the order of the columns in the select statement, if you use -- * -- to select all the column, then the order will be the order defined while declaring the table (creating the table)

#Committing and closing the database
cursor.commit()
conn.close()














#Updating data queries of the database

conn = sqlite3.connect('just_a_database_name.db')
cursor = conn.cursor()


cursor.execute("UPDATE Users SET Password = 'updated password' where ")