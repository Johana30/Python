flag = True
choice = 'Y'
i = 0
while choice == 'Y':
    while flag == True:
        word=input("type the word you want to check: ")
        if word.isnumeric() == True :
                print(f"it is a number {word} \n")
        else:
            flag = False
    char = 0
    for i in range(len(word)- 1,-1,-1):          
        if word[i] != word[char]:
            i=len(word)
        char+=1 
        i+=1
    if i == len(word)+1:
        print("it is not polindrome")
    else:
        print(f"({word}) is a polindrome ")
    choice = str(input("Continue ... y / n ")).upper()
    if choice == 'N':
        print("the program ends. Thanks")