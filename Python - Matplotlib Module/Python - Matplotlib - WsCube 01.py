import matplotlib.pyplot as plt         # -- matplotlib -- is a library, where as pyplot is a module of that library. Library is consists of one or more library

list1 = [2, 3, 4, 5]
list2 = [3, 5, 6, 5]

color_list1 = ["r", "y", "g", "b"]

plt.bar(list1, list2, color = color_list1)
plt.show()