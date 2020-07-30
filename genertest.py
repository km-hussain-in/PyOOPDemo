class Stack:

  class Node:
    
    def __init__(self, value, below):
      self.value = value
      self.below = below
  
  def __init__(self):
    self.top = None
    
  def push(self, val):
    self.top = Stack.Node(val, self.top)
    
  def pop(self):
    node = self.top
    self.top = node.below
    return node.value
    
  def empty(self):
    return self.top is None
 
  def __iter__(self):
    node = self.top
    while node is not None:
      yield node.value
      node = node.below

  def peek(self, action):
    node = self.top
    while node is not None:
      action(node.value)
      node = node.below
     
class StackContext:
  
  class Wrapper:
    
    def __init__(self, item):
      self.wrapped = item
      print('Wrapping', item)
      
    def __str__(self):
      return str(self.wrapped)
      
    def __del__(self):
      print('Unwrapping', self.wrapped)
      self.wrapped = None
      
  def __init__(self, *items):
    self.items = items
      
  def __enter__(self):
    self.resource = Stack()
    for item in self.items:
      self.resource.push(StackContext.Wrapper(item))
    return self.resource
    
  def __exit__(self, et, ev, tb):
    while not self.resource.empty():
      self.resource.pop()
    

store = Stack()
store.push('Desktop')
store.push('Laptop')
store.push('Printer')
store.push('Tablet')
store.push('Phone')

print('Items in store')
for item in store:
  print(item)
print('----------------------')
  
with StackContext('laptop', 'tablet', 'phone') as box:
  box.peek(lambda i : print('Shipping', i))


