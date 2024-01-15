import numpy as np

# =====  Matrix in NumPy Array  =====

list1 = np.matrix([[1, 2, 3], [4, 5, 6]])

arr1 = np.array(list1)              # Creating Array
matrix1 = np.matrix(list1)          # Creating Matrix

print("Array:\n", arr1, "\nData type: ", type(arr1))
print("\nMatrix:\n", matrix1, "\nData type: ", type(matrix1))       #Though both look exactly same, but the data type (class) is different



# The difference between Array and Matrix
                # The addition, subtraction of two array and two matrix is similar
                # But the multiplication between two array and two matrix is different

        # Multiplication of array:
 #               [[a11 a12]         [[b11 b12]]             [[a11*b11  a12*b12]
 #                [a21 a22]]    X    [b21 b22]]     =        [a21*b21  a22*b22]]
 

        # Multiplication on matrix: (dot multiplication)
#                [[a11 a12]          [[b11  b12]            [[(a11*b11)+(a12*b21)     (a11*b12)+(a12*b22)]
#                 [a21 a22]]    X     [b21  b22]    =        [(a21*b11)+(a22*b21)     (a21*b12)+(a22*b22)]]





#We can also multuply two matrix using -- matrix_name.dot() -- function,, 
                    #to multiply two matrix the both matrix must be under same broadcast i.e one's row number should match other's column number and vice versa
                        # The new result matrix's shape will be, (row of the first operand, column of the second operand)
list2 = [[7, 8], [9, 10], [11, 12]]
matrix2 = np.matrix(list2)

#Below Both lines are the same thing    
matrix3 = matrix1 * matrix2         
matrix4 = matrix1.dot(matrix2)      
print("\nMatrix 3:\n", matrix3, "\nMatrix 4:\n", matrix4)




