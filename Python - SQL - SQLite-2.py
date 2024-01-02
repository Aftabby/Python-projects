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

