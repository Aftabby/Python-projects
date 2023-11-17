#Remove duplicate chars from the string
def remove_char(index1, string1):
    res = ''
    for i in range(len(string1)):
        if i != index1:
            res += string1[i]
    return res


def remove_duplicate(string1):
    j = 1
    for i in string1:
        for k in range(j, len(string1)):
            if k == len(string1):  # Here is a slight mistake, if the last two character is same it doesn't remove any of it
                break
            if i == string1[k] and j < len(string1):
                string1 = remove_char(k, string1)
        j += 1
    return string1

string_one = "Hello world! HOw are all of you??"
string_one = remove_duplicate(string_one)
print(string_one)
#-------Another Approach-----------
def remove_dup(string1):
    res = ''
    for char in string1:
        if char not in res:  # 'not in' KW is just the opposite of 'in' KW
            res += char
    return res
string_one = "Hello world! HOw are all of you??"
string_one = remove_dup(string_one)
print(string_one)

#Find the second smallest of a list
def second_smallest(nums):
    nums.sort() # Or you can use--- nums = sorted(nums) -- does the same thing
    return nums[1]

nums = [ 5, 75, 89, 12, 44, 23, 22]
print(second_smallest(nums))
#----Another approach -----
nums.remove(min(nums))
print(min(nums))




#Find the second largest of a list
def second_largest(nums): # variable inside a function is different from the variable outside or global variable
    sec_large = max(nums)
    nums.remove(sec_large)
    sec_large = max(nums)
    return sec_large

nums = [ 5, 75, 89, 12, 44, 23, 22]
sec_large = second_largest(nums)
print(sec_large)
#---------Another approach------------
nums = [ 5, 75, 89, 12, 44, 23, 22]
nums.sort()
print(nums[-2])  # Reverse Index: when you -1 as index it will point to the last element of the list, same way -2 will point to the second last element of the list
# ---------------- Another approach--------------
nums.sort(reverse = True) 
print(nums[1]) # Using listName.sort(reverse = True) will sort the list in descending order





#Sum of Squares
num = int(input("Enter a number:\n"))
sum_up = 0
for i in range(num+1):
    print("value of i", i, "\n")
    sum_up += i**2
print(sum_up)
#--------Another approach
def sum_of_square(num):
    num = num*(num+1)*(2*num+1)/6 # When you divide and assign variable, the data type of that variable become float type 
    return num
print(sum_of_square(num))








#Find the largest element of a list
nums = [ 5, 75, 89, 12, 44, 23, 22]
highest_num = max(nums)
print(highest_num)
#--------Another Approach
highest_num = nums[0]
for i in nums:
    if i > highest_num:
        highest_num = i
print(highest_num)








# Easy way sum up a list
nums = [ 5, 75, 89, 12, 44, 23, 22]
sum_of_nums = sum(nums)
print(sum_of_nums)



#Important Notes
# Use the sum function to add element of a list
# Use max function to get the highest number out of a list && Use min for smallest
# Reverse Index: when you -1 as index it will point to the last element of the list, same way -2 will point to the second last element of the list
# Using listName.sort(reverse = True) will sort the list in descending order
# 'not in' KW is just the opposite of 'in' KW