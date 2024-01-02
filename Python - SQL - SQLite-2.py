#Dynamic Query

import sqlite3

conn = sqlite3.connect("just_a_database_name.db")
cursor = conn.cursor()




#Reading Data

cursor.execute("SELECT Email FROM Users WHERE Id = 2")      #Selecting the data which we want to read with cursor
test_email = cursor.fetchone()      #cursor.fetchone() returns a  tuple

print(test_email) 

#COUNTING TOTAL USERS AND ID
cursor.execute("SELECT COUNT(*) FROM Users")
id = cursor.fetchone()      #cursor.fetchone() returns a tuple
print(id, type(id))



#Exercise - Playing with database for a bit
print("\n\n")
user_email = input("Please enter your email?")

cursor.execute("SELECT Email FROM Users")
all_email = cursor.fetchall()           #cursor.fetchall() returns a list
print(all_email, type(all_email))

if user_email in all_email[0]:
    print("Congrats! You're an User!!")
else:
    user_password = input("You are not an user. To be a new user, please enter your new password.")








    #Creating a New USER           #======================  DYNAMIC QUERY  =====================================
    next_id = id[0] + 1
    print(next_id, type(next_id))

    cursor.execute("INSERT INTO Users VALUES(:id, :user_email, :user_password, 0)", {"id" : next_id, "user_email" : user_email, "user_password" : user_password})              
                        # To put a dynamic value inside a sql query we use dynamic place holder
                        # That is, we put a --  key (of a dictionary) -- and before it we put a colon (:) , and, in the second parameter of the function cursor.execute()  we pass a dictionary with same key as we passed as a dynamic_value_placeholder in the SQL query. The value of that key from the dictionary (we passed in the second parameter) gets replaced to the SQL query
                        # We could have also used concatanation, but that will increase the chance of getting hacked
                        # You could have multiple placeholders, make sure every named parameter on your dinamic query exists as the key of the dictionary you are passing in the second parameter.
    conn.commit()


    #Reading the new User
    cursor.execute("SELECT * FROM Users WHERE Id = :id", {"id" : next_id})
    user = cursor.fetchone()      #cursor.fetchone() returns tuples
    print("Contratulation you are an user now, here is your details: ",*user)        #unpacked tuple with an asterisk



















# ==========================================   DISTINCT KEYWORD ===================================
    
# If you want to read only one value , no duplicate data from a column then use Distinct kw
    
cursor.execute("SELECT DISTINCT City FROM Friends")         #Suppose you have a table named -- Friends -- and all friends has a city column
                                                            # Two or more friends could be from the same city
                                                            # But you wanna only know from how many cities you got friends
                                                            #Then with distinct kw , it will give you each name of the city only one time.
                                                            # You only wanna know all the cities, not wanna watch a city again and again












# =====================================   LIMIT KEYWORD =============================================

# Let's say you got a table with few millions of rows but you wanna read only the first 5 or 10 lines

cursor.execute("SELECT * FROM Customers LIMIT 10")      # It will only read first 10 lines of the -- Customer -- table
















#=============================================   Advanced Filters  ====================================

# When you want to select some particular rows from a table, lets say with id = 5, id = 8 and id = 10

#Below 2 lines are the same
cursor.execute("SELECT * FROM Users WHERE Id = 5 OR Id = 8 OR Id = 10")     #Though It has used -- OR -- but it will read all the rows
cursor.execute("SELECT * FROM Users WHERE Id IN (5, 8, 10)")    # With the -- IN -- keyword inside the parenthesis you can pass all the values, if any of the value is matched, that row will be selected




















# =======================================  Goldfish Memory : Databases Pattern Match ================================

#Let's say you don't remember full email of the user you are lookin for, you can just partially remember it like it ends with -- @yahoo.com ---- 
# If you use -- WHERE -- Keyword it will look for complete match, and hence will not find any data or row
# In that case to find all the user, whose email ends with -- @yahoo.com -- you have to do two things, instead of equal sign use the kw -- LIKE -- and use percentage sign -- % -- on the side of the string you don't know. see example below

cursor.execute("SELECT * FROM Users WHERE Email LIKE '%@yahoo.com' ")
cursor.execute("SELECT * FROM Users WHERE Email LIKE 'mail@aft%'  ")    # When you have forgot the last part of the email

