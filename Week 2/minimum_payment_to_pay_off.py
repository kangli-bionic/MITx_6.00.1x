balance = 3926
annualInterestRate = 0.2
min_payment = 0
unpaid_balance = balance

while unpaid_balance > 0:
    unpaid_balance = balance
    min_payment += 10
    for i in range(12):
        unpaid_balance -= min_payment
        unpaid_balance += (unpaid_balance * annualInterestRate/12)
    print(min_payment, unpaid_balance)

print(unpaid_balance)
print('Lowest Payment: {}'.format(min_payment))
