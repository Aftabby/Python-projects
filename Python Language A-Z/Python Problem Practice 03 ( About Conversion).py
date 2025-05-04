#Binary to Decimal

def bin_to_dec(num):
    dec = []
    for index, digit in enumerate(num):             #Enumerate function returns the value sequentiall along with it's index number, so it returns two value
        dec.append(int(digit)* (2 ** (index)))
    return sum(dec)

num = input("Enter the binary number: \n")
print(bin_to_dec(num))






#Decimal to Binary

def dec_to_bin(num):
    binary = []
    while num > 0:
        binary.append(num % 2)
        num = (num // 2)  # num = int(num/2) --- also works --- // is floor division
    binary.reverse()  # Reverse the whole list

    return ''.join([str(digit) for digit in binary])    #By the -- ''.join(list_name)  -- we can convert a total list into one string, but only condition is the elements of the list should be string.
                                                        # So we used a list comprehension, to get each element of the list, and converting each element to string, before passing it to the join() method
                                                        # --  ''.join(list_name)  -- is a method of the class string, that's why we started the method with an empty string

num = int(input("Enter a decimal number: \n"))
num = int(dec_to_bin(num))      #The function will return string, we just converted to int
print(num)

#-------------Another approach ( Using recursive function) *** Important concept
def dec_bin(num):
    if num > 1:
        dec_bin(num // 2)
    print(num % 2, end = '')
num = int(input("Enter a decimal number recursive function: \n"))
num = dec_bin(num)
print("\n")
#----------




#Miles to Kilometeres

def mile_to_km(mile):
    return mile * 1.61

mile = float(input("Enter miles: "))
print(str(mile) + " mile = " + str(mile_to_km(mile)) + " Kilometer\n")




#Queries
#What does the round function do? - Round function rounds a float value, depending upon the parameter you pass to it, it keeps that numbers of digit after decimal
# -- Ans: It takes two parameter or argument, one is the float type data variable and another one is how many decimal points you want to display
#what is end='' in print function, it is used to print in the same line using multiple print functions

#Important Notes
# print("anything", end = '') doesn't add a new line in the end