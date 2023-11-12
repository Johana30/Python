import random
choice = 'Y'
def select ():
    user_op = input("Enter rock, paper, or scissors: ").lower()
    while user_op not in ["rock", "paper", "scissors"]:
        user_op = input("wrong option \n please type rock, paper, or scissors: ").lower()

    return user_op

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"
 
while choice == 'Y':
    userop = select()
    pcop=random.choice(["rock", "paper", "scissors"])
    print(f"pc choice is: {pcop}\n", winner(userop, pcop))

    choice = str(input("Continue ... y / n ")).upper()
    if choice == 'N':
        print("the program ends. Thanks")