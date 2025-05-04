import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ==================  Box & Whisker Plot in Seaborn  =======
                                                

data1 = sns.load_dataset("tips")            #The --- seaborn.load_dataset() --  method is used to load in built datasets from the seaborn library. For the purpose of describing seaborn or creating reproducible examples for bug complaints, this function offers rapid access to a few example datasets. It is not required for everyday use.
print(data1, type(data1))           #panda dataframe object type
print(data1.total_bill)





'''

#Creating Box Plot
sns.set(style="whitegrid")      #A way of setting the style of the graph, (may be)you have to set it before creating the plotting

sns.boxplot(x="day", y="total_bill", data=data1)    #We can also make the graph with one column only -- x -- or --y --

plt.show()

'''





#Plotting Box Plot with parameters
order1 = ["Sat", "Sun", "Thur", "Fri"]
meanprops1 = {"marker": "+", "markeredgecolor":"white"}

sns.boxplot(x="day", y="total_bill", data=data1, hue="time", color="red", order=order1, showmeans=True, meanprops=meanprops1, linewidth=3, palette="afmhot", orient="v")
                                                #With named parameter -- hue -- we can visualize the data of different categories in each plot , it takes column name of the dataset as value
                                                #With named parameter -- color -- you can change the color of the box in the box plot
                                                #With named parameter -- order -- you can order view of the x-axis as per column unique values passed in element by order as a list
                                                #With named parameter -- showmeans -- we can indicate the arithmatic mean in the box plot, with a triangular shape.
                                                #With named parameter -- meanprops -- we can change the property basically style of the mean indicator
                                                #With named parameter -- linewidth -- we can change the width of the box and whisker
                                                #With named parameter -- palette -- we can change the color combination of the plot according to the color_palette value is passed into it, to get all the color palette pass any string, with raising an error it will show the available color palette
                                                #With named parameter -- orient -- we can make the graph horizontal (value -- "h" -- ), for horizontal the x-axis must work with numerical value column, by default it is vertical (value is -- "v" --)
                                                #With named parameter -- 
                                                #With named parameter -- 
                                                #With named parameter -- 
                                                #With named parameter --

plt.show()










