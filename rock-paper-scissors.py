import random

computer_wins=0
user_wins=0

options=["rock","paper","scissors"]

question=input("Do you want to play ? ")

if question.lower() !="yes":
    print("Good bye!")
    quit()

print("Whoever gets to 3 , wins!")
print()

while(computer_wins<3 and user_wins<3):
    user_pick=input("Pick Rock / Paper / Scissors ").lower()
    if user_pick not in options:
        continue

    random_number=random.randint(0,2)

    print("Computer picked",options[random_number]+".")
    computer_pick=options[random_number]

    if user_pick=="rock" and computer_pick=="scissors":
        print("You win!")
        print()
        user_wins+=1

    elif user_pick=="paper" and computer_pick=="rock":
        print("You win!")
        print()
        user_wins+=1

    elif user_pick=="scissors" and computer_pick=="paper":
        print("You win!")
        print()
        user_wins+=1

    elif user_pick==computer_pick:
        print("Draw")
        print()
        continue

    else:
        print("You lose")
        print()
        computer_wins+=1

if user_wins>computer_wins:
    print("Good job , you got 3 of them")
else:
    print("Computer wins the game !")
    print("Better luck next time!")
