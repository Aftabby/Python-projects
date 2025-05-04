import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ==================  Heatmap Plot in Seaborn  =======

data1 = sns.load_dataset("anagrams")            #The --- seaborn.load_dataset() --  method is used to load in built datasets from the seaborn library. For the purpose of describing seaborn or creating reproducible examples for bug complaints, this function offers rapid access to a few example datasets. It is not required for everyday use.
print(data1, type(data1))           #panda dataframe object type
print(data1.num3)

data1.drop(columns="attnr", axis=1, inplace=True)      #As categorical data can't be shown in heat map, to drop multiple columns pass a list with column names to the parameter -- columns --
print(data1)

arr1 = np.linspace(1, 10, 20).reshape(4, 5) #Creating an array with 20 elements from 1-10 with fixed interval, then reshaping it to 4 rows, 5 columns
print(arr1)




sns.heatmap(arr1)       #Here The data will be shown according to the number and color of the right side bar, the shape will be same as the shape of array
plt.show()                  #Heatmap with an 2D-Array


sns.heatmap(data1.head(10))     #Heatmap with dataframe_object (first 10 values), each value will represen a color in the heatmap, and the relation of color and number will be given at the right side bar
plt.show()












#Plotting heatmap with parameters
annot_kws1 = {"fontsize" : 15, "color" : "red"}
xlabel1 = "THIS IS X AXIS"
ylabel1 = "THIS IS Y AXIS"

heatmap1 = sns.heatmap(data1.head(10), vmin=0, vmax=12, cmap="ocean", annot=True, annot_kws=annot_kws1, linewidth=4, linecolor="yellow", cbar=False, xticklabels=False, yticklabels=False )
                                                #With named parameter -- vmin -- and -- vmax -- we change the color-number relation bar range (at the right side of the graph)
                                                #With named parameter -- cmap -- we can change the color combination of the plot according to the color_palette(or color map) value is passed into it, to get all the color map/palette pass any string, with raising an error it will show the available color map/palette values
                                                #With named parameter -- annot -- we can show the value of each of the box, inside the box along with color in the heatmap, by default it is False,, we can also pass our individual custom value to show on each of the box, for that pass the same shaped array with the custom values (remember to also pass the -- fmt="s" -- parameter also, which means format is string) 
                                                #With named parameter -- annot_kws -- we can change the property of annotation of the heat map, it takes a dictionary, where each of the key is property_name and the value is the property_value 
                                                #With named parameter -- linewidth -- we can change the width between the boxes, by default it is 0, to change the width individually for each box use -- linewidths -- and pass a list for all the boxes width as element
                                                #With named parameter -- linecolor -- we can change the color of width between the boxes of the heatmap
                                                #With named parameter -- cbar -- we can remove the color bar from the graph, by default it is False
                                                #With named parameter -- xticklabels -- and -- yticklabels -- we can remove the box index number from the x and y axis respectively, by default it is True
                                                #With named parameter -- 
                                                #With named parameter --


print(type(heatmap1))
heatmap1.set(xlabel=xlabel1, ylabel=ylabel1)    # By using -- set -- method on seaborn/matplotlib_object we can set property to the graph (just like plt.xlabel() from matplotlib)
                                                #There is an alternative also, we can use -- sns.set() -- before creating any graph(or may be after also), but I think that will apply to all the object created by seaborn/matplotlib_class in that file
sns.set(font_scale=15)  #Doesn't work(may be we should use it before creating a graph usin sns class)



plt.show()


