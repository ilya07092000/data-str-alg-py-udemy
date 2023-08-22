class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next
    
  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
    return True # returning true is not necessary in this case (optional)

  def pop(self):
    if self.length == 0:
      return False
    
    if (self.length == 1):
      self.tail = None
      self.head = None
      self.length -=1 
      return True

    pre_last_node = None
    curr_node = self.head
    while pre_last_node is None:
      if curr_node.next.next is None:
        pre_last_node = curr_node
      curr_node = curr_node.next

    pre_last_node.next = None
    self.tail = pre_last_node
    self.length -=1 
    return curr_node.value
  
  def prepend(self, value):
    new_node = Node(value)
    if (self.length == 0):
      self.head = new_node
      self.tail = new_node
    else:
      old_head = self.head
      self.head = new_node
      self.head.next = old_head
    self.length += 1
    return True
  
  def pop_first(self):
    if (self.length == 0):
      return False

    if (self.length == 1):
      self.head = None
      self.tail = None
    else:
      temp = self.head
      self.head = self.head.next
      temp.next = None
    self.length -= 1;
    return temp.value
  
  def get(self, index):
    if (self.length <= index or index < 0):
      return False

    pointer = self.head    
    for _ in range(index):
      pointer = pointer.next

    return pointer;

  def set_value(self, index, value):
    if (index < 0 or index >= self.length):
      return False
    node = self.get(index)
    node.value = value

  def insert(self, index, value):  
    if (index == 0):
      self.prepend(value)
      return

    if (index == self.length):
      self.append(value)
      return

    candidate_node = self.get(index - 1)
    if (candidate_node):
      new_node = Node(value)
      new_node.next = candidate_node.next
      candidate_node.next = new_node
      self.length += 1
      return new_node
    return False
  
  def remove(self, index):
    if (index < 0 or index >= self.length):
      return False
    
    if (index == 0):
      return self.pop_first()   

    if (index == self.length - 1):
      return self.pop();
    
    prev_node = self.get(index - 1)
    curr_node = prev_node.next
    prev_node.next = curr_node.next
    curr_node.next = None
    self.length -= 1
    return curr_node

  def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = None
    before = None

    for _ in range(self.length):
      after = temp.next
      temp.next = before
      before = temp
      temp = after

    

my_linked_list = LinkedList(4)

# APPEND FUNC TESTING
my_linked_list.append(123)
my_linked_list.append(102)
my_linked_list.append(20)

# PRINT FUNC TESTING
# my_linked_list.print_list()

# DELETE FUNC TESTING
# print('ON DELETE: ')
# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print('DELETED: ')
# my_linked_list.print_list()

# PREPEND FUNC TESTING
# print('BEFORE PREPEND')
# my_linked_list.print_list()
# print('AFTER PREPEND')
# my_linked_list.prepend(666)
# my_linked_list.print_list()
# print('BEFORE PREPEND')
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.print_list()
# print('AFTER PREPEND')
# my_linked_list.prepend(666)
# my_linked_list.print_list()

# POP FUNCT TESTING
# print('BEFORE')
# my_linked_list.print_list()
# print('AFTER')
# print('POPPED', my_linked_list.pop())
# # my_linked_list.pop()
# my_linked_list.print_list()

# GET FUNC TESTING
# print(my_linked_list.get(2))

#SET VALUE FUNC TESTING
# my_linked_list.print_list()
# my_linked_list.set_value(1, 666)
# my_linked_list.print_list()

#INSERT NODE FUNC TESTING
# print('BEFORE:')
# my_linked_list.print_list()
# my_linked_list.insert(4, 1010)
# print('AFTER:')
# my_linked_list.print_list()

#REMOVE NODE FUNC TESTING
# print('BEFORE:')
# my_linked_list.print_list()
# my_linked_list.remove(2)
# print('AFTER:')
# my_linked_list.print_list()

# REVERSE
print('BEFORE')
my_linked_list.print_list()
print('AFTER')
my_linked_list.reverse()
my_linked_list.print_list()
