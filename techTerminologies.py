print("Welcome to my game")

playing=input("Do you enjoy my game? ")

if playing.lower() !="yes":
   quit()

print("Okay! Let's do it baby")
score = 0
question = input("What does WWW stands for?  ")
if question == "World Wide Web":
   print("That's it girl/boy!")
else:
   print("Try again girl!")
score +=1
print("You scored " + str(score) + " questions baby!")
print("You scored " + str((score/2)*100) + "%.")


    

