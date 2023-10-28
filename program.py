import math

print ("**** menu ****\n", "1. + \n", "2. - \n", "3. / \n")
choice = int(input ("select one: "))

y = 1
number = 0
sum = 0

if choice == 1:
    x = int(input("how many number do you want to Sum? "))
    while y <= x:
        number = int(input ("type your "+ str(y) + " number: "))
        y+= 1
        sum = sum + number
elif choice == 2:
    x = int(input("how many number do you want to rest? "))
    while y <= x:
        number = int(input ("type your "+ str(y) + " number: "))
        y+= 1
        sum = sum - number
elif choice == 3:
    x = int(input(" number 1: "))
    number = int(input ("number 2: "))
    sum = x / number


print("the result of your calculation is: " + str(sum))