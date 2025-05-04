import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ==================  Styling Plot in Seaborn  =======
                                                #It not a plot type, rather how we can style our plot 

data1 = sns.load_dataset("tips")            #The --- seaborn.load_dataset() --  method is used to load in built datasets from the seaborn library. For the purpose of describing seaborn or creating reproducible examples for bug complaints, this function offers rapid access to a few example datasets. It is not required for everyday use.
print(data1, type(data1))           #panda dataframe object type
print(data1.total_bill)




#Seaborn Figure Style

#Below two lines work the same way
#sns.set_style("dark")
sns.set(style="dark")       #With -- sns.set() -- we can set certain property to the graph, here with parameter -- style -- we can set different background of the graph
                            # This method must be called or set to the graph before creating the graph (not sure about it)
sns.set_context("poster", font_scale=0.8)


sns.barplot(x=data1.day, y=data1.total_bill)
#plt.grid()                                 #We can do the same thing and many more using -- sns.set()
plt.show()










#Removing Axes Spines

sns.barplot(x=data1.day, y=data1.total_bill)

sns.despine()       #It removes the top and right border of the graph figure

plt.show()









#Scale and Contest

plt.figure(figsize=(12, 3))                #IT is a function matplotlib.pyplot, the parameter -- figsize=(vertical_size, horizontal_size) -- take two element in a tuple

sns.barplot(x=data1.day, y=data1.total_bill)


plt.show()

