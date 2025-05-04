import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ==================  Scatter Plot in Seaborn  =======

data1 = sns.load_dataset("penguins")            #The --- seaborn.load_dataset() --  method is used to load in built datasets from the seaborn library. For the purpose of describing seaborn or creating reproducible examples for bug complaints, this function offers rapid access to a few example datasets. It is not required for everyday use.
print(data1, type(data1))           #panda dataframe object type
print(data1.island)


#Creating a Scatter Plot
sns.scatterplot(x="bill_length_mm",
                y="bill_depth_mm",
                data=data1)      #With the named parameter -- x -- and -- y -- we can pass the column name of the dataframe_object of which column you want to show at which axis, if you don't pass these parameters, all the columns will be treated as dependent variable
                                #With the name parameter -- data -- we can pass the dataset on which it is gonna create a graph, N.B: datasets must in Pands dataframe_object or series_object, it doesn't take list_object

plt.show()








#Plotting Scatter plot with parameters
sizes1 = [10, 30]
marker1 = {"Male":"*", "Female":"o"}
sns.scatterplot(x=data1.bill_length_mm, y=data1.bill_depth_mm, hue=data1.sex, style=data1.sex, size=data1.sex, sizes=sizes1, palette="Accent", alpha=0.8)   #The difference is on the above statement we passed dataframe_object in the data parameter, so in x and y parameter we just to had pass the name of the column on which we wanna perform plotting, in here we directly passed the series_object to the x and y parameter which contains all the values 
                                                #With named parameter -- hue -- we can visualize the data of different categories in one plot , it takes column name of the dataset as value
                                                #With named parameter -- style -- you can change the style of the dot for each of the different kinds of value that particular data column contains, it takes colum name of the data set as value
                                                #With named parameter -- size -- you can change the size(by default) of the dot for each of the different kinds of value that particular data column contains, it takes colum name of the data set as value
                                                #With named parameter -- sizes -- you can pass desired size of the dot(scatter) according to the passed value, it takes list/tuple as value
                                                #With named parameter -- palette -- we can change the color combination of the plot according to the color_palette value is passed into it, to get all the color palette pass any string, with raising an error it will show the available color palette
                                                #With named parameter -- alpha -- we can set the grapgh transperency level, it takes value between 0 to 1
                                                #With named parameter -- markers -- we can put markers(the shape is defined by us) of the dots(scatters), for each individual line in the graph we have to pass that many elements as a list/ or a dictionary with key is the category_value and dict_value is the category_value marker shape, each element represent the shape of the marker
                                                #With named parameter --
                                                #With named parameter --
                                                #With named parameter --






plt.show()
