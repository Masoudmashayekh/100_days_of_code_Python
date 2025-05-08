rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
pc_choice = random.randint(0,2)
print("Welcome to Rock, Paper, Scissors!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if 0 <= user_choice <= 2:
    if user_choice == 0:
        if pc_choice == 0:
            print(f"You chose: {rock}\nComputer chose: {rock}" + "\nIt's a draw!")
        elif pc_choice == 1:
            print(f"You chose: {rock}\nComputer chose: {paper}" + "\nYou lose!")
        else:
            print(f"You chose: {rock}\nComputer chose: {scissors}" + "\nYou win!")
        
    if user_choice == 1:
        if pc_choice == 1:
            print(f"You chose: {paper}\nComputer chose: {paper}" + "\nIt's a draw!")
        elif pc_choice == 0:
            print(f"You chose: {paper}\nComputer chose: {rock}" + "\nYou win!")
        else:
            print(f"You chose: {paper}\nComputer chose: {scissors}" + "\nYou lose!")

    if user_choice == 2:
        if pc_choice == 1:
           print(f"You chose: {scissors}\nComputer chose: {paper}" + "\nYou win!")
        elif pc_choice == 0:
             print(f"You chose: {scissors}\nComputer chose: {rock}" + "\nYou lose!")
        else:
            print(f"You chose: {scissors}\nComputer chose: {scissors}" + "\nIt's a draw!")

else:
    print("You lose Cheater!")
    

