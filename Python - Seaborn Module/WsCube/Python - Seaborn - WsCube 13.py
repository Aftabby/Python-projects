import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ==================  Multiple Plot(FacetGrid) in Seaborn  =======
                                                #Making multiple plot with different categories/unique_values of the same column 

data1 = sns.load_dataset("tips")            #The --- seaborn.load_dataset() --  method is used to load in built datasets from the seaborn library. For the purpose of describing seaborn or creating reproducible examples for bug complaints, this function offers rapid access to a few example datasets. It is not required for everyday use.
print(data1, type(data1))           #panda dataframe object type
print(data1.total_bill)




fg1 = sns.FacetGrid(data1)
fg1.map(plt.scatter, "total_bill", "tip")       # -- FacetGrid_object.map(graph_type, x_axis_column_name, y_axis_column_name) --
plt.show()







fg1 = sns.FacetGrid(data1, col="sex", hue="day", palette="Accent")       # To create a facetgrid_object -- sns.FacetGrid(dataframe_object, col=name_of_the_column_on_which_to_differentiate) ,, with --hue -- you can differentiate on the same graph with color, but with -- col -- you get more graphs based on the unique value 
fg1.map(plt.scatter, "total_bill", "tip", edgecolor="green").add_legend()       # -- FacetGrid_object.map(graph_type, x_axis_column_name, y_axis_column_name) --
plt.show()                                                     # -- add_legend() -- shows the label on the graph matching with colors

