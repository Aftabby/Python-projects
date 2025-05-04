#Insertion Sort
def insertion_sort(list1):
    n = len(list1)
    for i in range(1, n):
        j = i - 1
        insert = list1[i]
        while insert < list1[j] and j >= 0:
            list1[j+1] = list[j]
            j -= 1
            list1[j+1] = insert
    return list1






#Selection Sort - Practical
def selection_sort(list1):
    n = len(list1)

    for i in range(n):
        for j in range(i+1, n):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
    return list1










#Bubble Sort - Practical
def bubble_sort(list1):
    n = len(list1)
    for i in range(n):
        for j in range(n-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j + 1], list1[j]
    
    return list1


list1 = [5, 10, 55, 109, 65, 2, 66, 47, 3, 58, 3, 12]
list1 = bubble_sort(list1)
print(list1)

list1 = [5, 10, 55, 109, 65, 2, 66, 47, 3, 58, 3, 12]
list1 = selection_sort(list1)
print("Selection Sort", list1)

list1 = [5, 10, 55, 109, 2, 66, 47, 3, 58, 3, 12, 35]
list1 = insertion_sort(list1)
print("Insertion Sort", list1)








#Shortcuts
a, b = 5, 3     #Shortcut way to declare multiple variables together
print(a, b)

a, b = b, a     #Shortcut way to swap variable
print(a, b) 

any_list = [0, 1, 2, 3, 4]
print(any_list[0], any_list[1])

any_list[0], any_list[1] = any_list[1], any_list[0]     #Swapping the element of list, as lists are mutable
print(any_list[0], any_list[1])





#Insertion Sort - Theory
# For each position, loop the elements on the right, Take an element and keep going from that element to the left side
# If the element is bigger than the selected element, keep going to the left.
# Once the next element is not smaller or you reached the leftmost position, insert the element.
# Repost steps 1 to 4











#Selection Sort - Theory
# For each position, loop the elements on the right
# Find the minimum numbers on the right
# Swap these two elements (Bring the min element to the current position and send the current element to the min element position)
# Repeat the above steps












#Bubble Sort - Theory
# Compare two adjacent elements, If the first item is bigger than the second then swap it
# Run the loop for n-1 iems
# Keep doing it for all the elements




#Advanced Sorting
# Google and learn about Merge Sorting, Quick Sorting, Heap Sorting






#Important Notes
# Google and learn -- Greedy Algorithm, Backtracking Algorithm, Branch and Bound Algorithm, Brute Force Algorithms, Heuristic ALgorithm etc.
