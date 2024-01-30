from matplotlib import pyplot as plt
import numpy as np

# =================  Working with Text in Matplotlib  ============

x1 = [1, 2, 3, 4, 5]
y1 = [10, 30, 20, 50, 40]

plt.plot(x1, y1, color="r")


plt.title("THIS IS TITLE", fontsize=20)
plt.xlabel("THIS IS X-LABEL", fontsize=20)
plt.ylabel("THIS IS Y_LABEL", fontsize=20)

plt.text(2, 35, "TEXT", fontsize=15, style="italic", bbox={"facecolor":"g"})       #-- plt.text() -- takes mandatory 3 paramters, which is (position_of_the_text_in_x_axis, position_of_the_text_in_y_axis, Text)
                                                                #With named parameter -- bbox -- we can create a box around the takes, this pamaeter takes a dictionary as value, and in the dictionary you can pass all the property of the box



plt.annotate("Annotate", xy=(2,1), xytext=(3,10), arrowprops=dict(facecolor="black", shrink=100))   # -- plt.annotate -- method helps to annotation a point, here the value passed, first the explanation text , second -- xy=(2,1) -- is the postion of which point arrow should point, third -- xytext=(3,10) -- is the position of where the text explanation text should be
                                                                                    #With named parameter -- arrowprops -- we can set the property of the arrow, it takes a dictionary as value


plt.legend(["Label"], loc=9, facecolor="Blue", edgecolor="Green", framealpha=0.8, shadow=True)       #You already know what legend method does, loc parameter is to set the location of the label (which takes value from 0 to 10)



plt.show()


