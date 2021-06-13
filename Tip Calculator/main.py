print("-" * 50)
print("\t Welcome to the tip calculator")
print("-" * 50)
Bill = float(input("What was the total bill? $"))
Tip = float(input("What percentage tip you would like to give? 10, 12 or 15? "))
Split = float(input("How many people to split the bill? "))

TipCalculation = (Bill * Tip) / 100
Total = Bill + TipCalculation
SplitBill = Total / Split

print(f"Each person should pay: ${SplitBill}")
