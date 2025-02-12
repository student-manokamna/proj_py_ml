
print("welcome to the tip Calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("how many people to split the bill? "))
total_bill = float((bill*(tip/100))+bill)

bill_per_person= total_bill/people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
print(f"Thank you for using the tip calculator!")