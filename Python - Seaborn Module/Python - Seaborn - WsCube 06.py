import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ==================  Count Plot in Seaborn  =======

data1 = sns.load_dataset("tips")            #The --- seaborn.load_dataset() --  method is used to load in built datasets from the seaborn library. For the purpose of describing seaborn or creating reproducible examples for bug complaints, this function offers rapid access to a few example datasets. It is not required for everyday use.
print(data1, type(data1))           #panda dataframe object type
print(data1.tip)



#Creating a Count Plot
    #Below two lines work the same
sns.countplot(x=data1.sex)  
#sns.countplot(x="sex", data=data1)  



plt.show()







#Plotting Count plot with parameters
sns.countplot(x="sex", data=data1, hue="smoker", palette="crest_r", saturation=0.8) 
                                                #With named parameter -- hue -- we can visualize the data of different categories in one plot , it takes column name of the dataset as value
                                                #To represent the graph vertically pass the column name in -- y -- parameter instead of -- x --
                                                #With named parameter -- palette -- we can change the color combination of the plot according to the color_palette value is passed into it, to get all the color palette pass any string, with raising an error it will show the available color palette
                                                #With named parameter -- saturation -- we can change the saturation of the color of the bars(value 0 to 1)
                                                #With named parameter -- 
                                                #With named parameter --
                                                #With named parameter -- 
                                                #With named parameter --



plt.show()





















