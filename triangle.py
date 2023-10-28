print ("                 **")
print ("                *****")
print ("             ***********")
print ("          *****************")
print ("       ***********************")
print ("     ***************************")
print ("   *******************************")
choice=1
while choice < 3:
    print ("")
    print ("**** menu ****\n", "1. perimeter of the triangle \n", "2. Area of the triangle \n", "3. exit \n")
    choice = int(input ("select one: "))


    y = 1
    x = 3
    type = "area"
    number = 0
    sum = 0

    if choice == 1:
        while y <= x:
            number = int(input ("type the "+ str(y) + " side: "))
            y+= 1
            sum = sum + number
            type = "perimeter"

    elif choice == 2:
            number = int(input ("type the hight of the triangle: "))
            sum = int(input ("type the base of the triangle: "))

            sum = sum * number / 2
            type = "area"
            
    elif choice == 3:
        print("the program ends. Thanks")
        exit()

    print ("********************** Result **********************")
    print("the " + type + " of the triangle is: " + str(int(sum)))
    print ("****************************************************")


#other way
#sp = perimeter/2
#a b c = side of the triangle
#area = math.sqrt(sp*((sp - a)*(sp - b)*(sp - c)))
