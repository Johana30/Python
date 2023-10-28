from random import randint
i = 0
x = 10
ad=0
value = 0
choice = 'None'
print("******* Adivina el numero between 0 to 10 ***********")
while choice != 'y' or choice != 'Y':
    i = 5
    x = 10
    ad = 0
    value = 0
    choice = str(input("do you want to change the hight number? y or n \n"))
    if choice == 'y' or choice == 'Y':
        x=input("type new hight number: \n")
        if x.isdigit():
            value = randint(0, int(x))
            print(value)
        else:
            print("it is not a number")
    while i > 0: 
        print("you have " + str(i) + " intentos")
        ad = input("teclea el numero que estas pensando: \n")
        if ad.isdigit(): 
            if int(ad) == value:
                print("WINNER")
                i = -1
            else:
                i = i - 1
        if i == 0:
            print("you lose")
    choice = str(input("do you want to exit? y or n \n"))
    if choice == 'Y' or choice == 'y':
        print("the program ends. Thanks")
        exit()            