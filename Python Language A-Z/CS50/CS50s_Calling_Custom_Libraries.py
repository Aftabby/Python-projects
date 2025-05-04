import sys
from CS50s_Custom_Libraries import hello, goodbye #Calling my own code (library) from the same directory file

if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])

