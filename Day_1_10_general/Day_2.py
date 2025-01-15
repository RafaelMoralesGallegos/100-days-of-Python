print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

if percentage == 10 or percentage == 12 or percentage == 15:
    # tip = round((bill*(1+percentage/100))/people,2)
    tip = "{:.2f}".format((bill * (1 + percentage / 100)) / people)
    print(f"Each person should pay: ${tip}")
else:
    print("Please run format again")
