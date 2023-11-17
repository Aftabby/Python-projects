#Binary to Decimal

def bin_to_dec(num):
    dec = []
    indexx = 0
    for i in num:
        dec.append(int(i)* (2 ** (indexx)))
        indexx += 1
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
    binarystr = ''
    for bit in binary: # From list to a string
        binarystr += str(bit)

    return binarystr

num = int(input("Enter a decimal number: \n"))
num = dec_to_bin(num)
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
#What does the round function do? 
# -- Ans: It takes two parameter or argument, one is the float type data variable and another one is how many decimal points you want to display
#what is end='' in print function, it is used to print in the same line using multiple print functions

#Important Notes
# print("anything", end = '') doesn't add a new line in the end