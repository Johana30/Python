choice = 'None'
print("do you want ot know your grade! ")
while choice != 'y' or choice != 'Y':
    try:
        #Get input from the user
        
        grade = int(input("enter your grade: \n"))
        if grade  >= 90:
            print("You got a A")
        elif grade  >= 80:
            print("You got a B")
        elif grade  >= 70:
            print("You got a C")
        elif grade  >= 60:
            print("You got a D")
        else:
            print("You got an F")

    except (NameError, ValueError) as error:
        print("Please enter a valid input ")

    choice = str(input("do you want to exit? y or n \n"))
    if choice == 'y' or choice == 'Y':
            print("the program ends. Thanks")
            exit()
