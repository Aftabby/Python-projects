import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ==================  Line Plot in Seaborn  =======
                                                #Seaborn is built on matplotlib library so there would be circumstances where we need to use both


#Creating Line Plot
x1 = [1, 2, 3, 4, 5, 6, 7]
y1 = [2, 3, 4, 1, 5, 3, 7]

df1 = pd.DataFrame({"x1" : x1, "y1" : y1})


sns.lineplot(x="x1", y="y1", data=df1)        #With the named parameter -- x -- and -- y -- we can pass the column name of the dataframe_object of which column you want to show at which axis, if you don't pass these parameters, all the columns will be treated as dependent variable
                                                        #With the name parameter -- data -- we can pass the dataset on which it is gonna create a graph, N.B: datasets must in Pands dataframe_object or series_object, it doesn't take list_object
                                                        
plt.show()                                      #As seaborn doesn't have any method to show the graph it created, we use -- plt.show() -- to view the data












#Line plotting using list_object
sns.lineplot(x=x1, y=y1)                #With named parameter -- x -- and -- y -- we can pass the value axis wise, it allows list_objects
plt.show()






#Creating graph with online datasets
data1 = sns.load_dataset("penguins")            #The --- seaborn.load_dataset() --  method is used to load in built datasets from the seaborn library. For the purpose of describing seaborn or creating reproducible examples for bug complaints, this function offers rapid access to a few example datasets. It is not required for everyday use.
print(data1, type(data1))

sns.lineplot(x="bill_length_mm", y="flipper_length_mm", data=data1)     #We passed the column name of the dataset to the parameter -- x -- and -- y --
plt.show()









#Plotting line with parameters
marker1 = ["o", ">"]
sns.lineplot(x="bill_length_mm", y="flipper_length_mm", data=data1, hue="sex", size=0.2, style="sex", palette="Accent", markers=marker1, dashes=False, legend=False)  
                                                                #With named parameter -- hue -- we can visualize the data of different categories in one plot , it takes column name of the dataset as value
                                                                #With named parameter -- size -- you can make an estimation of sized between two tickers of axises (Google)
                                                                #With named parameter -- style -- you can change the style of the line for each of the different kinds of value that particular data column contains, it takes colum name of the data set as value
                                                                #With named parameter -- palette -- we can change the color combination of the plot according to the color_palette value is passed into it, to get all the color palette pass any string, with raising an error it will show the available color palette
                                                                #With named parameter -- markers -- we can put markers(the shape is defined by us) on the sharp edges of the line graph, for each individual line in the graph we have to pass that many elements as a list, each element represent the shape of the marker
                                                                #With named parameter -- dashes -- we can signify if we want any dashed line in the graph or not, by default it is True, if False all the dashed line will be converted to the normal line
                                                                #With named parameter -- legend -- we can signify if we want any extra color matched label on the graph or not, by default it is -- auto --, if False the label will be removed. We can also pass some pre-defined value of legend, to know the values pass a random string. (In matplotlib, we use legend method to view the label)
                                                                #With named



plt.title("TITLE")              #We can also apply the matplotlib method on a graph plotted with seaborn
plt.grid()
plt.show()


