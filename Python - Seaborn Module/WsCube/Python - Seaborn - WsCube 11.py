import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ==================  Cat Plot in Seaborn  =======
                                                #Cat Plot can show different types of grapgh with its -- kind -- parameter, it is an well known parameter for cat plot

data1 = sns.load_dataset("tips")            #The --- seaborn.load_dataset() --  method is used to load in built datasets from the seaborn library. For the purpose of describing seaborn or creating reproducible examples for bug complaints, this function offers rapid access to a few example datasets. It is not required for everyday use.
print(data1, type(data1))           #panda dataframe object type
print(data1.total_bill)




'''
#Creating a Cat Plot
sns.catplot(x="tip", y="size", data=data1.head(20))

plt.show()
'''







#Plotting Catplot with parameters

sns.catplot(x="tip", y="size", data=data1.head(20), hue="sex", palette="ocean_r", height=4, kind="bar")
                                                #With named parameter -- hue -- we can visualize the data of different categories in each plot , it takes column name of the dataset as value
                                                #With named parameter --  palette -- we can change the color combination of the plot according to the color_palette value is passed into it, to get all the color palette pass any string, with raising an error it will show the available color palette
                                                #With named parameter -- height -- we can change the height of the graph
                                                #With named parameter -- kind -- we can change the type of grapgh, it is an well know parameter of cat plot, the values are -- "bar", "box" "boxen", "count", "point", "strip", "swarm", "violin" --



plt.show()






