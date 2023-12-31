#Print function mainly take 3 arguments
# print(*object, sep=' ' , end="\n")
# 1st - As much object as you give, 
# 2nd - It will separate each parameter with a ' ' by default while printing
# 3rd - After every print function finishes printing there will be an end of the line i.e. \n

sentence1 = "Hello, my name is Aftab."
sentence2 = "I've been into programming \"since my childhood."  #YOu can backslash to use escape character, computer will not end the string there
sentence3 = "Adios!"
print(sentence1, sentence2)
print(sentence3)


print(sentence1, sentence2, sep = '*separator*', end = "")
print(sentence3)


#F - String / Format string - One special kind of string that tells python to format stuff in the string in a special way
print(f"Hello {sentence1}")
print("\n\n\n")
# Formatting number in a string
num = 1000000000
print(f"{num:,}")   # IT'll add comma in the number like 1,000,000

num = 10.66666666
print(f"{num:.2f}") #10.67
print(f"{num}") #10.66666666
num = round(num, 3) #10.667
print(num)





# string_name.strip() -- Removes trailing and leading whitespaces from string by default
name = input("What's your name? ")
name = name.strip()
print(name)
#Capitalizing the first letter of a string -- string_name.capitalize
name = name.capitalize()
print(name)
# Title base capitalization , capitalizing first letter of each of the word
name = name.title()
print(name)

# Split user's name into first name and last name
first, last = name.split(" ")
print(f"hello, {first}")


print("\n\n\n")


# Standard way to put the codes
