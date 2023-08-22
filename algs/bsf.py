#BSF - breadth first search - в ширину


def bsf(self):
  stack = []
  results = []
  stack.append(self.root)

  while len(stack) > 0:
    node = stack.pop(0)
    results.append(node.value)
    
    if (node.left is not None):
      stack.append(node.left)

    if (node.right is not None):
      stack.append(node.right)

  return results

