from matplotlib import pyplot as plt
import numpy as np

# =================  Axis Matplotlib Plots  ============
                                                #IT is the ways to play/modify with the axis with the following method
                                                # xticks() , yticks(), xlim() , ylim() , axis()



x1 = [1, 2, 3, 4]
y1 = [10, 30, 20, 50]
label1 = ["python", "JS", "HTML", "CSS"]

plt.plot(x1, y1, color="r")
plt.show()




#Scaling/Naming the axis
plt.plot(x1, y1, color="r")
plt.xticks(x1, labels=label1)          # -- plt.xticks() -- pass the same number of elements to name the x-axis accordingly,, with labels parameter, we can name each of the ticks
plt.yticks(y1)           # -- plt.yticks() -- pass the same number of elements to name the y-axis in ascending order

plt.show()








#Extending the limit of the axis
plt.plot(x1, y1, color="r")
plt.xlim(0, 10)        # -- xlim() -- method takes two parameters (start_range, stop_range) , and by that it scales the x-axis accordingly with keeping the data graph intact
plt.ylim(0, 100)        # -- ylim() -- method takes two parameters (start_range, stop_range) , and by that it scales the y-axis accordingly with keeping the data graph intact

    #We can do the same thing also with the below line
plt.axis(0, 10, 0, 100)     # -- plt.axis(start_range_x_axis, stop_range_x_axis, start_range_y_axis, stop_range_y_axis)

plt.show()














