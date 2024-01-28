import calendar

cal = calendar.month(2016, 1)
print(cal)

print(calendar.isleap(2016))
print(dir(calendar))






#MATH Module

import math         #Importing a module called python

square_root = math.sqrt(16)     
print(square_root)
power = math.pow(2,5)       # 2^5
print(power)

print(math.log10(100))
print(math.floor(2.36))
print(math.ceil(2.36))


print(dir(math))            #Showing all the functions present in math module 


import math as m            # Importing a function and change it's name to a temporary name (Just for easy readability or easy typing)
print(m.ceil(20.36))







#Important Notes
# Module is nothing but a library of functions
# To find all the functions present in a module, import that module by -- import module_name -- , then -- dir(module_name) --- or google for the list of functions or modules ---
# Custom mudule is the list of functions you create by -- def function_name(): --- 
# Custom functions: In the same directory if you have two file, --functions.py (which is your custom function) -- and -- program.py --- you can import your custom functions easily to your 'program.py' file by just typing--  import functions -- 
# Custom functions: Then to use that custom function in -- programm.py -- you have to write -- functions.function_name -- just like the default modules, the custom -- functions.py -- will act like a module
# Custom function: If the program.py and module file (functions.py) is not in the same directory - after import type the path -- let's say functions.py is in a subdirectory named -- modules_folder -- then write -- import modules_folder.functions --- 
# Custom function: Better to use a system path and sys module -- import sys -- for the file location of -- functions.py --
# To change any module name in your programm.py file --- import module_name as alias(temporary_name) -- example -- import math as m -- now you can use function -- m.pow() -- instead of -- math.pow() -- (Just for easy readability or easy typing)