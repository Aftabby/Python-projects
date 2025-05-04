import matplotlib.pyplot as plt
import numpy as np


#============  HOW TO CREATE A SCATTER PLOT  ==============



#Creating a scatter plot

day = [1, 2, 3, 4, 18, 6, 7]       # X-Axis
num = [2, 3, 1, 4, 5, 3, 6]       # The values in the graph

colors = ["r", "y", "g", "b", "r", "m", "w"]
sizes = [100, 2, 4, 500, 2, 10, 7]

plt.title("Title of Scatter Plot", fontsize=20) #Title of the graph, and a named parameter -- fontsize ---
plt.xlabel("Day", fontsize=15)                   #Labeling x-axis
plt.ylabel("Number of Hours Slept", fontsize=15) #Labeling y-axis


plt.scatter(day, num, color=colors, sizes=sizes, alpha=0.7, marker="*", edgecolor="g", linewidth=4)   # -- plt.scatter(x, y) -- Maintaining order for each value of the index_postion of x, the value of the same index_position of y will be the scattered value in the graph,, both the passed list/array(x,y) should match the shape, and only numerical value is allowed
                                                    #With named parameter -- color=list -- or  -- color=initial_character_of_color_name -- you can customize the color of each of the scattered dot with a list(each element represent a dot respectively, and each color is represented by the string of the first character of the color names or you can also pass color code), or a constant color for all the scattered dots with only one value,, this parameter has two name one is -- color -- another is --  c -- c is use for number sequence of color codes
                                                    #With named parameter -- sizes=list -- or  -- size=integer_value -- you can customize the size of each of the scattered dot with a list(each element represent a dot respectively), or a constant size for all the scattered dots with only one value,, this parameter has two name one is -- sizes -- another is --  s --
                                                    ##With named parameter -- alpha=0<int<1 -- you can blur the whole graph, that is the less the integer value the less the opacity
                                                    #With named parameter -- marker="*" -- you can change the marker of the scarred plot, which is by default a circle/dot
                                                    #With named parameter -- edgecolor=list -- or  -- edgecolor=initial_character_of_color_name -- you can customize the edge/ border color of each of the marker with a list(each element represent a marker(dot) respectively, and each color is represented by the string of the first character of the color names or you can also pass color code), or a constant color for all the markers(dot) with only one value
                                                    #With named parameter -- linewidth=list -- or  -- linewidth=int -- you can customize the edge/border width of each of the marker with a list(each element represent a marker respectively), or a constant edege/border width for all the markerss with only one value




plt.show()                  #Class level method ,, This -- plt.show() -- method shows the visualization of the plotting/graph/distribution 






#Playing with colors
colors =  [10, 49, 30, 29, 56, 20, 33]

plt.scatter(day, num, c=colors, sizes=sizes)        #We are showing color with numbers, there are a lot of color map which you can also use
plt.show()



plt.scatter(day, num, c=colors, sizes=sizes, cmap="viridis") # with -- cmap -- parameter you can use the intensity of different type of maps, to know all the cmap value google it
plt.colorbar()          #If you want to see the color intensity bar of the current cmap

plt.show()


    #Labeling the color bar
plt.scatter(day, num, c=colors, sizes=sizes, cmap="twilight")

color_bar = plt.colorbar()
color_bar.set_label("Color Bar Intesity", fontsize=15)

plt.show()











#Plotting multiple scatter graph together

day = [1, 2, 3, 4, 18, 6, 7]       # X-Axis
num = [2, 3, 1, 4, 5, 3, 6]       # The values in the graph
num2 = [5, 9, 1, 3, 6, 4, 3]       # Another value

color1 = "r"
color2 = "g"
sizes = [100, 2, 4, 500, 2, 10, 7]

plt.title("Title of Scatter Plot", fontsize=20) #Title of the graph, and a named parameter -- fontsize ---
plt.xlabel("Day", fontsize=15)                   #Labeling x-axis
plt.ylabel("Number of Hours Slept", fontsize=15) #Labeling y-axis

plt.scatter(day, num, color=color1, s=sizes, label="Week 1")
plt.scatter(day, num2, color=color2, s=sizes, label="Week 2")

plt.legend()

plt.show()
