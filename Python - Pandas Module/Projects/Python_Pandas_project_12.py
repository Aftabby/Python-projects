import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


dict1 ={'Name':['Priyang','Aadhya','Krisha','Vedant','Parshv',
                'Mittal','Archana'],
                'Marks':[98,np.nan,99,87,np.nan,83,99],
                'Gender':['Male','Female','Female','Male','Male',
                         'Female','Female'],
                'Email':['priyang@gmail.com','aadhya@gmail.com',
                        'krisha@gmail.com','vedant@yahoo.com','parshv@hotmail.com',
                         'mittal@yahoo.com','archana@yahoo.com']
               }
df1=pd.DataFrame(dict1)
print(df1)



#Print all the rows except the last two rows of the dataset
print(df1.head(-2))


#Print all the rows except the first two rows of the dataset
print(df1.tail(-2))


#Shape
print(df1.shape)




#Get information about the dataset
df1.info()




#Check null values in the dataset
print(df1.isnull().sum())












#Get overall stats about the data set
print(df1.describe())   #You can add -- include = "all" --






#Find unique values from the gender column
print(df1.Gender.unique())








#Find the number of unique values from the gender column
print(df1.Gender.nunique())









#Display count of unique values in gender column
print(df1.Gender.value_counts())








#Handling missing values

#df1 = df1.dropna(how="any")     # -- how="any" -- means if any value is missing drop the row, -- how="all" -- if the whole row is NaN drop that row

#df1 = df1.fillna(0)
df1["Marks"] = df1.Marks.fillna(df1['Marks'].mean())























#Marks between 80 - 90

df2 = df1[(df1['Marks']>=80) & (df1["Marks"]<=90)]
print(df2)

        #Alternative
df3 = df1[df1["Marks"].between(80, 90)]           #Both are inclusive
print(df3)













#Name of the students with lowest marks

name1 = df1[df1["Marks"] == df1["Marks"].min()]["Name"]
print(name1)













#Top 5 students by their marks

top5 = df1.sort_values(by="Marks", ascending=False)
print(top5.head())

        #Alternative
topp = df1.nlargest(5, "Marks")
print(topp)








#Find Average Marks

mark1 = df1.Marks.mean()
print(mark1)







#Apply method
df1["Half_marks"] = df1["Marks"].apply(lambda x : x/2)
print(df1.Half_marks)









#Map Function
df1["Gender_num"] = df1["Gender"].map({"Male": 1, "Female":0})
print(df1.Gender_num)





#Drop a column
df1.drop("Half_marks", axis=1, inplace=True)
print(df1)










#Display name and marks of the female students only
df4 = df1[df1["Gender"] == "Female"][["Name", "Marks"]]
print(df4)

        #Alternative
df5 = df1[df1["Gender"].isin(["Female"])][["Name", "Marks"]]
print(df5)










#Rename the Marks column
df1.rename(columns={"Marks":"Final_marks"})     #By default, -- inplace=True --
print(df1)










#Concat two dataset
df6 = pd.DataFrame({"Name":"Anil", "Marks":85,
                    "Gender":"Male", "Email":"anil@gmail.com"}, index=[0])

df7 = pd.concat([df1, df6], ignore_index=True)
print(df7)




df1["Name_marks"] = df1["Name"] + ", " + df1["Marks"].apply(str)             #Converting the marks column to string using -- apply -- method then addin the two series object with a comma in between
print(df1)










#loc & iloc

df8 = df1.loc[:, "Marks":"Gender"]       #It means all the rows ":" , and "Marks" to "Gender" column
print(df8)                              #When using -- loc -- method, you can pass only the labels not the index, in -- loc -- both the values are inclusive while slicing



df9 = df1.iloc[1, 2]                   #It means the row index 1 and the column index 2
print(df9)                              #While using -- iloc -- method, you can pass only the index not the labels, in -- iloc -- first value is inclusive and the last one is exclusive while slicing












#Find the highest average value as per gender

df10 = df1.groupby("Gender")["Marks"].mean().round(2)   #It will return series
print(df10.to_frame())          #We can use -- to_frame() -- to convert series object to dataframe object


















#What are the top 5 most popular email providers

df1["Email_provider"] = df1["Email"].apply(lambda x : (x.split("@"))[1])
print(df1["Email_provider"])

pop1 = df1["Email_provider"].value_counts()
print(pop1)







