print("Welcome to the tip calculator")
total_bill =float(input("Give the total of the bill: "))
tip = int(input("How many tip would you like to give? 5, 10 or 15?: "))
people = int(input("How many people are spliting the total of the bill with tip: "))
Total_tip = ( total_bill * tip/100)/people
Total = round (Total_tip,2)
print(f"Everyone shloud pay ${Total}")
