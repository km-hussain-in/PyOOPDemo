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
    
  def peek(self, action):
    node = self.top
    while node is not None:
      action(node.value)
      node = node.below
    
  def __iter__(self):
    node = self.top
    while node is not None:
      yield node.value
      node = node.below
    

store = Stack()
store.push('Monday')
store.push('Tuesday')
store.push('Wednesday')
store.push('Thursday')
store.push('Friday')

print('Traversing items in store')
store.peek(lambda i : print(i))
print('----------------------')

print('Iterating items in store')
for item in store:
  print(item)
print('----------------------')
  
print('Popping items of store')
while not store.empty():
  print(store.pop())


