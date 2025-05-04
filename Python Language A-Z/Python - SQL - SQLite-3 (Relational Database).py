# Relational Database, is actually relation between two tables
# For example, one table has data of all the parents, and another table has data of all the children, then the ralation between two table is, one couple from parents table has relation with one or more children from the children's table
# This relation is maintained by the same column (Family Id) and matching values for both the table
# Here the column --- FamilyId  -- is the Primary Id of the -- Parents -- table , And we will be using that Primary Id in the -- Children -- table as well. 
# And when we use a Primary Key of one table to another table, the second table column is a -- Foreign Key Column -- . Because it refers to a primary key of another table. Hence the FamilyId column in the Children table is a Foreign Key
# Foreign Key -- refers Primary Key of another table to build relation


# Example of the relational table below:
'''
    Table 1 : Parents Table                                                                 Table 2 : Children Table
    ---------------------------
Family Id      Father          Mother                                               Child Id              FamilyId        Child
----------     --------         ----------                                         ----------             ---------       -------------
0100            Habib           Natasha                                                 101                0100            Rocky
0200            Labib           Lamiya                                                  102                0100            Altaf
0300            Abir            Sumaiya                                                 103                0200            Siam
                                                                                        104                0300            Tuhin
                                                                                        105                0300            Alfaz

'''




# We could have made the table like below as well which is a bad practice

'''
                                Table 3 :  Family Table
                                -----------------------
            Family Id               Father              Mother                      Child
            ---------               -------             -------                     -----------
            0100                    Habib               Natasha                     Rocky
            0100                    Habib               Natasha                     Altaf
            0200                    Labib               Lamiya                      Siam
            0300                    Abir                Sumaiya                     Tuhin
            0300                    Abir                Sumaiya                     Alfaz
'''

# Here you will see father and mother information repeating a lot, To avoid duplicate you can simply break the table into many tables, and thus a primary key is required to maintain a relation between all the tables
# NORMALIZATION : The approach of breaking down a large table into multiple smaller table is called Normalization. We normalize to avoid duplicate entries and gives up flexibility to play with data easily. Also updating a duplicate data becomes a lot easier
# DeNORMALIZATION : The opposite of breaking down into smaller table is combining together, combining multiple tables into a large table is called denormalization







# ==========================================  Inner Join  =================================

#There are few kinds of join: Inner Hoin, Outer Join, Left Join, Cross Join, Self Join


import sqlite3

conn = sqlite3.connect('just_a_database_name.db')
cursor = conn.cursor()


#Creating Parents Table (You only need to run the below line once)

#cursor.execute("CREATE TABLE Parents (FamilyId INTEGER PRIMARY KEY, Father TEXT, Mother TEXT)") #You know why we commented it out

#Inseritng Values / Data / Rows of Parents Table

cursor.execute("INSERT INTO Parents VALUES(0010 , 'Habib', 'Natasha')")
cursor.execute("INSERT INTO Parents VALUES(0020 , 'Labib', 'Lamiya')")
cursor.execute("INSERT INTO Parents VALUES(0030 , 'Abir', 'Sumaiya')")


#Createing Children Table (You only need to run the below line once)

#cursor.execute("CREATE TABLE Children (ChildId INTEGER PRIMARY KEY, Name TEXT, FamilyId INTEGER)")

#Inserting Values / Data / Rows of Children table

cursor.execute("INSERT INTO Children VALUES(101, 'Rocky', 0010)")
cursor.execute("INSERT INTO Children VALUES(102, 'Altaf', 0010)")
cursor.execute("INSERT INTO Children VALUES(103, 'Siam', 0020)")
cursor.execute("INSERT INTO Children VALUES(104, 'Tuhin', 0030)")
cursor.execute("INSERT INTO Children VALUES(105, 'Alfaz', 0030)")





# Now we wanna know the mother's name of each of the child, for that we have to join to tables, because two different information is in two tables
# We will do it with the help of - INNER JOIN - keyword, table with which you wanna join, Matching columns from both tables
# ---  " INNER JOIN Parents ON Children.FamilyId = Parents.FamilyId"

cursor.execute("SELECT Name, Mother FROM Children INNER JOIN Parents ON Children.FamilyId = Parents.FamilyId")

family = cursor.fetchall()

print( family, sep='\n')


#Saving the file in the database
conn.commit()
#Closing the connection
conn.close()