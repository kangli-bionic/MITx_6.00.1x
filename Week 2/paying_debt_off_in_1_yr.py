for i in range(12):
    balance = balance + (annualInterestRate/12.0 * balance)
    balance = balance - (monthlyPaymentRate * balance)

print('Remaining balance: {.2f}'.format(balance))
