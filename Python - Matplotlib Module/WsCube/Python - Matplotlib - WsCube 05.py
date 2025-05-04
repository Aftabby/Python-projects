import matplotlib.pyplot as plt
import numpy as np


# ==========  STEMS Plot with Matplotlib  ==========


x1 = [1, 2, 3, 4, 5]
y1=  [-3, 4, 5, -1, 6]
label1 = "THIS IS LABEL"

plt.stem(x1, y1, linefmt="--", markerfmt="r+", bottom=2, basefmt="g", label=label1,)      #with named parameter -- linefmt -- we can change the line style of stem plot (by default the value is "-" : solid line)("--" : Dashed line,, "-." : Dash-dot line, ":" : Dotted line)
                                                              #with named parameter -- markerfmt -- we can change both the marker style and color of the marker
                                                              #with named parameter -- bottom -- we can shift the x-axis vertically based on its numerical value 
                                                              #with named parameter -- basefmt -- we can pass various color code and change the color of x-axis
                                                              #with named parameter -- use_line_collection -- passing False as value (by default, it's True), there will be multiple color of each of the line


plt.legend()    #with -- legend() -- method, we can activate the label that was passed to plt.stem (or any kind of graph)
plt.show()










#Plotting the stem plot horizontally
plt.stem(x1, y1, orientation="horizontal")

plt.show()


