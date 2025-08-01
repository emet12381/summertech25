#code by summertech. emet's original code was not saved

from random import randint

x = randint(1, 100)

guess = -1
tries = 0

while not guess == x:

 guess = int(input("Please enter a number between 1-100. "))
 tries += 1

 if guess > x:
   print("Too high! ", end = "")

 if guess < x:
   print("Too low! ", end = "")

 if tries == 7 and not guess == x:
   print("You're out of tries, you lose.")
   break
 elif not guess == x:
   print("Try again.")

if guess == x:
 print("You won!")

