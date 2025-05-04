import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ==================  Strip plot in Seaborn  =======
                                                #Strip plot is like a scatter plot that differentiates different categories, it is considered a good alternative to a box or violin plot

data1 = sns.load_dataset("tips")            #The --- seaborn.load_dataset() --  method is used to load in built datasets from the seaborn library. For the purpose of describing seaborn or creating reproducible examples for bug complaints, this function offers rapid access to a few example datasets. It is not required for everyday use.
print(data1, type(data1))           #panda dataframe object type
print(data1.total_bill)





'''

#Creating a Strip Plot
sns.stripplot(x="day", y="total_bill", data=data1)   #You can also make strip plot with only a column/series_object (pass it to -- x -- or -- y -- parameter)


plt.show
'''





#Plotting Strip Plot with paramter
sns.stripplot(x="day", y="total_bill", data=data1, hue="sex", palette="cubehelix", linewidth=1, edgecolor="red", jitter=1.5, size=4, marker="<", alpha=0.8 )
                                                #With named parameter -- hue -- we can visualize the data of different categories in each plot , it takes column name of the dataset as value
                                                #With named parameter -- palette -- we can change the color combination of the plot according to the color_palette value is passed into it, to get all the color palette pass any string, with raising an error it will show the available color palette
                                                #With named parameter -- linewidth -- we can change the edge width of the dots/markers, by default it is 0, to change the width individually for each column use -- linewidths -- and pass a list for all the column's marker edge width as element
                                                #With named parameter -- egdecolor -- we can change the edge color of the dots/markers
                                                #With named parameter -- jitter -- we can change the horizontal distance ratio between each of the dots(Which is not recommended except special cases)
                                                #With named parameter -- size -- we can change the size of the dots/markers
                                                #With named parameter -- marker -- we can change the shape of the dot/marker, it takes a value, dictionary(with hue column unique values as key and shape as value) or list 
                                                #With named parameter -- alpha -- we can set the grapgh transperency level, it takes value between 0 to 1
                                                #With named parameter -- 
                                                #With named parameter -- 
                                                #With named parameter -- 
                                                #With named parameter --


plt.show()