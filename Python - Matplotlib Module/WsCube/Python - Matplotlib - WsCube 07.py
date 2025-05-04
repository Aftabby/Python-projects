import matplotlib.pyplot as plt
import numpy as np

# ===============  Area vs Stack Plot  ==============
                                        #When we plot multiple area plot to the same graph we call it stack plot


x1 = [1, 3, 5, 7, 9]
y1 = [4, 5, 3, 1, 2]

plt.stackplot(x1, y1)       #Stack plot takes at least two paramter one is the value of x-axis and another is the y-axis (in the graph the value of the y-axis depends upon the same index_positioned x-axis value that is passed to the parameter ), (It is recommeded to always keep the x-axis value in an ascending order)

plt.show()











#Plotting multiple area plot together to a stackplot
y2 = [3, 4, 1, 2, 5]
y3 = [2, 3, 1, 5, 2]

plt.stackplot(x1, y1, y2, y3)       #Here for a single x-axis value, we can plot multiple area graph, but the value of y3 adds up to the value of y2 and y1(according to index), so that while overlapping the graph you can still visualize all the graph,, same way y2 adds up to the value of y1 (according to index)
plt.show()












#Applying multiple parameter to the stack plot

label1 = ["Area1-y1", "Area2-y2", "Area3-y3"]
colors1 = ["r", "g", "b"]

plt.stackplot(x1, y1, y2, y3, labels=label1, colors=colors1, baseline="zero")
                                                        #With named parameter -- labels -- we can label each area in the graph according to its color, it takes a list as value
                                                        #With named parameter -- colors -- we can customize the color of the area graph, it takes a list as a value 
                                                        #With named parameter -- baseline -- we can change the baseline pov ,, by default -- baseline="zero" -- , with value -- "sym" -- you can get almost a symetry of the values on x-axis, with value -- "wiggle" -- you will get another baseline pov




plt.title("THIS IS STACK GRAPH")
plt.xlabel("THIS IS X-AXIS")
plt.ylabel("THIS IS Y-AXIS")

plt.legend(loc=2)        #With method -- plt.method -- you can show the labels that's been passed to the -- stackplot -- method,, and with parameter -- loc -- we can change the location of the labels in the graph, 

plt.show()

