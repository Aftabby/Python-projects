import pandas as pd

#============Top 10 most used function in pandas ===============

dict1 = {"age":[25, 22, 18, 30, 45, 50, 35, 20, 55, 40],
         "gender":["M", "F", "F", "M", "M", 'F', "M", "F", "M", "M"],
         "score":[90, 80, 75, 95, 70, 85, 75, 90, 95, 85]
         }

df1 = pd.DataFrame(dict1)


#Value_Counts
val1 = df1["gender"].value_counts()
print(val1)


val2 = df1["gender"].value_counts(normalize=True)
print(val2)











#Where()

where1 = df1.where(df1["age"]>30, other=0).all(True)
print(where1)













#Isin()
df2 = df1["age"].isin([25, 35])     #It will return a boolean series where the value of age column is 25 or 35
print(df2)


df3 = df1[["age", "gender"]].isin({"age":[25, 35], "gender":["M"]}).all(True)
print(df3)















#Cut and Qcut
            #It is used to divide a set of continous variable into a set of discrete variable

df1["score_bins"] = pd.cut(df1["score"], bins=[60, 70, 80, 90, 100])
print(df1["score_bins"])


df1["score_equal_bins"] = pd.qcut(df1["age"], 4)        #It will cut the range into 4 equal parts and make bins out of it
print(df1)









#Groupby











#Pivot_table
pivot1 = df1.pivot_table(index="gender", values="score", aggfunc="mean")
print(pivot1)














#Nlargest and Nsmallest
n1 = df1["score"].nlargest(3)
n2 = df1.nlargest(3, "score")   #same

print(n1, n2)




n3 = df1["score"].nsmallest(3)
n4 = df1.nsmallest(3, "score")   #same

print(n3, n4)














#Query 
q1 = df1.query("age>25 and gender=='F'")

print(q1)






#Apply

