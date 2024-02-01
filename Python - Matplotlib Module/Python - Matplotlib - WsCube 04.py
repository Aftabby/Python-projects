import matplotlib.pyplot as plt
import numpy as np



# ======================   How to Create a Pie Chart in Python  ===============


list1 = [10, 20, 30, 40]
list2 = [40, 50, 30, 10]
label1 = ["Javascript", "CSS", "HTML", "Python"]
explode1 = [0.0, 0.0, 0.0, 0.4]
color1 = ["m", "g", "y", "b"]


#Creating a simple pie-chart
plt.pie(list1, labels=label1, explode=explode1, colors=color1)       #With named parameter -- labels=list_of_value_named -- we can create label to the pie chart beside every portion of the pie -- N.B: This is -- labels -- not -- label --
                                                                    #With named parameter -- explode=list -- we can make a certain segment to pop out of the original pie circle, it works according to the indexed values
                                                                    #With named parameter -- colors=list_of_colors -- you can change the default color variant of the pie chart to your own, N.B: it is -- colors -- not -- color --


                                                                    
plt.title("IT IS THE TITLE")        #Showing the title of the graph
plt.legend(loc=2)        #To show the label and color as a separate box, use the method -- plt.legend()  --- and changing the location of it with parameter -- loc -- whose value is (1/2/3/4)

plt.show()













#Showing percentage value to every portion of pie chart and adding shadow
plt.pie(list1, labels=label1, autopct="%0.1f", shadow=True)    #With named parameter -- autopct= special_string_format -- we can show percentage to each slice of pie, special string format: which starts with(%) , with --%0.1f%% -- we are specifying we want to see percentage in float value(f for float) and we want to see 1 value after decimal(0.1), also the last two percentage sign (%%) because we want to see the percentage sign after the value 
                                                                #With named parameter -- shadow=True -- we can show a visual shadow of the pie, by default it is False

plt.show()















#Changing the radius of the pie and distance of the label from the pie sections

plt.pie(list1, labels=label1, radius=1.2, labeldistance=1.2)   # -- radius=integer -- and -- labeldistance=intergar -- takes an relative integer value

plt.show()







#Rotating the pie and changing the text/label property
plt.pie(list1, labels=label1, startangle=270, textprops={"fontsize":20})       # -- startangle -- takes the value of the degree you want to start the first value from,, by default the first value starts from the 0 degree 
                                                                # -- textprops -- parameter stands for text property, and it takes a dictionary as a value
plt.show()






#Changing the direction of the pie(clockwise/counter-clockwise) and changing the wedge property(google it)
plt.pie(list1, labels=label1, counterclock=False, wedgeprops={"linewidth":5, "edgecolor":"y"})   # -- counterclock -- paramter is by default True    ]
                                                                                                 # -- wedgeprops -- takes a dictionary as a value
plt.show()








#Changing the center of the pie and rotating label
plt.pie(list1, labels=label1, center=(6,6), rotatelabels=True) # -- center -- paramter takes a tuple of the value (x,y) in 2D, to where to put the center,, the I don't see any changes in center (I think it changes the center of the labels)
plt.show()                                                              # -- rotatelabel -- paramter is by default False








#Creating multiple pie chart together
plt.pie(list1, labels=label1, radius=1.5)           #The radius of the initial pie always should be more than the following pie chart's radius, else you can't see them as they overlap on one anoter
plt.pie(list2, labels=label1, radius=0.5)


    #Below two funcions works the same
#plt.pie([1], colors="w", radius=1)         #To create a ring pie chart, i.e over lapping another pie chart with one value and color white
#circle = plt.Circle(xy=(0,0), radius=1, facecolor="w")     #No explanation
#plt.gca().add_artist(circle)

plt.show()

