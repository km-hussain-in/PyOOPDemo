class Echo:
  
  def __init__(self, target):
    self.target = target

  def __call__(self, *args):
    print(f">>Invoking {self.target.__name__}")
    return self.target(*args)

@Echo
def greet(name, formal=False):
  if formal:
    return f'Hello {name}.'
  return f'Hi {name}!'


print(greet('Jack'))
print(greet("Jack's Mom", True))
