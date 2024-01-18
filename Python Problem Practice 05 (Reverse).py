#Reverse the words only
def white_space_rev(str):
    white_space = []
    index = len(str) - 1
    for i in str[::-1]:     #Google str[::-1] to know how it works, basically in list/string slicing -- string_name[start_index : end_index : stepsize] ,, so when we passed the negative one (-1) in step size, the list/string is reversed
        if(i == ' '):
            white_space.append(index)
        index -= 1
    white_space.append(-1)
    return white_space

def rev_words(str):
    white_space_in_rev = white_space_rev(str)
    rev_str = ''
    j = 0
    while True:
        for i in str[(white_space_in_rev[j] + 1):]:
            if i != ' ':
                rev_str += i
            else:
                break
        j += 1
        if j == len(white_space_in_rev):
            break
        rev_str += ' '
    return rev_str


str1 = "Are you okay?"
print(rev_words(str1))
# -------------------Another important approach------
def rev_wordss(str2):
    str2 = str2.split()     # If you don't pass any parameter, split method will split the words by whitespaces and return a list of all the individual words, if you pass a character as a parameter it will break the string by that character.
    str2.reverse()          # .reverse() method reverses a list
    rev_str = ' '.join(str2)  # The opposite of split is join method, it adds all the the element/string of a list/array together, if you want to join them by whitespaces run ---  ' '.join(array)
    
    print(rev_str)

str2 = "Hello huney bunny dongor fongor"

rev_wordss(str2)






#Reverse Domain
sites = "www.programming-hub.com"
parts = sites.split('.')    #Returns a split list
parts.reverse()
parts = '.'.join(parts)     # -- ''.join(list_name) -- is a string class method, which adds every element of list, and adds the string on which it was called upon (here it is -- dot(.)) , between all the elements
print(parts)
#----------ANother approach--------
site = "www.programming-hub.com"
rev = '.'.join(reversed(site.split('.')))       # list_name.reverse() -- and -- reversed(list_name) does the same thing
print(rev)














#Reverse a number
def max_dec(num):
    dec = 1
    while num > 0:
        num = round(num / 10)
        dec = dec * 10
    return int(dec / 10)

def rev_num(num):
    decimal = max_dec(num)  #for 3 digits it will be 100, for 4 digits 100 and so on..
    digit = 0
    rem = num

    while rem > 0:
        digit += (rem % 10) * decimal
        rem = rem // 10         # Or you can use rem = round(rem / 10, 0)
        decimal = round(decimal/10, 0)     #Or you can use decimal = decimal // 10
    return digit

num = int(input("Enter any number to reverse: \n"))
num = int(rev_num(num))
print(num)
#--------------ANother approach-----
def rev_number(num):
    reverse = 0
    while num > 0:
        reverse =  (reverse * 10) + (num % 10)
        num = num //10 
    return reverse
n = int(input("Enter number: \n"))
reverse = rev_number(n)
print(reverse)








#Reverse String (Recursive):
def rev_rec(str):
    if len(str) == 0:
        return str
    else:
        return rev_rec(str[1:]) + str[0]  # It's called slicing, works both for list and string
    
    

str = input("Enter any string:  \n")
rev_str = rev_rec(str)

print(rev_str)
#-----------Another approach----
txt = "Welcome to the Jungle"
print(txt[::-1])       # How does it work??? Added to queries below








#Reverse String (Stack)
def reverse_stack(str):
    stack = []
    for char in str: #string to list, to use method and function that only works on lists
        stack.append(char)
    rev = ''
    while len(stack)>0:
        last = stack.pop()  #pop method by default (if not index given) removes the last element from the list and return the element
        rev += last

    return rev

usr_str = input("ENter your string:\n")
reverse = reverse_stack(usr_str)
print(("Reversed is: ", reverse))








#Reverse String
def revString(docs):
    rev_string =''
    length = 1
    while length <= len(docs):
        rev_string += docs[(-1)*length]  # for i in docs --- rev_string = i + rev_string ------ IT also works
        length += 1
    return rev_string

docs = input("Enter any string:\n")
print(revString(docs))



#Queries
# Search google for txt[::-1] how does it work? and print reverse string 
# what is reversed()  (Not reverse it's reversed)


#Important Notes
# A python is almost like a list, BUT Not a list
# Python is case sensitive, the variable num, Num, NUM is three different variables
# You can't append, remove, or set e character to string by the INDEX 
# list[3:6] , string[2:], list[:5]  --- It's called slicing, works both for list and string
# .split() = If you don't pass any parameter, split method will split the words by whitespaces and return a list of all the individual words, if you pass a character as a parameter it will break the string by that character.
# .join() = The opposite of split is join method, it adds all the the element/string of a list/array together, if you want to join them by whitespaces run ---  ' '.join(array)
# .reverse() method reverses a list