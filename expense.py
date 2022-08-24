"""simple expenses calc"""
# expenses = [10.50,8,5,15,20,5,3]
# TOTAL = sum(expenses)

# print ("You spent $", TOTAL, " on lunch this week", sep = '')

TOTAL = 0
expenses = []
num_expenses = int(input("How many receipts are you submitting? "))

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

TOTAL = sum(expenses)

print("You spent $", TOTAL, sep="")
