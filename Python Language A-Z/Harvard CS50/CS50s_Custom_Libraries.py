def main():
    hello("World")
    goodbye("Earth")

def hello(name):
    print(f"hello {name}")


def goodbye(name):
    print(f"goodbye {name}")


if __name__ == "__main__": #This (name) is a very special variable of python, it gets equal to "__main__", when you run the program from command line, not by calling as a library to another file
    main()                  # And thus the code will not get trigerred while using it as a module to another file




# Important NOte: If you program anything outside of a function
    # while importing the file to another file, the codes will run by default,
    # Becuase at first python read the library/module fully so all the codes gets executed
    # To avoid this put main code in main function
    # If needed call -- main() -- from below
    # Or you can call main() the way I called inside a condition
    # --  __name__=="main"  -- gets only True, when you run this file directly, not when you import it to another file