# ==========================   ITERATORS   ==================================

# An object that can be iterated upon, using various types of loops in python, and will return data, one element at a time, is called iterators (example: list , tuple)
# To make your custom iterator -- object --, you have to create two extra special methods while creating -- class -- from which you will create the object

# 1. ---    __iter__()    --- Each iterator class should have the __iter__() method. It is the initialization of an iterator (Just like we use __init__() to initialize an object). It returns an iterator object
# 2. ---   __next__()       ----  An iterator class should have a __next__() method. This method is basically used to go on to the next element in a sequence and iterate over an iterator. It returns the next value for the iterable. 

# A python iterator object must implement two special methods , __iter__(), __next() -- collectively called the iterator protocol. 

# How does it work?
# When we use the a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object,
# Which further uses the next() method to iterate over.
# When we reach the end and there is no more data to be returned, it will raise the StopIteration exception



#Below there is a demo of how a for loop works with your iterable object:
'''
iterable_value = "Programming Hero"
iterable_obj = __iter__(iterable_value)

while True:
    try:
        item = __next__(iterable_obj)
        print(item)
    except StopIteration:
        break

'''




# An example of creating an iterator object---- range() works something like this in a for loop

class Data:
    def __init__(self, limit):          # Step 1
        self.limit = limit

    def __iter__(self):                 # Step 2
        self.value = 0                                     # __iter__ method returns the iterator object
        return self
    
    def __next__(self):                 # Step 3 
        x = self.value
        if x >= self.limit:      #When it reached the end value
            raise StopIteration
        else:
            self.value = x+1
            return x


for i in Data(10):
    print(i)

# Strings, Lists, Sets, Tuples etc are built-in iterators in Python.

# Recap : Implement a class with __iter__() method and __next__() method, 
    #keep track of the internal states, and raise StopIteration when there are no values to be returned