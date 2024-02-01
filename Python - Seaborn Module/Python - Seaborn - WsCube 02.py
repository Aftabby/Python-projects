import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ==================  Bar Plot in Seaborn  =======

data1 = sns.load_dataset("penguins")            #The --- seaborn.load_dataset() --  method is used to load in built datasets from the seaborn library. For the purpose of describing seaborn or creating reproducible examples for bug complaints, this function offers rapid access to a few example datasets. It is not required for everyday use.
print(data1, type(data1))
print(data1.island)



#Plotting bar plot in seaborn
    #Below two lines works the same
sns.barplot(x=data1.island, y=data1.bill_length_mm)        #With the named parameter -- x -- and -- y -- we can pass the column_name/dataset(single) of the dataframe_object of which column you want to show at which axis(here by data1.column_name , we are passing the column(series_object) as we didn't pass the parameter data=dataframe_object here)
#sns.lineplot(x="island", y="bill_length_mm", data=data1)   


plt.show()









#Plotting bar with parameters
order1 = ["Dream", "Torgersen", "Biscoe"]
order2 = ["Female", "Male"]

    #Below two lines works almost the same
#plt.grid()
sns.set(style="darkgrid")       #We can set different parameter by -- sns.set() -- method, by -- style="darkgrid" -- we are using a style of the graph where the values are pre-defined by the original developers, N.B: this method always should be called before plotting the graph

sns.barplot(x="island", y="bill_length_mm", data=data1, hue="sex", order=order1, hue_order=order2, orient="v", color="g", palette="Accent", saturation=0.8, capsize=0.5, dodge=True, alpha=0.8 )
                                                                #With named parameter -- hue -- we can visualize the data of different categories in one plot , it takes column name of the dataset as value
                                                                #With named parameter -- order -- we can order the bars in a seaborn countplot/barplot based on sequence column_names/column_index defined in a list as each element, and pass the list in it
                                                                #With named parameter -- hue_order -- we can order the grouped bar of the different categories shown by -- hue -- parameter
                                                                #With named parameter -- orient -- we can orient the grapgh horizontally or vertically, by default it is -- orient="v" -- which means vertical, to make it horizontal pass -- orient="h" -- N.B: In horizontal graph both x and y axis should countain numeric value(i.e no categorical values)
                                                                #With named parameter -- color -- we can change the color of the graph, either you can pass one value for all the bars, or a list of values for each bar,, the value can be the first letter of the color or the full color name in string
                                                                #With named parameter -- palette -- we can change the color combination of the plot according to the color_palette value is passed into it, to get all the color palette pass any string, with raising an error it will show the available color palette
                                                                #With named parameter -- saturation -- we can change the saturation of the color of the bars (value 0 to 1)
                                                                #With named parameter -- errcolor -- and -- errwidth -- and -- capsize -- we can change the color and width of the err marks on the bar (the vertical mark that is in top-mid on each of the bar), it is also known as - ci(confidence interval) - ,,, with capsize we can create a cap showing the min and max of the ci(confidence interval)
                                                                #With named parameter -- dodge -- we can super-impose(overlap on one another) the grouped bar together, by default it is True (i.e not super-imposed)
                                                                #With named parameter -- alpha -- we can set the grapgh transperency level
        






plt.show()













