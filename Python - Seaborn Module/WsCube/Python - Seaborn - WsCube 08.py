import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ==================  Pair plot in Seaborn  =======
                                                #IT is not any type of plot, it is used to show multiplot plotting(or you can use a dataframe with multiple numeric columns) in the same window within multiple sub-window, it is used to compare graph mainly

data1 = sns.load_dataset("tips")            #The --- seaborn.load_dataset() --  method is used to load in built datasets from the seaborn library. For the purpose of describing seaborn or creating reproducible examples for bug complaints, this function offers rapid access to a few example datasets. It is not required for everyday use.
print(data1, type(data1))           #panda dataframe object type
print(data1.total_bill)





'''
#Creating a pair plot
sns.pairplot(data1) #Here we passed a dataframe_object with multiple numeric columns, where each numeric column will be grapghed with each of the numeric column(like permutation)
plt.show()

'''





#Plotting pair plot with parameters
vars1 = ["total_bill", "tip"]
hue_order1 = ["Female", "Male"]
marker1 = ["*", "<"]

sns.pairplot(data=data1, vars=vars1, hue="sex", hue_order=hue_order1, palette="brg", kind="reg", diag_kind="hist", markers=marker1)
                                                #With named parameter -- hue -- we can visualize the data of different categories in each plot , it takes column name of the dataset as value
                                                #With named parameter -- vars -- we can select the specific columns rather than all the numeric columns to show in the pair plot, it takes the column_names as element in a list as value
                                                #With named parameter -- hue_order -- we can order the position of the value in the column passed in -- hue -- in the pair plot, it takes list, the unique values of the hue column is passed as element maintaining your desired order
                                                #With named parameter -- palette -- we can change the color combination of the plot according to the color_palette value is passed into it, to get all the color palette pass any string, with raising an error it will show the available color palette
                                                #With named parameter -- x_vars - you can specify which columns you wanna see in the x-axis, for that you have to remove --vars-- parameter, it takes list as the column_names as element
                                                #With named parameter -- y_vars - you can specify which columns you wanna see in the y-axis, for that you have to remove --vars-- parameter, it takes list as the column_names as element
                                                #With named parameter -- kind -- we can change the type of grapgh plotting, it takes these values -- "scatter", "kde", "hist", "reg" --
                                                #With named parameter -- diag_kind -- we can change the type of graph plotting diagonally(i.e same_column vs same_column), it takes these values -- "kde", "auto", "hist" --
                                                #With named parameter -- markers -- we can change the marker style of the graph, it takes list of marker pre defined shape as element, the element number must match with the number of unique value of --hue-- column
                                                #With named parameter -- 
                                                #With named parameter -- 
                                                #With named parameter --



plt.show()


