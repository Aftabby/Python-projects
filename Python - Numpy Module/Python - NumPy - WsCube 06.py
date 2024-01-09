import numpy as np

#Arithmatic Operation in NumPy

#=============================================================================================
# a+b np.add(a, b)                  # a-b np.subtract(a, b)         # a*b  np.multiply(a,b)
# a/b np.divide(a,b)                # a%b np.mod(a, b)              # a**b np.power(a**b)
# 1/a np.reciprocal(a)
#=============================================================================================
# Minimum Value np.min(a)           # Maximum Value np.max(a)       # Postion of Minimum Value np.argmin(a, axis=)           - Arguments of min(argmin)    N.B: Min, Max - For multidimensional array you have to pass axis(0 or 1 etc.) to find the minimum/maximum element of column or rows
# Cosine  np.cos(a)                 # Sine      np.sin(a)           #Postion of Maximum Value  np.argmax(a, axis=)           - Arguments of max(argmax)    
# Cumulative Sum  np.cumsum(a)      # # Square Root   np.sqrt(a)
#===============================================================================================



#Addition - with constant and with other arrays - only the arrays of the same shapes can be added together
            # Same procedures applies for any dimension of array
list1 = [1, 2, 3, 4]
arr1 = np.array(list1)

print("Array1:\n", arr1, "\nArray1 + 3 :\n", arr1+3)

list2 = [5, 6, 7, 8]
arr2 = np.array(list2)

print("\n\nArray 1: \n", arr1, "\nArray2: \n", arr2, "\nArray1 + Array2:\n", arr1 + arr2)   # To add you can also use function to do the same task - the functions are described at the top of the file, the function returns the calculated result as an array






#Subtraction- with constant and with other arrays - only the arrays of the same shapes can be subtracted from each other
print("Array1:\n", arr1, "\nArray1 - 3 :\n", (arr1 - 3))
print("\n\nArray 1: \n", arr1, "\nArray2: \n", arr2, "\nArray1 - Array2:\n", (arr1 - arr2)) # # To add you can also use function to do the same task - the functions are described at the top of the file, the function returns the calculated result as an array





#Multiplication - with constant and with other arrays - only the arrays of the same shapes can be multiplied with each other
print("Array1:\n", arr1, "\nArray1 * 3 :\n", (arr1 * 3))
print("\n\nArray 1: \n", arr1, "\nArray2: \n", arr2, "\nArray1 * Array2:\n", (arr1 * arr2)) # To add you can also use function to do the same task - the functions are described at the top of the file, the function returns the calculated result as an array




#Division -with constant and with other arrays - only the arrays of the same shapes can be divided by one another
print("Array1:\n", arr1, "\nArray1 / 3 :\n", (arr1 / 3))
print("\n\nArray 1: \n", arr1, "\nArray2: \n", arr2, "\nArray1 / Array2:\n", (arr1 / arr2)) # To add you can also use function to do the same task - the functions are described at the top of the file, the function returns the calculated result as an array



#Modulus - with constant and with other arrays - other array should be of same shape, to find modulus
print("Array1:\n", arr1, "\nArray1 % 3 :\n", (arr1 % 3))
print("\n\nArray 1: \n", arr1, "\nArray2: \n", arr2, "\nArray2 % Array1:\n", (arr2 % arr1)) ## To add you can also use function to do the same task - the functions are described at the top of the file, the function returns the calculated result as an array



#--------------------------------------------------------------------------------

list3 = [1, 3, 6, 12, 9, 4, 2]
arr3  = np.array(list3)

print("Array3 :\n", arr3, "\nMin :", np.min(arr3), "\nMax :", np.max(arr3), "\nArgmin: ", np.argmin(arr3), "\nArgmax :", np.argmax(arr3))
print("Sine: \n", np.sin(arr3))
print("Cumulative Sum: \n", np.cumsum(arr3))    # Cumulative sum adds adds all element before that particular element with it, example: let's say you wanna apply cumulative sum to the array [a  b  c], it will be [a  a+b  a+b+c]