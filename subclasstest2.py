from banking import *

def pay_annual_interest(accounts):
  for acc in accounts:
    if isinstance(acc, Profitable):
      amt = acc.interest(1)
      acc.deposit(amt)

jack = CurrentAccount()
jack.deposit(15000)
jill = SavingsAccount()
jill.deposit(10000)
try:
  payment = float(input('Amount to pay: '))
  if payment > 0:
    jill.transfer(payment, jack)
    print('Payment succeeded.')
except InsufficientFunds:
  print('Payment failed due to lack of funds!')
except Exception as ex:
  print('Error -', ex)

bank = {'Jack': jack, 'Jill': jill}
pay_annual_interest(bank.values())
for cust, acc in bank.items():
  print(f"{cust}'s balance is {acc.balance()}")




