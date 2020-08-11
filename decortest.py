def once(target):
  def wrapper():
    if not hasattr(target, 'once_result'):
      target.once_result = target()
    return target.once_result
  return wrapper

@once
def greet():
 print('Producing greet message')
 return 'Hello World'

print(greet())
print(greet())

class Echo:
  
  def __init__(self, target):
    self.target = target

  def __call__(self, *args):
    print(f">>Invoking {self.target.__name__}")
    return self.target(*args)
    
  #just a helper (not required)
  def decorates(func):
    return isinstance(func, Echo)

@Echo
def greet(name, formal=False):
  if formal:
    return f'Hello {name}.'
  return f'Hi {name}!'

print(greet('Jack'))
print(greet("Jack's Mom", True))
#print(Echo.decorates(greet))

class Interval:
  
  def __init__(self):
    self.__min = 0
    self.__sec = 0
    
  @property
  def time(self): 
    return 60 * self.__min + self.__sec
  
  @time.setter
  def time(self, value):
    self.__min = value // 60
    self.__sec = value % 60
  
  def __str__(self):
    return(f'{self.__min}:{self.__sec:02d}')

i = Interval()
i.time = 125
print(i)
