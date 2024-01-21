# Algorithm

#Recursion algorithm
# factorial using iteration
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

#factorial using recursion algorithm
def factorial(n):
    if n <= 1:      #Stopping condition or base condition
        return 1
    else:
        return n * factorial(n-1)       # Calling the function itself
    
print(factorial(5))





#Pseudocode
# It is a step by step process to solve a problem. Pseudocode is an easier way to think about the code.




#Search Algorithm
# A step by step process to find an element is called Search Algorithm.
# A linear search takes linear time, time increases linearly for more elements. If the list has n elements, we have to check n times.




#Binary Search
# The reason it is called binary search is that it divides the search space into two equal parts. And choose one to continue with, ignoring the other part.
# It only works for a sorted list.
# The time complexity of binary search is -- O(logn) -- 



#Recursion Algorithm
# It has two conditions: A stopping condition or base condition --- and --- call the function itself.
# Recursive algorithm calls itself from inside




#Time Complexity
# The efficiency of a code is measured by the time taken by an algorithm while running.
# Thie comparison of time to measure the efficincy of an algorithm is called Time complexity
# Linear Time Complexity: To measure we need two things - 1. The input size, 2. The growth rate. If the array han 'n' elementts, we have to check 'n' times
# Linear Time Complexity: Every time we increase one or ten more elements, we have to check one or ten more elements. that is, our checking time increases linearly with the increase of the number of input elements.
# Linear Time Complexity: When the time complexity changes linearly with the change of the number of the input elements, the algorithm complexity is called --- O(n) --- pronounced as - ooh an --The time complexity O(n) has two parts - 1. Input size 'n', 2. Growth rate 0. A for loop gas O(n) time complexity.
# For nested For loops - the inner loop has a time complexity of --- O(n^2) -- read as- ooh an square --- this mean, you increase one element in the input list, the time will increase by a square of elements - this is called --- Quadratic Time Complexity --- that is if you add 1 element then you have check n element more. Thus, time complexity is increasingly quadratically.
# Constant Time Complexity: Suppose, you know the index of the element you want to find, the just by running --- list_name[index_number] -- you will get the element. For direct access, it will take exactly the same amount of time regardless the size of the list. The time complexity -- O(1) -- read it as --- ooh one --- It is not searching , more of direct accessing.







#Important Notes
# When you have some specific steps to do something or solve a problem it's called an algorithm
# While programming, you will have multiple ways to do the same task, you will select the most efficient way of doing the task
# The algorithm must have - 1. Correctness, 2. Efficiency
# Faster and efficient than the other alternative options