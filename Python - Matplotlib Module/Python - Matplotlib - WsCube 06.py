from matplotlib import pyplot as plt
import numpy as np


#=============  Plot a BOX and WHISKER Plot  ==========

list1 = [10, 20, 30, 40, 150]
list2 = [55, 58, 34, 45, 60]


plt.boxplot(list1)      # -- plt.boxplot() -- shows each of the data set in a box and whisker plot with its least, highest, 1st quantile, median, 3rd quantile and outliers(following 1.5IQR formula, shows with a circle far from whiskers) values in the plot

plt.show()






#Plotting box plot with multipleparameters
plt.boxplot(list1, notch=True, vert=False, widths=0.3, labels=["X1"], patch_artist=True, showmeans=True, whis=10, sym="g+", boxprops={"color":"r"}, capprops=dict(color="g"), whiskerprops=dict(color="m"), flierprops=dict(markeredgecolor="b"))   # With named parameter -- notch -- we can show the box like a notch, by default -- notch=False --
                                                            #With named parameter -- vert -- we can show the box plotting horizantally, by default -- vert=True --
                                                            #With named parameter -- width -- we can change the width of the box (only box)
                                                            #With named parameter -- label -- we can label the x-axis, label parameter always takes a list of values (as we can plot multiple data set in the same box plot graph)
                                                            #With named parameter -- patch_artist -- we can fill the box with color, by default -- patch_artist=False -- 
                                                            #With named parameter -- showmeans -- we can see the mean value of the data set (by a triangle icon in the plotting),, by default -- showmeans=False --
                                                            #With named parameter -- whis -- we can increase the length limit of whisker and thus include the outlier(circle shaped) in the whisker, google for more
                                                            #With named parameter -- sym -- you can change the shape and color of the outlier in the graph, (here it is green and '+' shape),, you can also hide the outlier by passing a blank string to the parameter value
                                                            #With named parameter -- boxprops -- we can change the property of the box, it takes dictionary as a value, with -- color -- as key we provided the edge color of the box
                                                            #With named parameter -- capprops -- we can change the property of the cap (The line indicating max and min value), it takes dictionary as a value, with -- color -- as key we changed the color of the cap
                                                            #With named parameter -- whiskerprops -- we can change the property of the whisker, it takes dictionary as a value, here with -- color -- key we changed the color of whisker
                                                            #With named parameter -- flierprops -- we can change the property of the outlier, it takes dictionary as a value, here with key name -- markeredgecolor -- we changed the edge color of the outlier marker
                                                            #With



plt.show()










#Plotting multiple box plot in the same graph

plt.boxplot([list1, list2], labels=["THIS IS X1", "This IS X2"])         #To plot multiple box plot in the same graph, pass the data sets in a list of lists/arrays,, by default each of the data set will be shown on its serial number(index+1) on the x- axis, to change and label the x-axis we passed the label parameter 
plt.show()
