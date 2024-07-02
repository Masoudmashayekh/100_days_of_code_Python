print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_cal = tip/100
total_tip_amount = bill * tip_cal
total_bill_amount = bill + total_tip_amount
bill_per_person = total_bill_amount / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: $ {final_amount}")
