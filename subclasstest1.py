import payroll

def income_tax(emp):
  e = emp.get_income() - 10000
  return 0.15 * e if e > 0 else 0

def average_income(group):
  total = 0
  for member in group:
    total += member.get_income()
  return total / len(group)
  
def total_sales(group):
  return sum(e.get_sales() for e in group if isinstance(e, payroll.SalesPerson))
  

jack = payroll.Employee()
jack.set_hours(186)
jack.set_rate(52)
jill = payroll.SalesPerson(186, 52, 48000)
print(f"Jack's ID is {jack.get_id()}, Income is {jack.get_income()} and Tax is {income_tax(jack)}")
print(f"Jill's ID is {jill.get_id()}, Income is {jill.get_income()} and Tax is {income_tax(jill)}")

dept = [jack, jill]
print(f'Average income: {average_income(dept):.2f}')
print(f'Total sales   : {total_sales(dept):.2f}')
