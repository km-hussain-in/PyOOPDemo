class SealedMeta(type):
  
  def __new__(cls, name, bases, dct):
    if len(bases) > 0:
      raise TypeError(f'{name} cannot extend a sealed class: {bases[0].__name__}')
    return super(SealedMeta, cls).__new__(cls, name, bases, dct)
    
class NonInheritableClass(metaclass=SealedMeta): pass

#this will cause error - cannot extend a sealed class
#class ProblematicClass(NonInheritableClass): pass

#module for supporting an abstract base class(ABC)
from abc import * 

class TaxPayer(metaclass=ABCMeta):

  @abstractmethod
  def annual_income(self): pass
  
  def __init__(self, age):
    self.__age = age
    
  def income_tax(self):
    rate = 0.15 if self.__age < 60 else 0.12
    amount = self.annual_income() - 200000
    return rate * amount if amount > 0 else 0
  
class Employee(TaxPayer):
  
  def __init__(self, salary, age):
    super().__init__(age)
    self.__salary = salary
    
  def annual_income(self):
    return 12 * self.__salary + 25000

class Dealer(TaxPayer):
  
  def __init__(self, sales, age):
    super().__init__(age)
    self.__sales = sales
    
  def annual_income(self):
    return 0.05 * self.__sales
    

#this will cause error - Can't instantiate abstract class
#john = TaxPayer(23)

jill = Employee(21000, 36)
jack = Dealer(5800000, 63)

print("Jill's income tax =", jill.income_tax())
print("Jack's income tax =", jack.income_tax())
