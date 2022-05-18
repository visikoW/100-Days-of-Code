# introduction to the bill calculator interface
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
total_people = int(input("How many people to split the bill? "))
tip = int(input("What percenentage tip would you like to give? 10, 12, or 15? "))

# processing datas: bill per person
per_person_bill = total_bill / total_people
per_person_tip = total_bill * (tip/100)/ total_people

# calculate my total valor
dollars = round(per_person_bill + per_person_tip)

# printing te final code
print(f"Each Person should pay: ${dollars:.2f}")
