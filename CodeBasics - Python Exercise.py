











#String Replacing
sentence = "maine 200 banana khaye"
sentence = sentence.replace('banana', 'samosa')
sentence = sentence.replace('200', '10')
print("String replacing using two lines:", sentence)


sentence = "maine 200 banana khaye"
sentence = sentence.replace("banana", "samosa").replace('200', '10')
print("String replacing in one line: ", sentence)


#Another python f-string
vegetable = 25
fruit = 33

print(f'I eat {vegetable} veggies and {fruit} fruits daily.')



#Slicing operator and negative index
sentence = "Earth revolves around the sun"

print(sentence[6:14])
print(sentence[-3:])










#String and f-string
street = "Kazipara, Mirpur"
city = "Dhaka-1216"
country = "Bangladesh"
address = street + '\n' + city + '\n' + country

print("Address using + operator: ", address)

address = f'{street}\n{city}\n{country}'
print("Address using f-string: ", address)




# Print binary representation of number 17
num = 17
print("Binary of number 17 is: ", format(num, 'b'))     #Formatting a number by -- function -- which takes two argument one is the number and another is the formatting type


