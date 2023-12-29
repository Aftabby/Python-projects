#name = input("What's your name?")

#

#with open("names.txt", "a") as file:   #If you open a file like -- with open("file_name_in_pc", "read/write/append_mode") as variable_name:  --- then the file automatically closes when not indented, you don't have to close it manually
    #file.write(f"{name}\n")

with open("names.txt", "r") as file:
    lines = file.readlines()

for _ in lines:
    print(_, end='')
    #print(_.rstrip())  Does the same thing



# To read file 
with open("names.txt", "r") as file:
    for line in file:   #that means you can  iterate over file, and each time the loop variable will be a variable
        print(f"hello, {line.rstrip()}") 



#sorting the file - And modifying the contents of the file
names= []
with open("names.txt") as file: #By default it will read the files, that is "r"
    for line in file:
        names.append(line.rstrip())   #rstrip removes the white spaces and new line from the beginning and end of an element
    #names.sort()
    #print(names)
    
    for name in sorted(names):
        print(f"yoyo, {name}")



#sorting the file - easily
with open("names.txt") as file:
    for line in sorted(file):
        print(line.rstrip())