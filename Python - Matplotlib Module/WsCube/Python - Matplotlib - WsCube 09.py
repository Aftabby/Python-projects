from matplotlib import pyplot as plt
import numpy as np

# ==============  Fill Between Plot in Matplotlib  ============
                                                    #Fill between is not any kind of graph, rather it fill the gap between data graph line and base line with color


x1 = [1, 2, 3, 4]
y1 = [1, 4, 2, 3]

plt.plot(x1, y1, color="r")

plt.fill_between(x1, y1)      #With -- fill_between() -- method, by default if the x-axis and y-axis value is passed, it will fill the gap between data line and base line(x-axis) with default color,, N.B: It is independent of the -- plt.plot() -- or other plotting method, i.e you can fill other areas with it as well

plt.title("This is title")
plt.xlabel("This is X label")
plt.ylabel("This is Y label")

plt.show()







#Using fill_between indepedently

plt.plot(x1, y1, color="r")
plt.fill_between([2, 4], [3, 5])        # -- plt.fill_between(x, y1, y2) -- if you don't pass y2, it will take reference from the base line
plt.show()



plt.plot(x1, y1, color="r")
plt.fill_between([2, 4], 3, 5, color="g")          # In x-axis the color will be filled within 2 and 4 value, and within y-axis it will be within 3 and 5 value
plt.show()




plt.plot(x1, y1, color="r")
plt.fill_between(x1, y1, where=(np.array(x1)>=2) & (np.array(x1)<=4))
                                                            #With named parameter -- where -- we can pass a condition to only fill the graph portion only where the condition is True, --and-- is a logical operator and --&-- is bitwise operator,, comparison operator doesnt't work with list so we converted the list to numpy array
plt.show()