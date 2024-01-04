from tkinter import *   #importing tkinter library

root = Tk()         # tkinter library provides a -- Tk() -- toolkit, which is a thin object-oriented layer that helps to create GUI in python. Tk() initializes the class, and 'root' is the name given to the object 
root.title("My First GUI")          # Giving title to your GUI window, IT is optional
root.geometry("500x200")    # You can mention the size of the GUI window in pixel as X x Y format, though it is optional


# WIDGET - is the element we add in the GUI that might represent some information and enables user to interact with the window
            # Tkinter provides various widgets , each widgets are nothing but an object of their respective Python Class
            # We create widget object with their class, and with the help of Geometry Managers we place it into our GUI


# Geometry Manager - pack() - it organizes widget in blocks before placing them in the parent widget.
                #  - grid() - It organizes widget in a table - like structure in the parent widget.
                #  - place() - It organizes widgets by placing them in a specific position in the parent widget.

#you CANNOT use pack and grid inside the same class or for the same frame. Thus, use only one.

# Label Widget - It is used to display text or images to the GUI.
                # object_name = Label(parent_window_name, options...)     
                # Label is the class that represent label widget

#course = Label(root, text = "Programming Languages", bg = "red", fg = "white")         #you CANNOT use pack and grid inside the same class or for the same frame. Thus, use only one.
#Now put that label object to geometry manager to show it on window
#course.pack()       


#Button Widget - It is used to add button in Python GUI Application
                    # object_name = Button(parent, options...)
                        # Button is a class that represents button object

python = Button(root, text = "Python" , width= 8)
java = Button(root, text = "Java" , width= 8)
cpp = Button(root, text ="C ++" , width= 8)
js = Button(root, text = "Javascript", width = 8)

#enroll = Button(root, text = "Enroll Now", bd = 5, fg = "blue", bg = "yellow")
#enroll.pack()   #Geometry manager


#Grid - Geometry manager with button

python.grid(row=0, column = 0)
java.grid(row = 0, column = 1)
cpp.grid(row = 1, column = 0)
js.grid(row = 1, column = 1)




# ENTRY - Text Field Widget - It is used to add text box to GUI app
        # It is used to accept a single-line text string from an user
        # 



root.mainloop()     # This is a must have line in tkinter code, it holds the GUI onto the screen