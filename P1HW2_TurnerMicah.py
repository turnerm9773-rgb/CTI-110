# Micah Turner
# 11/13/2025
# P1HW2_TurnerMicah.py
# This program performs multiplication, exponentiation, addition, and subtraction based on user input.

print("Enter Your Budget Calculations Below!: $1200" )
print("Enter your travel destination: Nashville")
print("Enter the amount you plan to spend on gas: $250" )
print("Enter the amount you plan to spend on accomadations: $600")
print("Enter the amount you plan to spend on food: $300")


print("------Travel Expenses------")
Location = "Nashville"
Budget = 1200
Gas_Expense = 250
Accommodations_Expense = 600
Food_Expense = 300

Remaining_Balance = Budget - (Gas_Expense + Accommodations_Expense + Food_Expense)  

print("Your remaining balance after your trip to", Location, "is $", Remaining_Balance, "!!")
