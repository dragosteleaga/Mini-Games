goodNumber=25
scor=100
print("Guess a number between 0 and 100")
x = int(input())

while x!=goodNumber :
    if (x<0 or x>100):
        scor-=10
        print("A number between 0 and 100 !! :(")
    elif x >= 30 and x<=100 :
        scor -= 5
        print("Your scor is = ", scor)
        print("Try lower")
    elif x<= 20 and x>=0:
        scor -= 5
        print("Your scor is = ", scor)
        print("Try higher")
    elif x==26 or x==24:
        scor -= 5
        print("Your scor is = ", scor)
        print("That is so close ! ")
    elif x>=20 and x<=24 :
        scor -= 5
        print("Your scor is = ", scor)
        print("Just a little bit higher")
    elif x>26 and x<30 :
        scor -= 5
        print("Your scor is = ", scor)
        print("Just a little bit lower")
    x = int(input())
    if (goodNumber == x):
        print("Good guess !")
        print("You win !")
        print("Your final scor is = ",scor)





