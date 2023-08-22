class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self, value):
    new_node = Node(value)
    self.top = new_node
    self.length = 1

  def print_stack(self):
    node = self.top
    while node is not None:
      print(node.value)
      node = node.next

  def push(self, value):
    new_node = Node(value)
    if self.top is None:
      self.top = new_node
    else:
      new_node.next = self.top
      self.top = new_node
    
    self.length += 1
    return True
  
  def pop(self):
    if self.top is None:
      return False
    
    old_node = self.top
    if self.length == 1:
      self.top = None
    else:
      self.top = old_node.next
      old_node.next = None
    
    self.length -= 1
    return old_node
    
   


my_stack = Stack(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
my_stack.pop()
my_stack.pop()

my_stack.print_stack()
