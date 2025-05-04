#Data Structure
# 1. Stores more than one data
# 2. Special Structure to store data
# 3. Specific rule to add or remove data
# Data structure is used to organize data
# Examples: List, Dictionary, Linked List
# If follows, LIFO policy - is called STACK, else if follows FIFO policy - is called QUEUE. (LIFO : Last In First Out, FIFO : First In First Out)
# Dictionary type data structure contains key:value pair
# Linked list - node use pointers to link with each other















#Graph - Data Structure
# When multiple nodes are connected with each other, two way/ or one way (via edges) is called graph
# Directed Graph - When in a graph, nodes connection (edge) have direction like one way only, is called directed graph
# Element is called nodes, connection / pointer is called edges
# Storing Data using graph structure is - Graph data structure - Google map uses graph data structure












#Tree Data Structure
# Every element of the tree DS is called node
# The topmost or starting node is called root
# Any node connected under a node is called the child node of the upper node
# Similarly, any node connected on the upward node, direct upward node is called parent node of the node under it
# Those nodes that don't have any child is called leaves
# There are thousands type of tree DS - popular 4 are - 1. Tree (general kind) - 2. Binary Tree - 3. Binary search tree - 4. Heap

#Binary Tree - is a special kind of tree - a node can have maximum of two child nodes
#Binary Search Tree (BST) - The value of the left child will be smaller than parent node value, and the value of right child will be higher than the value of parent node
#Max Heap - When the value of any parent node is higher or equal to any child node, the tree is called Max Heap.
#Min Heap - When the value of any parent node is lower or equal to any child node the tree is called Min Heap


# To add a node - there is a function - which takes two parameter (data, and parent) - it finds parent, create a new node and set as a child
# Two approach to search a node - 1. Breadth First Search (row priotized) - 2. Depth First Search (column priotized)








#Linked List
# List with items/nodes connected with chain (pointers)
# Item in a list is called element, but item in a linked list is called node
# Every node contains one or two pointers to the next/previous/both-side nodes
# Linked List are of two types - Singly [One way direction - one pointer in nodes, head to tail] -- Doubly [ Two way direction - two pointers (right & left pointers) - head to tail & tail to head]
# Special case : IN some cases tail node (last) point to the head node (first) - it's called circular linked list








#Tuples (Does not fall under data structure)
# It is immutable like string, once declared you can't change any particular element of it, that's why it doesn't considered under data structure.
# It is a list of value grouped together


#Declaring Tuples
points = (54, 22, 1, 67, 33, 65)
print(points[0])        #Accessing tuples is just like list

# point[2] = 91    #It will give an error as tuples are immutable











#Declaring a dictionary

best_duo = {"Virat" : False, 34 : 48} # -- dictionary_name = {key1:value1, key2:value2, ...}  --- that's how to declare a dictionary
print(best_duo["Virat"])    #Accessing dictionary element's value by key

any = best_duo[34]          #You can access any value in the dictionary by its key --- dictionary_name[key]  --
print(any)                #To know more read important notes below

best_duo["Tahsan"] = "Mithila"   #Adding element in dictionary --- dictionary_name[new_key] = new_value  ---
print(best_duo["Tahsan"])


print(best_duo)      #Printing the whole dictionary

best_duo["Tahsan"] = "Single"  # Update element of dictionary
print(best_duo["Tahsan"])

del best_duo[34]  # delete element(key:value pair) in dictionary
print(best_duo)

if "Virat" in best_duo:   # Check the key exists or not, if the key is in that dictionary it returns True, otherwise False
    print("Found it!")          #Though the value of key "Virat" is False, but it returns True, because it is not returning the value of the key in the dictionary, it is returning if the key is present in the dictionary or not
    print("Virat" in best_duo, "\n\n")

print("Hello" in  best_duo)    #It will return false, as the key "Hello" is not present at the dictionary

best_duo["Virat"] = "Anushka"

