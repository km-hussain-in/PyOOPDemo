class Employee:
  
  __count = 0
  
  def __init__(self, hours=0, rate=50):
    Employee.__count += 1
    self.__id = 100 + Employee.__count
    self.__hours = hours
    self.__rate = rate
    
  def get_id(self): return self.__id
  
  def get_hours(self): return self.__hours
  
  def set_hours(self, val): self.__hours = val
  
  def get_rate(self): return self.__rate
  
  def set_rate(self, val): self.__rate = val
  
  def get_income(self):
    income = self.__hours * self.__rate
    ot = self.__hours - 180
    if ot > 0: income += 50 * ot
    return income
    

class SalesPerson(Employee):
  
  def __init__(self, hours, rate, sales):
    Employee.__init__(self, hours, rate)
    self.__sales = sales
    
  def get_sales(self): return self.__sales
  
  def get_income(self):
    income = Employee.get_income(self)
    if self.__sales >= 20000:
      income += 0.05 * self.__sales
    return income

