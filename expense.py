# expenses = [10.50,8,5,15,20,5,3]
# total = sum(expenses)

# print ("You spent $", total, " on lunch this week", sep = '')

total = 0
expenses = []
num_expenses = int(input("How many receipts are you submitting? "))

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print("You spent $", total, sep="")
