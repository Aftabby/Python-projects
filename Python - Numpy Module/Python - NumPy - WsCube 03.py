import numpy as np

#Create numpy arrays with random numbers

# - rand()  - the function is used to generate a random value between 0 to 1
arr_rand = np.random.rand(4)       #The parameter takes shape of the array, here it is 1X4 , when you pass a single number, you don't need to mention 1, it automatically understands you want one row
print(arr_rand)

arr_rand1 = np.random.rand(3,5)     #it takes the parameter as the shape of the array, example: 3 x 5
print(arr_rand1, "\n\n")







# -  randn()  - the function is used to generate a random value close to zero, they may return positive or negative number as well
arr_randn = np.random.randn(5)  #The parameter takes shape of the array, here it is 1X5 , when you pass a single number, you don't need to mention 1, it automatically understands you want one row
print(arr_randn)

arr_randn1 = np.random.randn(4,5)   # it takes the parameter as the shape of the array, example: 4 x 5
print(arr_randn1, "\n\n")    











# -  ranf()  - the funcion for doing random sampling in numpy. It returns an array of specific shape and fills it  with random floats in the range of  [0.0, 1.0) - that is  1 not included
arr_ranf = np.random.ranf(4)    #The parameter takes shape of the array, here it is 1X4 , when you pass a single number, you don't need to mention 1, it automatically understands you want one row
print(arr_ranf)

arr_ranf1 = np.random.ranf((5,3)) # it takes the parameter as the shape of the array, example: 5 X 3, and takes the shape as atuple
print(arr_ranf1, "\n\n")








# -  randint()  - the funcion is used to generate a random number between a given range
                # - the parameters of this function is -- randint(min, max, shape_of_matrix)

arr_randint = np.random.randint(5, 20, 3)      #This function will generate numbers between 5 to 20 (min and max range) and the shape of the matrix will be 1X3
print(arr_randint)


arr_randint1 = np.random.randint(10, 30, (4,5)) #This function will generate numbers between 10 to 30 (min and max range) and the shape of the matrix will be 4X5
print(arr_randint1)








#Important NOtes:
# SOme function takes the shape of the array as parameter, be careful different function takes it different way, 
    #some as a tuple -- (2, 3) -- some as list -- [2, 3] -- some as another parameter --  2, 3  --