player_rating = { "Ronaldo" : 9.5, "Messi" : 7.8, "Shakib Al Hasan" : 6.8}
all_players = player_rating.keys()  #To get all the keys of a dictionary use keys() method -- dictionary_name.keys()  --- return data type 'dictionary keys'
print(all_players, type(all_players))

all_players = list(all_players)       # Converting all the keys of dictionary into a -- list -- object from a  --dictionary_keys -- object
print(all_players, type(all_players), "\n\n")


all_ratings = player_rating.values() # Similarly, to get all the values of a dictionary use -- dictionary_name.values() -- method
print(all_ratings, type(all_ratings))

all_ratings = list(all_ratings)     # Converting all the keys of dictionary into a -- list -- object from a  --dictionary_keys -- object
print(all_ratings, "\n\n") 

for key_name in player_rating:        #Iterating over the whole dictionary
    print(key_name, type(key_name))   # here the loop_variable is each of the key in each iteration
    
    rating = player_rating[key_name]  # Assigning the dictionary value for every key in a variable
    print(rating, type(rating))


for key_name, value in player_rating.items():   #This --dictionary_name.items()-- method will return both key and value pass
    print(f'Key: {key_name} and the Value: {value}')


dictt = { "key1" : "value1", "key2" : "value2", "key3" : "value3"}
print(dictt)

dictt.clear()   #This method will clear the whole dictionary and the dictionary will be empty, but not deleted
print(dictt)











#Queue
queue = []
queue.append("Hello")   # append is used to insert data in list
queue.append("How")
queue.append("are")
queue.append("you")

print(queue)

queue.pop(0)   #First in First out - FIFO, pop method removes the last element of the list and returns it, if no parameter is passed. But if you pass an index, only the value of that index will be removed and will return the value.
print(queue)         #Here we are removing the first element of the list by index 0


#Priority Queue
# If a queue is  designed such a way to give higher priority to a special type of elements, that queue is called priority queue






#Stack
stack = []

stack.append("Hello")
stack.append("How")
stack.append("are")
stack.append("you")

print(stack)

stack.pop()   #Last in First out - LIFO

print(stack)











#Important Notes
# Strings and tuples are immutable, while lists, dictionaries and sets are mutable.
# Stack is like a pile of clothes you wear in winter, Last in First out - LIFO
# Queue is like a line of people buying tickets from counter, First in First out - FIFO
# If a queue is  designed such a way to give higher priority to a special type of elements, that queue is called priority queue
# A dictionary is like a couple, to declare a dictionary -- dictionary_name = {"Key" : "Value", "key1" : "value2"}   ------- key and value can be of any data type (numeric, string, boolean, object, any_data_structure)
# To access a dictionary element's Value ---  print(dictionary_name["Key"]) ----
# To access an item in list we need to know index, but for dictionary we need to know the key of the value. Actual index position doesn't matter in dictionary 
# To update or add any element in dictionary --- dictionary_name["Key"] = "Value"  ---- Key and value can be of any data type
# To delete any element dectionary, use the KW del --- del dictionary_name["Key"]  --- The particular key:value pair will be removed from dictionary
# Same as -- element_name in list_name -- gives us True or False, we can use --- "key" in dictionary_name --- will give us True if that key exist in that dictionary, otherwise False
# To get all the keys of a dictionary use keys() method -- dictionary_name.keys()  --- return data type 'dictionary keys'
# Similarly, to get all the values of a dictionary use -- dictionary_name.values() -- method
# To convert all the keys of a dictionary into a list use --- list(dictionary_name.keys()) ----- 
# To use iteration -- for loop_variable in dictionary_name:  --- here the loop_variable will be the key_name, and will be iterate through every element's key_name
# In a list, every element is independent, in a linked list every element is connected
# Item in a list is called element, but item in a linked list is called node

#Linked List and Tree Data Structure, Graph explained above
