print ("Welcome to my quizz game !")

play =input("Do you want to play? ")

if play.lower()!="yes":
    print("Ok , bye!")
    quit()

print("Good choice !")
print()
print("Here is your fist question...")
scor=0


answer =input("In which continent is France situated? ")
if answer.lower()!="europe":
    print("Incorrect!")
else:
    print("Correct!")
    print("That was an easy one , unless you are from America :) ")
    scor+=1
print()
print("Second question...")

answer = input("What is the largest planet from Milky Way? ")
if answer.lower() != "jupiter":
    print("Incorrect!")
else:
    print("Correct!")
    print("Good job , I bet you like astrology!")
    scor += 1
print()
print("Third question...")

answer = input("Name the best-selling book series of the 21st century? ")
if answer.lower() != "harry potter":
    print("Incorrect!")
else:
    print("Magic!")
    print("That was correct !")
    scor += 1
print()
print("4th question...")

answer = input("Who invented the iconic Little Black Dress? ")
if answer.lower() != "coco chanel":
    print("Incorrect!")
else:
    print("Correct!")
    print("You're a real fashion killer ! ")
    scor += 1
print()
print("5th question...")
print("That is a hard one!")

answer = input("Norwegian artist Edvard Munch is famous for painting which iconic piece? ")
if answer.lower() != "the scream":
    print("Incorrect!")
else:
    print("Correct!")
    print("Pure art !  ")
    scor += 1
    print()
print("Well played ")
print("Your final scor is ",scor," out of 5 !")
print("That is ",scor/5*100,"%.")



