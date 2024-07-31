from art import logo, vs
from game_data import data
from replit import clear
import random
# ----------------------------------------------------------------------------------------
def format_data(account):
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"
# ----------------------------------------------------------------------------------------
def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
# ----------------------------------------------------------------------------------------
print(logo)
score = 0
# ----------------------------------------------------------------------------------------
account_B = random.choice(data)
game_should_continue = True
while game_should_continue:
  account_A = account_B
  account_B = random.choice(data)
  if account_A == account_B:
    account_B = random.choice(data)
  # ----------------------------------------------------------------------------------------
  print(f"Compare A: {format_data(account_A)}.")
  print(vs)
  print(f"Compare B: {format_data(account_B)}.")
  # ----------------------------------------------------------------------------------------
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  # ----------------------------------------------------------------------------------------
  a_follower_count = account_A["follower_count"]
  b_follower_count = account_B["follower_count"]
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  clear()
  print(logo)
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")
    
    
