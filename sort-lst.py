# Create a program based on the binary search algorithm.
# The program should take a list as the number to be found in such list as inputs and returns the index with the position of such number in the (sorted) list.
# Ex			lst = [0, 34, 56, 2, 4, 9, 78]
# 			num = 56
# Output:
# 		“The number 56 is included in the list in position 5”

def select ():
    num = input("Search number: ")
    while num.isdigit() == False:
        num = input("wrong option \n please type a number: ")
    return int(num)

def looking(lst_looking, po):
	try:
		position = lst_looking.index(po)
	except ValueError:
		position = 0
	return position


lst = [0, 34, 56, 2, 4, 9, 78]
lst.sort()
p = select()

if looking (lst, p) == 0:
	print("the number is not in the list")
else:
	print(f"the number is in position {looking (lst, p)}")