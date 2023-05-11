class Node:
  def __init__(self,left=None,right=None,value=0,color='',parent=None,root=False) -> None:
    self.left = left
    self.right = right
    self.value = value
    self.color = color
    self.parent = parent
    self.root = root
    self.children =[]
    
  def recolor(self):
    if self.color == 'R':
      self.color = 'B'
    else:
      self.color = 'R'
    
  def inorderTraversal(self, root):
    res = []
    if root:
        res = self.inorderTraversal(root.left)
        res.append({root.value,root.color})
        res = res + self.inorderTraversal(root.right)
    return res
  
def bst_search(self,element):
  if element == self.value:
    return self
  elif element > self.value:
    return bst_search(self.right,element)
  else:
    return bst_search(self.left,element)
          
def delete_node(self):
  parent = self.parent
  if parent.left is not None:
    if parent.left == self:
      parent.left = None
  elif parent.right == self:
    parent.right = None
    
def replacerNode(node):
  print(node.value)
  if node.left is not None:
    replacerNode(node.left)
  else:
    print(node)
    return node
  
def delete(node):
  if node.color == 'R':
    if node.left is None and node.right is None:
      delete_node(node)
      return
    
    if node.right is not None:
      newnode = replacerNode(node.right)
      print(newnode)
    else:
      newnode = replacerNode(node.left)
  
    node.value = newnode.value
    delete(newnode)

# driver code



root = Node(value=10,color='B')
root.right = Node(value=30, color='R',parent=root)
root.right.right = Node(value=40, color='B',parent=root.right)
root.right.left = Node(value=25, color='B',parent=root.right)
root.right.right.left = Node(value=38, color='R',parent=root.right.right)
root.left = Node(value=5, color='R',parent=root)
root.left.left = Node(value=2, color='B',parent=root.left)
root.left.right = Node(value=9, color='B',parent=root.left)

print(root.inorderTraversal(root))

element = 30
node = bst_search(root,element)
delete(node)
print(root.inorderTraversal(root))


 