logo = '''
   ______                                 _________  __              ____  _____                       __                       
 .' ___  |                               |  _   _  |[  |            |_   \|_   _|                     [  |                      
/ .'   \_| __   _   .---.  .--.   .--.   |_/ | | \_| | |--.  .---.    |   \ | |  __   _   _ .--..--.   | |.--.   .---.  _ .--.  
| |   ____[  | | | / /__\\( (`\] ( (`\]      | |     | .-. |/ /__\\   | |\ \| | [  | | | [ `.-. .-. |  | '/'`\ \/ /__\\[ `/'`\] 
\ `.___]  || \_/ |,| \__., `'.'.  `'.'.     _| |_    | | | || \__.,  _| |_\   |_ | \_/ |, | | | | | |  |  \__/ || \__., | |     
 `._____.' '.__.'_/ '.__.'[\__) )[\__) )   |_____|  [___]|__]'.__.' |_____|\____|'.__.'_/[___||__||__][__;.__.'  '.__.'[___]    
'''

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
import random
number = random.randint(1,100)
print(f"The correct answer is {number}")
# -------------------------------------------------------------------------------------------
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")
if difficulty == "easy":
  i = 10
  print("You have 10 attempts remaining to guess the number.")
elif difficulty == "hard":
  i = 5
  print("You have 5 attempts remaining to guess the number.")
# -------------------------------------------------------------------------------------------
while i > 0 :
  guess = int(input("Make a guess: "))
  if guess == number:
    print(f"You got it! The answer was {number}.")
    break
  elif guess > number:
    print("Too high.") 
    print("Guess again.")
  elif guess < number:
      print("Too low.")
      print("Guess again.")
  i -= 1
  print(f"You have {i} attempts remaining to guess the number.")
  if i == 0:
    print("You've run out of guesses, you lose.")
    break

# -------------------------------------------------------------------------------------------
