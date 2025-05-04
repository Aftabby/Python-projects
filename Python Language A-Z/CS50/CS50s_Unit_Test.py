#Unit test is typically testing of unit of your code (functions) that you've written
# For Unit test there are lots of third party library and module,
# We're gonna use -- pytest -- for that
# We generally test our main_code from another Unit_test_code, by importing the function to that unit_test_code from main_code
#This the main_code

def main():
    x = int(input("What's X? "))
    print("X squared is", square(x))

def square(n):
    return n + n

if __name__ == "__main__":
    main()