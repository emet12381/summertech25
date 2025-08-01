#code by summertech. emet's original code was not saved


from random import randint

repeat = True

while repeat == True:

 #Let rock => 0, scissors => 1, paper => 2
 computer = randint(0, 2)

 player = input("Enter [R]ock, [P]aper, or [S]cissors! ")

 if computer == 0:
  
   if player == "R":
     print("It's a tie! Go again.")

   elif player == "P":
     print("You win!")
     repeat = False

   else:
     print("You lost! Go again.")

 if computer == 1:

   if player == "S":
     print("It's a tie! Go again.")
  
   elif player == "R":
     print("You win!")
     repeat = False

   else:
     print("You lost! Go again.")

 if computer == 2:

   if player == "P":
     print("It's a tie! Go again.")
  
   elif player == "S":
     print("You win!")
     repeat = False

   else:
     print("You lost! Go again.")
