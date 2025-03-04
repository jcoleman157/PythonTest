
current_bal = 500
withdraw = eval(input("Enter an ammount to withdraw! "))
if withdraw > 500:
    print("Insufficient funds")
elif withdraw < 0:
    print("Please enter a positive number")
elif withdraw % 10 != 0:
    print("This ATM only dispenses multiples of 10")
else:
    current_bal -= withdraw
    print("new bal = ", current_bal)
