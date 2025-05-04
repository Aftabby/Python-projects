#Unit test is typically testing of unit of your code (functions) that you've written
# For Unit test there are lots of third party library and module,
# We're gonna use -- pytest -- for that
# We generally test our main_code from another Unit_test_code , by importing the function to that unit_test_code from main_code
#This the unit_test code

from CS50s_Unit_Test import square
import pytest


def test_square():
    assert square(2) == 4   # -- assert -- keyword shows AsertError if the later statement is false of the KW
    assert square(3) == 9
    assert square(-4) == 16
    assert square(0) == 0







#TO Check the error in the command line run -- pytest name_of_this_file  --
    #Pytest library runs all the function of the file and tests for errors
    # If you want you can create more function individully like for- positive numbers, negative numbers, and zeros - to check 
    # By creating more function you will get the idea where error is occurring 
    # Because pytest only give the idea about the first error
    
    
    #OR

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):  #In case for a particular input for the function of your main_code, should raise an error.
        square("cat")               #You can check the error, if it has been raised correctly by this method in -- pytest --





# For your information -- the square function in CS50_Unit_Test.py is returning addition not square
    # This mistake was done intentionally


