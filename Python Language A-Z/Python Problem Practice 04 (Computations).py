


#Prime Factors
def isPrime(num):
    for i in range(2, int((num/2)+1)): # Instead of int(num/2), you can use (num//2) , also you can -- import math -- math.ceil(num/2) -- instead of using -- int((num/2)+1) --
        if num % i == 0:
            return False
    return True

def primeNumbers(num):
    prime_number_list = []
    for i in range(2, num+1):   #Because range function doesn't include the end_range_value, we have to add an extra one(1)
        if isPrime(i):
            prime_number_list.append(i)
    return prime_number_list
        
# ----- Till now we found the list of all prime numbers

def primeFactors(prime_list, num):
    prime_factors = []
    for i in prime_list:
        if num % i == 0:
            prime_factors.append(i)
    return prime_factors
# ------ Now we found the prime factors list
num = int(input("Enter the number to get a prime factors list: \n"))

all_prime = primeNumbers(num)
prime_factors = primeFactors(all_prime, num)

print(prime_factors)











#All Prime numbers
def isPrime(num):
    for i in range(2, int((num/2)+1)): # Instead of int(num/2), you can use (num//2)
        if num % i == 0:
            return False
    return True

def primeNumbers(num):
    prime_number_list = []
    for i in range(2, num+1):
        if isPrime(i):
            prime_number_list.append(i)
    return prime_number_list
        
num = int(input("Enter the number to get a prime numbers list: \n"))

print(primeNumbers(num))




#Check Prime
num = int(input("Enter a number to check prime or not: \n"))
clock = int(num/2)
isPrime = 1
while clock > 1:
    if (num % clock == 0):
        isPrime = 0
        break
    clock -= 1

if isPrime == 1:
    print("The number is prime.\n")
else:
    print("The number is not prime.\n")










#Triangle Area
import math
a = float(input("Enter the value of side: \n"))
b = float(input("Enter the value of side: \n"))
c = float(input("Enter the value of side: \n"))

s = (a + b + c) / 2
area = math.sqrt(s * (s - a)*(s - b)*(s - c))  # To calculate the root , we imported math module and used math.sqrt
print("Area of your triangle", round(area, 2))









#Compound Interest
def comp_interest(primary, interest_rate, year):
    total_amount = primary * ((1 + (interest_rate/100)) ** year)    #Just using formula
    return total_amount

primary = int(input("How much did you take?\n"))
interest_rate = float(input("How much is the interest rate?\n"))
year = float(input("For how many years did you take it?\n"))

print("Total amount payable: ", comp_interest(primary, interest_rate, year))









#Simple Interest 
def simple_interest(primary, interest_rate, year):
    total_amount = (((interest_rate / 100) * primary) * year ) + primary
    return total_amount

primary = int(input("How much did you take?\n"))
interest_rate = float(input("How much is the interest rate?\n"))
year = float(input("For how many years did you take it?\n"))

print("Total amount payable: ", simple_interest(primary, interest_rate, year))