import matplotlib.pyplot as plt         # -- matplotlib -- is a library, where as pyplot is a module of that library. Library is consists of one or more library
import numpy as np


# ============= HOW TO PLOT A LINE CHART/ BAR PLOT ==============


#Bar Plot

list1 = ["A", "B", "C", "D"]              #Creating a list with all the individual
list2 = [10, 20, 5, 15]              #Creating a list with all the value of the individul, maintaining the index order as the individuals

list3 = ["g", "b", "m", "y"]

plt.xlabel("Individuals")          # Name/label of the x-axis ,, with parameter -- fontsize=interger_value -- you can customize font size,,
plt.ylabel("Popularity point")  # Name/label of the y-axis,, with parameter -- fontsize=interger_value -- you can customize font size,,
plt.title("Title of the Bar graph", fontsize = 30)     #Title of the graph/distribution/plot,, with parameter -- fontsize=interger_value -- you can customize font size,,



plt.bar(list1, list2, width=0.2, color=list3, align="edge", edgecolor = "r", linewidth = 10, linestyle = ":", alpha = 0.8)           #Class method, In -- plt.bar() -- method the first parameter is the individuals and the second parameter is the value (maintaining the index order as the individual)
                                                #With named parameter -- width=list -- or  -- width=int -- you can customize the width of each of the bar with a list(each element represent a bar respectively), or a constant width for all the bars with only one value
                                                #With named parameter -- color=list -- or  -- color=initial_character_of_color_name -- you can customize the color of each of the bar with a list(each element represent a bar respectively, and each color is represented by the string of the first character of the color names or you can also pass color code), or a constant color for all the bars with only one value
                                                #With named parameter -- aligned = "edge" -- you can align each of the name of the individual to the edge of their respective bar, by default -- align='center' --
                                                #With named parameter -- edgecolor=list -- or  -- edgecolor=initial_character_of_color_name -- you can customize the edge/ border color of each of the bar with a list(each element represent a bar respectively, and each color is represented by the string of the first character of the color names or or you can also pass color code), or a constant color for all the bars with only one value
                                                #With named parameter -- linewidth=list -- or  -- linewidth=int -- you can customize the edge/border width of each of the bar with a list(each element represent a bar respectively), or a constant edege/border width for all the bars with only one value
                                                #With named parameter -- linestylr=":" -- you can customize the border style of all the bars from solid(by default) to dotted
                                                ##With named parameter -- alpha=0<int<1 -- you can blur the whole graph, that is, the less the integer value the less the opacity


plt.show()                      #Class level method ,, This -- plt.show() -- method shows the visualization of the plotting/graph/distribution ,,





#Lableing on the graph with individual name and its color
plt.bar(list1, list2, color=list3, label=["A", "B", "C", "D"])       #With named parmater -- labeled=list_of_individuals -- we can add an extra label on the graph, with accordance with individual and its respective color
plt.legend()                                            #When you pass the label parameter in -- plt.bar() -- method, you gotta call the -- plt.legend() -- method,, you can also pass the label parameter in this method instead of -- plt.bar() -- method
plt.show()                     #Uncomment it to view






















#Overlapping two or more graphs on top of another (Overlapping on the same line)
x = ["A", "B", "C", "D"]
y1 = [10, 5, 15, 20]
y2 = [15, 15, 5, 10]


plt.bar(x, y1, color="r", label="Popularity1")
plt.bar(x, y2, color="y", label="Popularity2")
plt.legend()                #With -- location -- parameter you can also change the postion of the label in -- plt.legend() -- method

plt.show()             















#Plotting two graphs side by side
x = ["A", "B", "C", "D"]
y1 = [10, 5, 15, 20]
y2 = [15, 15, 5, 10]

width_value = 0.2                                # It is the width of the first bar graph
x1 = np.arange(len(x))         #It will return an array of -- [0 1 2 3]
x2 = [i+width_value for i in x1]    # List Comprehension, It will return the same list as x1 but adding the -- width_value -- with each element, it is the value of x-axis of second graph, as the x-axis is not represented by a text now rather a number,, adding width will show the second graph side to side with the first graph


plt.bar(x1, y1, width=width_value, color="r")         #The x-axis is -- 0,1,2,3 --
plt.bar(x2, y2, width=width_value, color="y")         #But still a problem we can't show the name of the individual in the x-axis, we will do it with the help of -- xticks() -- method
                                                        #Here x1 is an array and x2 is a list
plt.show()                          #Displaying the graph


        #Lets add the individual name in the x-axis

plt.bar(x1, y1, width=width_value, color="r")         #Same as before
plt.bar(x2, y2, width=width_value, color="y")

plt.xticks(x1+width_value, x, rotation = 15)       # -- plt.xtics(a, b) -- a = the values (in list/array) in the x axis where you wanna set the tick mark,, b = the values (in list/array) of what you wanna name the tick marks with(respectively) ,,,, with this method Get or set the current tick locations and labels of the x-axis
plt.show()                          # As x1 is an array you can perform mathematical operation with it (that's why we didn't take x2), also if you want the tick mark to be in exactly center of both the bars, pass the first parameter as -- plt.xticks((x1+width_value)/2, x) --
                                       #The same graph but this time with a name of the individuals in x-axis
                                        # With the named parameter -- rotation=integer_value -- you can tilt the individual name based on the integer value
                                        # Ticks are the markers denoting data points on axes


















#Plotting a horizontal bar graph
x = ["A", "B", "C", "D"]
y1 = [10, 5, 15, 20]
y2 = [15, 15, 5, 10]


plt.barh(x, y1, color="r", label="Popularity1")     #Just use the method -- plt.barh() -- instead of -- plt.bar() --
plt.barh(x, y2, color="y", label="Popularity2")     #You can also plot both horizontal and vertical bar at the same graph, tho it looks horrible
plt.legend()                #With -- location -- parameter you can also change the postion of the label in -- plt.legend() -- method

plt.show()  



