a = 0
b = 0

#validating if user is inputting the correct value
try:
    #Get input from the user
    a = int(input("What is your first number: "))
    b = int(input("What is your second number: "))

    #Calculating if A or B is the bigger number
    if a > b:
        print(a, "Is bigger then", b)
    elif b > a:
        print(b, "Is bigger the", a)
    else:
        print("The both numbers are the same")
except (NameError, ValueError) as error:
    print("Please enter a valid input as a number")
