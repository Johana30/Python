# Binary search is a searching algorithm that efficiently finds the position of a target value within a sorted array. 
#The idea behind binary search is to repeatedly divide the search interval in half. 
#If the value of the search key is less than the item in the middle of the interval, 
#then the search space is halved by ignoring the right half. If the key is greater, 
#then the left half is ignored. The process continues until the target is found or the search interval becomes empty.

import random

def select ():
    num = input("Search number: ")
    while num.isdigit() == False:
        num = input("which number do you want to check")
    return int(num)

def binary(lst_num, target):
    low, high = 0, len(lst_num) - 1
    lst_num.sort()
    while low <= high:
        mid = (low + high) // 2  # Calculate the midpoint
        #print(f"low {low}, high {high}")
        if lst_num[mid] == target:
            return mid  # Target found, return its index
        elif lst_num[mid] < target:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half

    return -1  # Target not found in the array


lst_num = [random.randint(1,100) for x in range(20)]
#print(f"The List of numbres are: {lst_num}, \n")

print("the list content 20 numbers, between 1 to 100, \n")
n = select()

if binary(lst_num, n) == -1:
    print("the number is not in the list")
else:
    print(f"the number is position {binary(lst_num, n)}")
