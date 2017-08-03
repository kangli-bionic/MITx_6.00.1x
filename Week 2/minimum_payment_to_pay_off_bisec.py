balance = 999999
annualInterestRate = 0.18
min_payment_lower = balance/12
min_payment_upper = ((balance + balance * annualInterestRate/12)**12)/12
unpaid_balance = balance

while True:
    unpaid_balance = balance
    min_payment = (min_payment_lower + min_payment_upper)/2
    for i in range(12):
        unpaid_balance -= min_payment
        unpaid_balance += (unpaid_balance * annualInterestRate/12)
    if round(unpaid_balance, 2) == 0:
        break
    elif unpaid_balance > 0:
        min_payment_lower = min_payment
    else:
        min_payment_upper = min_payment

print('Lowest Payment: {:.2f}'.format(min_payment))
