import pandas as pd

#Top 10 must know pandas string functions for data analysis


dict1 = {'Name': ['Priyang Bhatt', 'Rashmin Panchal', 'Anil Rana', 'Rahul Patel'],
        'City': [' New York ', ' Los Angeles ', ' Chicago', ' Houston'],
        'State': ['NY', 'CA', 'IL', 'TX']}
df1 = pd.DataFrame(dict1)

print(df1)



#str.lower()     and str.upper()
df1["Name_lower"] = df1["Name"].str.lower()
print(df1)

df1["Name_upper"] = df1["Name"].str.upper()
print(df1)








#str.len()

df1["Name_length"] = df1["Name"].str.len()
print(df1)











#str.strip()            -- removes trailing whitespaces from the beginning and the end of the string 
df1["City_noSpace"] = df1["City"].str.strip()
print(df1)

df1["City_noSpaceRight"] = df1["City"].str.rstrip()
print(df1)

df1["City_noSpaceLeft"] = df1["City"].str.lstrip()
print(df1)














#Str.split()
df1["First_name"] = df1["Name"].str.split(" ", expand=True)[0]      # -- expand=True -- means the return value will be returned as a series object, where each value as one row

df1["Last_name"] = df1["Name"].str.split(" ", expand=True)[1]

print(df1)


















#Str.contains()
check1 = df1["Name"].str.contains("Bhatt")
print(check1)









#Str.replace()
df1["State_full"]= df1["State"].str.replace("NY", "New York").str.replace("CA", "California")
print(df1)











#str.startswith()   and str.endswith()
check2 = df1["First_name"].str.startswith("P")
check3 = df1["Last_name"].str.endswith("l")

print(check3)
print(check2)










#Str.cat()
df1["Full_name"] = df1["First_name"].str.cat(df1["Last_name"], sep=" ")
print(df1["Full_name"])









#Str.get()
check4 = df1["Name"].str.split().str.get(1)
print(check4)










#Str.slice()
check5 = df1["Name"].str.slice(0, 3)
print(check5)











#Str.find()     and  str.rfind()
check6 = df1["Name"].str.find("i")      #Returns the index of first occurance if found otherwise -1
print(check6)

check7 = df1["Name"].str.rfind("a")      #Returns the index of last occurance if found otherwise -1
print(check7)
