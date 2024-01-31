import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ==================  Histogram Plot in Seaborn  =======

data1 = sns.load_dataset("penguins")            #The --- seaborn.load_dataset() --  method is used to load in built datasets from the seaborn library. For the purpose of describing seaborn or creating reproducible examples for bug complaints, this function offers rapid access to a few example datasets. It is not required for everyday use.
print(data1, type(data1))           #panda dataframe object type
print(data1.island)



#Creating a histogram plot

sns.displot(data1["bill_length_mm"])    #To create a basic histogram pass the dataset(1D/single_column) to the method -- distplot() -- method
plt.show()









#Plotting histogram with parameters
bin1 = [170, 200, 230, 260]
sns.displot(data1["flipper_length_mm"], bins=bin1, kde=True, rug=True, color="green", log_scale=True)
                                                #With named parameter -- bins -- you can change the range/bins/basket of data to a fixed interval in x-axis in histogram plot
                                                #With named parameter -- kde -- which stands for kernel density estimation, if True we can view a density graph over the histogram plot, by default it is False
                                                #With named parameter -- rug -- , if True, we can visualize the data distribution(density) with scaling on x-axis, by default it is False
                                                #With named parameter -- color -- we can change the color of the bars, it takes list of values for individual bar, or a single value for all the bars
                                                #With named parameter -- log_scale -- we can change to scaling of x-axis to log scaling, by default it is False
 




plt.show()

