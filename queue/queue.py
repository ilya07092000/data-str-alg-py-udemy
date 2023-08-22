class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Queue:
  def __init__(self, value):
    new_node = Node(value)
    self.first = new_node
    self.last = new_node
    self.length = 1

  def print_queue(self):
    node = self.first
    while node is not None:
      print(node.value)
      node = node.next

  def enqueue(self, value):
    new_node = Node(value)
    if (self.last is None):
      self.first = new_node
      self.last = new_node
    else:
      self.last.next = new_node
      self.last = new_node
    self.length += 1

  def dequeue(self):
    if self.first is None:
      return False
    node = self.first
    if self.length == 1:
      self.first = None
      self.last = None
    else:
      self.first = self.first.next
      node.next = None
    self.length -= 1
    return node


my_queue = Queue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.enqueue(40)
my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()