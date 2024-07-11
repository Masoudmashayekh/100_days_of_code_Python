#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

let_list = []
for i in range(1,nr_letters+1):
  let_list.append(random.choice(letters))               
# print(let_list)

sym_list = []
for i in range(1,nr_symbols+1):
  sym_list.append(random.choice(symbols))
# print(sym_list)

num_list = []
i = 0
for i in range(1,nr_numbers+1):
  num_list.append(random.choice(numbers))
# print(num_list)

password = []
password = let_list  + sym_list + num_list
target = nr_letters + nr_numbers + nr_symbols
# print(password)
combined_string = ''.join(map(str, password))
# print(combined_string)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(password)
combined_string = ''.join(map(str, password))

print(f"Your password is: {combined_string}")
