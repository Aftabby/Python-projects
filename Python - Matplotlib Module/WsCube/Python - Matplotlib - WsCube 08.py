from matplotlib import pyplot as plt
import numpy as np

# ==============  Step Plot in Matplotlib Python  ============

x1 = [1, 3, 5, 7, 9]
y1 = [3, 4, 5, 6, 5]
label1 = "THIS IS LABEL"



plt.step(x1, y1)    #Step plot takes at least two paramter one is the value of x-axis and another is the y-axis (in the graph the value of the y-axis depends upon the same index_positioned x-axis value that is passed to the parameter ), (It is recommeded to always keep the x-axis value in an ascending order)

plt.grid()          #To show a grid on the graph
plt.show()




#Step plot with parameters
plt.step(x1, y1, color="g", marker="o", ms=10, mfc="y", label=label1)
                                        #With named parameter -- color -- we can change the color of the line
                                        #With named parameter -- marker -- you can show the values marker within the graph, with the value -- "o" -- we want tha marker shape to be circle
                                        #With named parameter -- ms -- we can change the marker size (ms stands for marker size)
                                        #With named parameter -- mfc -- we can change the marker face color (i.e the inner color)
                                        #With named parameter -- label -- we can put a label on the graph







plt.legend()

plt.show()