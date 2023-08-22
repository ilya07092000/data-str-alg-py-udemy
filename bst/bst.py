class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = Node(value)
    if (self.root is None):
      self.root = new_node
      return
    else:
      node = self.root
      while True:
        if new_node.value == node.value:
          return False
        
        if new_node.value > node.value:
          if (node.right is None):
            node.right = new_node
            return True
          node = node.right
        else:
          if (node.left is None):
            node.left = new_node
            return True
          node = node.left

  def contains(self, value):
    if (self.root is None):
      return False
    
    node = self.root
    while node is not None:
      if (value < node.value):
        node = node.left
      elif value > node.value:
        node = node.right
      else:
        return True

    return False
  
  def __r_contains(self, current_node, value):
    if current_node == None:
      return False
    if value == current_node.value:
      return True
    if value < current_node.value:
      return self.__r_contains(current_node.left, value)
    if (value > current_node.value):
      return self.__r_contains(current_node.right, value) 
    
  def r_contains(self, value):
    return self.__r_contains(self.root, value)
  
  def __r_insert(self, current_node, value):
    if current_node == None:
      return Node(value)
    if value < current_node.value:
      current_node.left = self.__r_insert(current_node.left, value)
    if value > current_node.value:
      current_node.right = self.__r_insert(current_node.right, value)
    return current_node

  def r_insert(self, value):
    if (self.root == None):
      self.root = Node(value)
    return self.__r_insert(self.root, value)
  
  def min_value(self, current_node):
    while current_node.left is not None:
      current_node = current_node.left
    return current_node.value
  
  def __delete_node(self, current_node, value):
    if current_node == None:
      return None
    if value < current_node.value:
      current_node.left = self.__delete_node(current_node.left, value)
    elif value > current_node.value:
      current_node.right = self.__delete_node(current_node.right, value)
    else:
      if current_node.left == None and current_node.right == None:
        return None 
      elif current_node.left == None:
        current_node = current_node.right
      elif current_node.right == None:
        current_node = current_node.left
      else:
        sub_tree_min = self.min_value(current_node.right)
        current_node.value = sub_tree_min
        current_node.right = self.__delete_node(current_node.right, sub_tree_min)
      
    return current_node

  def delete_node(self, value):
    self.root = self.__delete_node(self.root, value)
          

# my_tree = BinarySearchTree()
# my_tree.insert(10)
# my_tree.insert(20)
# my_tree.insert(30)
# my_tree.insert(50)
# my_tree.insert(5)
# # print(my_tree.root.right.right.value)
# print(my_tree.contains(5))

my_tree = BinarySearchTree()
my_tree.r_insert(10)
my_tree.r_insert(20)
my_tree.r_insert(30)
my_tree.r_insert(50)
my_tree.r_insert(5)
# print(my_tree.root.right.right.value)
print(my_tree.r_contains(5))