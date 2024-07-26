print("Welcome to the tip calculator.")  

payment=input("How much is the total bill in dollars? ")
payment=float(payment)
tip=input("How much tip do you want to give? 10, 12, or 15? ")
tip=int(tip)
Numberofpeople=input("How many people are splitting the bill?")
Numberofpeople=int(Numberofpeople)

payperperson=(payment*(tip/100)+payment)/Numberofpeople
payperperson=round(payperperson,2)
print(f"Each person should pay {payperperson} dollars")
