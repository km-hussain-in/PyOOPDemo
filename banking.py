class InsufficientFunds (Exception):
  pass

class Account:
  
  def __init__(self, amount=0):
    self._balance = amount
    
  def balance(self): return self._balance
  
  def transfer(self, amount, other):
    if other is not self:
      self.withdraw(amount)
      other.deposit(amount)
  
class Profitable:
  
  def interest(self, period):
    rate = 3.5 if self._balance < 20000 else 4.5
    return self._balance * period * rate / 100

class CurrentAccount (Account):
  
  def deposit(self, amount):
    if self._balance < 0: amount *= 0.95
    self._balance += amount
  
  def withdraw(self, amount):
    self._balance -= amount
    
class SavingsAccount (Account, Profitable):
  
  MIN_BAL = 5000
  
  def __init__(self):
    Account.__init__(self, SavingsAccount.MIN_BAL)
  
  def deposit(self, amount):
    self._balance += amount
  
  def withdraw(self, amount):
    if self._balance < amount + SavingsAccount.MIN_BAL:
      raise InsufficientFunds
    self._balance -= amount
    
  
