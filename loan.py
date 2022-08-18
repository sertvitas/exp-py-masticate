# get loan details

principal = float(input("How much principal is outstanding?\n")) # 50,000
apr = float(input("What's the apr?\n")) # 3%
payment = float(input("What's your monthly payment? \n")) #1,000
months = int(input("How many months do you want to see results for?\n")) #24

# Divide apr by 100, to make a decimal, then by 12 for the monthly rate of accrual.

monthly_rate = apr/100/12

for i in range(months):
    
    #add in interest

    interest = principal * monthly_rate
    principal = principal + interest

    if (principal - payment <0):
        print("The last payment is",principal)
        print("You paid off the loan in",i+1,"months")
        break

    #make payment

    principal = principal - payment

    #print results after this month

    print("Paid",payment, "of which",interest,"was interest.",end=' ')
    print("Now I owe",principal)



