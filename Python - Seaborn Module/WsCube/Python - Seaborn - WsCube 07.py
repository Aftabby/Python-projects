import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ==================  Violin plot in Seaborn  =======

data1 = sns.load_dataset("tips")            #The --- seaborn.load_dataset() --  method is used to load in built datasets from the seaborn library. For the purpose of describing seaborn or creating reproducible examples for bug complaints, this function offers rapid access to a few example datasets. It is not required for everyday use.
print(data1, type(data1))           #panda dataframe object type
print(data1.total_bill)



#Creating a Violin plot
sns.violinplot(x="day", y="total_bill", data=data1) #You can also pass only x or y parameter, to see single violin plot

plt.show()






#Plotting violin plot with parameters
order1 = ["Sat", "Sun", "Fri", "Thur"]
sns.violinplot(x="day", y="total_bill", data=data1, hue="time", linewidth=2, palette="Accent", order=order1, saturation=0.8, split=True, scale="count", inner="quart" )
                                                #With named parameter -- hue -- we can visualize the data of different categories in one plot , it takes column name of the dataset as value
                                                #With named parameter -- linewidth -- we can change the edge line thickness of each of the violin plot
                                                #With named parameter -- palette -- we can change the color combination of the plot according to the color_palette value is passed into it, to get all the color palette pass any string, with raising an error it will show the available color palette
                                                #With named parameter -- order -- we can change the order of the x-axis, it takes a list of each unique value of the x-axis column order-wise
                                                #With named parameter -- saturation -- we can change the saturation of the color of the bars(value 0 to 1)
                                                #With named parameter -- color -- we can change the color of the graph
                                                #With named parameter -- split -- we can see the different category data held together for each of the unique value of x-axis, it is then easy to compare, by default it is False
                                                #With named parameter -- scale -- we can change the scaling on which it make the graph, it takes three values - "count", "area", "width" -
                                                #To make the graph horizontal, swap the column name of x-axis and y-axis in the parameter
                                                #With named parameter -- inner -- we can view different types of distribution type inside the violin, by default it show box & whisker, by passing - "quart" - we can see the quarter view, the value it takes are - "box", "quartile", "point", "point", None - 
                                                #With named parameter -- 
                                                #With named parameter --
                                                #With named parameter -- 
                                                #With named parameter --








plt.show()