class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class DoublyLinkedList:
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
      self.tail = new_node
      self.head = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node 
    self.length += 1
    return True
  
  def pop(self):
    if self.tail is None:
      return False
    
    last_item = self.tail
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
      last_item.prev = None
    self.length -= 1
    return last_item
  
  def prepend(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    self.length += 1
    return True
  
  def pop_first(self):
    if self.head is None:
      return False
    
    first_item = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
      self.head.prev = None
      first_item.next = None
    self.length -= 1
    return first_item
  
  def get(self, index):
    if (self.head is None or index < 0 or index >= self.length):
      return False
    
    node = self.head
    if index < self.length / 2:
      for _ in range(index):
        node = node.next
    else:
      node = self.tail
      for _ in range(self.length - 1, index, -1):
        node = node.prev
    return node

  def set(self, index, value):
    node = self.get(index)
    if node is not None:
      node.value = value
      return True
    return False
  
  def insert(self, index, value):
    if (index < 0 or index > self.length):
      return False

    if (index == 0):
      return self.prepend(value)
    elif (index == self.length):
      return self.append(value)
    else:
      new_node = Node(value)
      curr_node = self.get(index)
      prev_node = curr_node.prev
      if (curr_node is not None):
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = curr_node
        curr_node.prev = new_node
        self.length += 1
        return True
      return False
    
  def remove(self, index):
    if (index < 0 or index >= self.length):
      return False
    if (index == 0):
      return self.pop_first()
    elif (index == self.length - 1):
      return self.pop()
    else:
      candidate = self.get(index)
      prev_node = candidate.prev
      prev_node.next = candidate.next
      candidate.prev = prev_node
      candidate.next = None
      candidate.prev = None
      return True

my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
# my_doubly_linked_list.print_list()

# POP FUNC TESTING
# print('BEFORE: ')
# my_doubly_linked_list.print_list()
# print('AFTER: ')
# my_doubly_linked_list.pop()
# my_doubly_linked_list.pop()
# my_doubly_linked_list.print_list()

# PREPEND FUNC TESTING
# print('BEFORE: ')
# my_doubly_linked_list.print_list()
# print('AFTER: ')
# my_doubly_linked_list.prepend(1000)
# my_doubly_linked_list.prepend(10001)
# my_doubly_linked_list.print_list()

# # POP FIRST FUNC TESTING
# print('BEFORE: ')
# my_doubly_linked_list.print_list()
# print('AFTER: ')
# my_doubly_linked_list.pop_first()
# my_doubly_linked_list.pop_first()
# my_doubly_linked_list.print_list()

# POP FIRST FUNC TESTING
# print(my_doubly_linked_list.get(0).value)
# print(my_doubly_linked_list.get(2).value)
# print(my_doubly_linked_list.get(3).value)
# print(my_doubly_linked_list.get(4).value)
# print(my_doubly_linked_list.get(6))

# INSERT FUNC TESTING
# print('BEFORE')
# my_doubly_linked_list.print_list()
# my_doubly_linked_list.insert(6, 1111)
# print('AFTER')
# my_doubly_linked_list.print_list()

# REMOVE FUNC TESTING
print('BEFORE')
my_doubly_linked_list.print_list()
my_doubly_linked_list.remove(4)
print('AFTER')
my_doubly_linked_list.print_list()
