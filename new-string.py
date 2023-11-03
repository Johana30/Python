choice = 'Y'
#exe 1
# flag = True
# choice = 'Y'
# i = ''
# while choice == 'Y':
#     while flag == True:
#         word=input("type the word you want to check: ")
#         if word.isnumeric() == True :
#                 print(f"it is a number {word} \n")
#         else:
#             flag = False
#     word = word + ' '
#     print('-\n'.join((word.split(' '))))

#     choice = str(input("Continue ... y / n ")).upper()
#     if choice == 'N':
#         print("the program ends. Thanks")


#exe 2
# paragraph = "Argentina  wins   football   world cup 2022 in a nail biting final match that led to a       spectacular    penalty shootout. Football lovers   across the world   hailed   it as one of the most    memorable   matches."
# print(' '.join((paragraph.split())))


#exe3
# choice = 'Y'
# i=0
# word=''
# while choice == 'Y':
#     word=input("type the word you want to check: ")
#     word = (''.join((word.split())))
#     num=0
#     char=0
#     sym=0
#     for i in word:
#         if i.isdigit() == True:
#             num+=1
#         elif i.isalpha():
#             char+=1
#         else:
#             sym+=1

#     print(f"there are {num} digits, {char} letters, {sym} symbols")

#     choice = str(input("Continue ... y / n ")).upper()
#     if choice == 'N':
#         print("the program ends. Thanks")

# exe 4
# while choice == 'Y':
#     sentence = input("type a sentence: ").upper()
#     word=input("type the word to search: ")
#     s = word.upper()
#     if s in sentence:
#         print(f"the word {word} is included in the sentence")
#     else:
#         print(f"the word {word} is not included in the sentence")
#     choice = str(input("Continue ... y / n ")).upper()
#     if choice == 'N':
#         print("the program ends. Thanks")

#exe 5
# while choice == 'Y':
#     num = input("type a number: ")
#     word=input("type the word to search: ")
#     s = word.upper()
#     if s in sentence:
#         print(f"the word {word} is included in the sentence")
#     else:
#         print(f"the word {word} is not included in the sentence")
#     choice = str(input("Continue ... y / n ")).upper()
#     if choice == 'N':
#         print("the program ends. Thanks")

num = int(input("type a number: "))+1

for i in range(1,num):
    for y in range(1, i):
        print(i, y)
