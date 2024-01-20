
# Module is simply a programming file, just like this one, which we can use for reusability, and faster development of code. 
# Module consists of variable, methods, class etc. which we can use in our code.


# Three ways to import a module :
        # 1. Using the import statement - Imports the whole module in our code, import module_name
        # 2. Using the 'as' keyword - Importing and renaming the module. --  import module_name as m  -- here 'm' is a shorter version of the module name, 
        # 3. Using the from_import statement  - In situation where we just need some particular funcion from a module,  -- from module_name import function_name


# There are three types of module:
        # 1. Built-in modules
        # 2. Third-party module (also known as package)
        # 3. Custom module




# ==============================================  Built-in Module  =====================================

import math             #That's how you import a module

a = 4.6
print(math.floor(a))                    #When you imported only the module, you can access its function by -- module_name.function_name() ---
print(math.ceil(a))                    



import os               #this operating system built-in module will help us to interact with the operating system

print(os.name)          # here the -- name -- is not a function rather a variable inside os module
print(os.getcwd())      # It returns the  current working directory(CWD) from the file you are executing the code

# YOu can make directory by -- os.mkdir()  -- and also rename an existing file --  os.rename() --






#===================================  Third-Party Module  ========================

# You gotta install thirt-party modules first before importing that module to your code, these modules are also called package
# Python third-party packages are hosted on PyPI(Python Package Index) -- just like third party apps are hosted in playstore
# PIP is the package manager of python, which helps us to install thirt party packages
# In the command line we have to write -- pip install package_name -- once we install the module we can use it just like built-in module





#==============================  Custom Module  =======================

# Custom modules are simple python file that can be importedinto another file, and created by you according to your own needs
# Perks of creating custom module : When your program has a large number of classes, function and variable, it is conventional to keep that in separate files (custom module) by similar relevance
# How to create: create a file, say logic.py, which is the custom module containing logics of relevance topic, and in your original file use -- import logic  -- to import the logic.py and use it's functionability
