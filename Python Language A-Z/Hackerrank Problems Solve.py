





#Mini - Max Sum
a = input() #Numbers will be give in a line with whitespaces
b = (a.split())  #To split numbers(still as string) by whitespaces and taking output as a list

#converting list element from string to integar
b = [int(i) for i in b if int(i) > 0]  # Using list comprehension
#b = list(map(int, b)) #ANother approach - doing the same thing using map function

maxx = sum(b) - min(b)
minn = sum(b) - max(b)

print(f"{minn} {maxx}")



#Important Notes
# map(function_name, list_name) --- map runs the parameter function_name for every element in the list
# list comprehension -- [Output -- Collection -- Condition] or in another word [ Do this -- for this elements of list -- In this condition]