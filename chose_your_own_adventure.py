answer=input("Hello , do you want to play? ")
if answer.lower() !="yes":
    print("Ok , bye!")
    quit()

name=input("What is yout name? ")
print("Hello",name,"you wake up on an island and start walking on a dirty road ,it is 1 AM in early october and it is raining, the road comes to an end and you can go right or left")
answer=input("Which way will you go?(right/left) ")
if answer=="right":
    print("You walk for 20 minutes and you come across a bride.You can pay 10$ to cross the bridge or you can swim (swim/pay)")
    answer=input("What do you do? ")
    if answer=="swim":
        print("There was an aligator in the water and now you are dead :( ")
    elif answer=="pay":
        print("You succesfully crossed the brige and at the end of it you've met a strange man dressed all in purple.")
        answer=input("Do you talk to him or you continue the road (talk/continue)? ")
        if answer=="talk":
            print("He was your lost brother and he saved you! ")
            print("You win!")
        elif answer=="continue":
            print("He got offended and killed you! ")
        else:
            print("You lost")

elif answer=="left":
    print("You see a strange wire")
    answer=input("Do you pull it?(yes/no) ")
    if answer=="yes":
        print("Yout activated an alarm and someone will come and rescue you! ")
        print("You win!")
    elif answer=="no":
        print("You keep waking and after 20 minutes you meet a strange man dressed all in purple.")
        answer=input("Do you talk to him? (talk/continue) ")
        if answer=="talk":
            print("He was your lost brother and he saved you! ")
            print("You win!")
        elif answer=="continue":
            print("He got offended and killed you! ")
        else:
            print("You lost")

    else:
        print("You lost")


else:
    print("You lost :( ")

