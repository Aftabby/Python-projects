import numpy as np

#Matrix Functions in NumPy Arrays (Transpose, Swapaxes, Inverse, Power, Determinant)

list1 = [[1, 2, 3], [4, 5, 6]]
matrix1 = np.matrix(list1)
print("Matrix:\n", matrix1)



# ===  Transpose  ===
                # In transpose the row becomes the column and the column becomes the row
#Below both lines are same
transpose_matrix1 = np.transpose(matrix1)        #You can also transpose a matrix by -- matrix_name.T  ---
transpose_matrix2 = matrix1.T       # Here -- T -- is a variable name of the np.matrix class
print(transpose_matrix1)
print(transpose_matrix2)








# === Swapaxes  ===
                # Swapaxes, swaps the axes of a matrix, that row to colum and column to row or vice versa
swapaxes_matrix1 = np.swapaxes(matrix1, 0, 1)   # here the -- 0 axis -- of the matrix would be changed to -- 1 axis -- np.swapaxes(matrix_name, the_axis_to_be_change, to_the_new_axis_value)
print(swapaxes_matrix1)














# ===  Inverse Matrix  ====
list2 = [[10, 11], [12, 13]]
matrix2 = np.matrix(list2)

inverse_matrix = np.linalg.inv(matrix2)         # linalg is the short form of linear algebra
print(inverse_matrix)










# === Power of Matrix ===
                # that is, if A is a matrix then, A^2 = A.A  <- which is a dot multiplication
                # -- np.linalg.matrix_power(array, n)  --- here - n - is the value of power, (array to power n), n could be of three types (n<0 , n=0, n>0)
                # For n=0 , the matrix become the Identity matrix
                # For n>0 , the power will be applied to the matrix with dot multiplication
                # For n<0 , the power is applied on the inverse of that matrix i.e. (A^(-1*n))          #which is a common sense, simple mathematics


power_matrix1 = np.linalg.matrix_power(matrix2, 2)          # Here n>0
print(power_matrix1)

power_matrix2 = np.linalg.matrix_power(matrix2, 0)          # Here n=0
print(power_matrix2)

power_matrix3 = np.linalg.matrix_power(matrix2, -2)
print(power_matrix3)
















#  ====  Determinant of Matrix  ===== 
                            # if A is a matrix, in mathematics of linear algebra determinant is |A|

det_matrix = np.linalg.det(matrix2)
print(det_matrix)








