# Calculator
from art import logo
 # Add
def add(number_1,number_2):
  return number_1 + number_2

# Subtract
def subtract(number_1,number_2):
  return number_1 - number_2

# Multiply
def multiply(number_1,number_2):
  return number_1 * number_2

# Divide
def divide(number_1,number_2):
  return number_1 / number_2

# Dictionaries
operations = {
  "+": add, 
  "-": subtract,
  "*": multiply,
  "/": divide}

def caulculator():
  print(logo)
  number_1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation:")
    number_2 = float(input("What's the next number?: "))
    calcuation_function = operations[operation_symbol]
    answer = calcuation_function(number_1,number_2)
    
    print(f"{number_1} {operation_symbol} {number_2} = {answer}")
    
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") =="y":
      number_1 = answer
    else:
      should_continue = False
      caulculator()

caulculator()
