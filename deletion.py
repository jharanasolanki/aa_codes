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
  
  def delete_node(self):
    parent = self.parent
    if parent.left is not None:
      if parent.left == self:
        parent.left = None
    elif parent.right == self:
      parent.right = None
      
  def bst_search(self,element):
    if element == self.value:
      return self
    elif element > self.value:
      return self.right.bst_search(element)
    else:
      return self.left.bst_search(element)
  
  def add_black(self):
    if self.color == 'R':
      self.color = 'B'
    else:
      self.double_black()
      
  def sibling_black_children_black(self,sibling):
    self.delete_node()
    self.parent.add_black()
    sibling.color = 'R'
    
  def farchildred(self,sibling):
    parent = self.parent
    if parent.left == sibling and sibling.left.color == 'R':
      temp = parent.color
      parent.color = sibling.color
      sibling.color = temp
      
    elif parent.right == sibling and sibling.right.color == 'R':
      temp = parent.color
      parent.color = sibling.color
      sibling.color = temp
      
      
    return
  
  def sibling_black(self,sibling):
    parent = self.parent
    if sibling.left is None and sibling.right is None :
      self.sibling_black_children_black(sibling)
    elif sibling.left is not None and sibling.right is not None:
      if sibling.left.color == 'B' and sibling.right.color == 'B':
        self.sibling_black_children_black(sibling)
      elif parent.left == sibling and sibling.left.color == 'B' and sibling.right.color=='R':
        sibling.right.color = 'B'
        sibling.color = 'R'
        parent.left = sibling.right
        temp = sibling.left.right 
        sibling.right.left = sibling
        sibling.right = temp
        sibling.right.parent = parent
        sibling.parent = sibling.right
        self.farchildred(sibling)
      elif parent.right == sibling and sibling.right.color == 'B' and sibling.left.color=='R':
        sibling.left.color = 'B'
        sibling.color = 'R'
        parent.right = sibling.left
        temp = sibling.left.right 
        sibling.left.right = sibling
        sibling.left = temp
        sibling.left.parent = parent
        sibling.parent = sibling.left
        self.farchildred(sibling)
    
  def sibling_red(self,sibling):
    parent = self.parent
    if parent.right == sibling:
      if parent.parent.right == parent:
        parent.parent.right = sibling
      else:
        parent.parent.left = sibling
        
      sibling.parent = parent.parent
      parent.parent = sibling
      parent.right = sibling.left
      sibling.left = parent
      temp = parent.color
      parent.color = sibling.color
      sibling.color = temp
      self.delete_node()
    else:
      sibling.parent = parent.parent
      parent.parent = sibling
      parent.left = sibling.right
      sibling.right = parent
      temp = parent.color
      parent.color = sibling.color
      sibling.color = temp
      self.delete_node()
  
  def double_black(self):
    parent = self.parent
    if parent is None:
      return
    if parent.left == self:
      sibling = parent.right
    else:
      sibling = parent.left
      
    if sibling is None:
      self.sibling_black_children_black(sibling)
    elif sibling.color == 'B':
      self.sibling_black(sibling)
    elif sibling.color == 'R':
      self.sibling_red(sibling)
      
    
  def delete(self):
    if self.left is None and self.right is None:
      if self.color == 'R':
        self.delete_node()
        return 
      elif self.color == 'B':
        self.double_black()
        return
    
    if self.right is not None:
      newnode = self.right
      while newnode.left is not None:
        newnode = newnode.left
    else:
      newnode = self.left
      while newnode.left is not None:
        newnode = newnode.left
    
    self.value = newnode.value
    newnode.delete()

# normal delete
# root = Node(value=10,color='B')
# root.right = Node(value=30, color='B',parent=root)
# root.right.right = Node(value=40, color='R',parent=root.right)
# root.right.right.right = Node(value=50, color='B',parent=root.right.right)
# root.right.left = Node(value=25, color='B',parent=root.right)
# root.right.right.left = Node(value=35, color='B',parent=root.right.right)
# root.right.right.left.right = Node(value=38, color='R',parent=root.right.right.left)
# root.left = Node(value=5, color='B',parent=root)
# root.left.left = Node(value=2, color='B',parent=root.left)
# root.left.right = Node(value=9, color='B',parent=root.left)


# print(root.inorderTraversal(root))
# element = 30
# node = root.bst_search(element)
# node.delete()
# print(root.inorderTraversal(root))


# sibling black children black
# root = Node(value=10,color='B')
# root.left = Node(value=5, color='B',parent=root)
# root.right = Node(value=20, color='B',parent=root)
# root.right.right = Node(value=30, color='B',parent=root.right)
# root.right.left = Node(value=15, color='B',parent=root.right)

# element = 15
# node = root.bst_search(element)
# node.delete()
# print(root.inorderTraversal(root))

# sibling red
# root = Node(value=10,color='B')
# root.left = Node(value=5, color='B',parent=root)
# root.right = Node(value=20, color='B',parent=root)
# root.right.left = Node(value=15, color='B',parent=root.right)
# root.right.right = Node(value=30, color='R',parent=root.right)
# root.right.right.left = Node(value=25, color='B',parent=root.right.right)
# root.right.right.right = Node(value=40, color='B',parent=root.right.right)

# element = 15
# node = root.bst_search(element)
# node.delete()
# print(root.inorderTraversal(root))

# sibling black far sibling child is black and near child is red
root = Node(value=10,color='B')
root.left = Node(value=5, color='B',parent=root)
root.left.left = Node(value=1, color='B',parent=root.left)
root.left.right = Node(value=7, color='B',parent=root.left)

root.right = Node(value=30, color='B',parent=root)
root.right.left = Node(value=25, color='R',parent=root.right)
root.right.right = Node(value=40, color='B',parent=root.right)
root.right.left.left = Node(value=20, color='B',parent=root.right.left)
root.right.left.right = Node(value=28, color='B',parent=root.right.left)

element = 1
node = root.bst_search(element)
node.delete()
print(root.inorderTraversal(root))