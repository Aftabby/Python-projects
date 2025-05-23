from matplotlib import pyplot as plt
import numpy as np
import random


# ================== How to Plot Histogram Chart in Matplotlib? ============


array1 = np.random.randint(10, 60, (50))        # -- randint(low, high, size) -- Because we need lots of numbers for histogram plot
print(array1)

bins = [5, 10, 15, 20, 25, 26, 27, 30, 35,  40,45, 50, 60]

plt.title("HISTOGRAM GRAPH TITLE")
plt.xlabel("THIS IS X LABEL")
plt.ylabel("THIS IS Y LABEL")

plt.hist(array1, color="g", edgecolor="y", bins=bins)       #With named parameter -- bins -- you can range the data bins/basked of x-axis according to the passed values
plt.show()






#With custom range of x-axis,, with unnamed range parameter


plt.hist(array1, "auto", (0, 200), color="g", edgecolor="y" )     # -- plt.hist(value_array/list, interval/bins_system, (range_start, range_end)) -- third unnamed parameter is a tuple,, second and third unnamed parameter is not mandatory
plt.show()








#Changing the lowest starting point of y-axis in the graph, with named parameter -bottom-


plt.hist(array1, bottom=20, color="g", edgecolor="y", align="left" )    #with named parameter -- align -- you can align the x-axis value with respect to their bar range
plt.show()                                                              #With named parameter --bottom -- you can set the minimum value of y-axis scale









#COnverting histogram to step type graph, and also other histogram type
plt.hist(array1, bottom=20, color="g", edgecolor="y", histtype="step" )     # with named parameter --histype- you can change the type of histogram to different types,, the values are -- bar, barstacked, step, stepfilled --
plt.show()






#Plotting histogram graph horizontally
plt.hist(array1, bottom=20, color="g", edgecolor="y", orientation="horizontal" )    # By default, -- orientation="vertical" --
plt.show()







#Change the width of each of the bar in histogram
plt.hist(array1, bottom=20, color="g", edgecolor="y", rwidth=0.8 )      # -- rwidth=0<int<1  -- 
plt.show()









#Tranforming the y-axis in a log scale
plt.hist(array1, bottom=20, color="g", edgecolor="y", log=True )
plt.show()







#Showing the label in the graph

plt.legend()     #When you pass the label parameter in -- plt.hist() -- method, you gotta call the -- plt.legend() -- method,, you can also pass the label parameter in this method instead of -- plt.bar() -- method

plt.show()






#Showing a vertical line at any point of x-axis

plt.hist(array1, edgecolor="g")

plt.axvline(45, color="r", label="Median")      #A vertical line by -- plt.axvline(value_of_x_axis) --- ,, to activate the label paramter, you have to call the method -- plt.legend() --
plt.legend()

plt.show()









#Showing grid on the graph
plt.hist(array1, edgecolor="g")
plt.grid()          # -- plt.grid() -- method activates the grid view of the graph

plt.show()









