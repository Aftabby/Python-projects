from matplotlib import pyplot as plt
import numpy as np

# =================  Matplotlib Subplot  ============
                                   #Subplot is not any kind of plotting, rather it is a way to view multiple plot/grapgh together

x1 = [1, 2, 3, 4]
x2 = [10, 20, 30, 40]
x3 = ["a", "b", "c", "d"]
y1 = [1, 2, 4, 3]
y2 = [20, 10, 30, 40]


plt.subplot(1, 3, 1)        #-- subplot -- method is ike a multiwindow of plots, where we can view all the graphs together, to create the window we have to pass the value -- (number_of_row, number_of_colum, position_of_next_graph) as
plt.plot(x1, y1, color="r")
            
plt.subplot(1, 3, 2) 
plt.pie(x2)

plt.subplot(1, 3, 3) 
plt.bar(x3, y2)

plt.show()     #If we see the graph without the -- subplot() -- method, it will be overlapped on one another and will be non-readable




