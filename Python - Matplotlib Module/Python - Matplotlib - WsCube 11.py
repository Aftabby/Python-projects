from matplotlib import pyplot as plt
import numpy as np

# =================  Savefig in Matplotlib  ============
                                                #-- Savefig -- is not a method to plot any kind of graph, rather it is used to save the graph as a figure in the local device

x1 = [1, 2, 3, 4, 5]
y1 = [10, 30, 20, 50, 40]

plt.plot(x1, y1, color="r")

plt.savefig("savefig1")         #The graph will saved as -- savefig1.png  -- in the local machine, at the directory where terminal is opened, by default it saved in png format





#Savefig method with parameters
plt.plot(x1, y1, color="r")

plt.savefig("savefig2.jpg", dpi=2000, facecolor="y", transparent=True, bbox_inches="tight")         
                                    #with named parameter -- dpi -- you can select the resolution of the downloaded image, dpi stands for dots per inch
                                    #with named parameter -- facecolor -- you can change the boundary background color of the image
                                    #To save the file as other format, pass the format extension at the end of the file name (ex: savefig.pdf)
                                    #With named parameter -- transparent -- you can make the background of the graph transperent,, by default it is False
                                    #with named parameter -- bbox_inches -- you can modify the size of the box, google for value





