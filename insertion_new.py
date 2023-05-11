class Node:
  root = None
  def __init__(self) -> None:
    self.left = None
    self.right = None
    self.value = 0
    self.color = ''
    self.parent = None
    self.root = False
    
  def recolor(self):
    if self.color == 'R':
      self.color = 'B'
    else:
      self.color = 'R'
  
  def inorderTraversal(self, root):
    res = []
    if root:
        res = self.inorderTraversal(root.left)
        res.append([root.value,root.color])
        res = res + self.inorderTraversal(root.right)
    return res
  
  def rr_rotation(self,parent,grandparent):
    if Node.root == grandparent:
      Node.root = parent
    else:
      top = grandparent.parent
      parent.parent = top
      if top.left == grandparent:
        top.left = parent
      else:
        top.right = parent
    parent.recolor()
    grandparent.recolor()
    grandparent.right = parent.left
    if parent.left is not None:
      parent.left.parent = grandparent
    parent.left = grandparent
    grandparent.parent = parent
    
  def ll_rotation(self,parent,grandparent):
    if Node.root == grandparent:
      Node.root = parent
    else:
      top = grandparent.parent
      parent.parent = top
      if top.left == grandparent:
        top.left = parent
      else:
        top.right = parent
    parent.recolor()
    grandparent.recolor()
    grandparent.left = parent.right
    if parent.right is not None:
      parent.right.parent = grandparent
    parent.right = grandparent
    grandparent.parent = parent
    
  def rl_rotation(self,parent):
    grandparent = parent.parent
    grandparent.right = self
    self.parent = grandparent
    self.right = parent
    parent.parent = self
    parent.left = None
    parent.rr_rotation(self,grandparent)
    
  def lr_rotation(self,parent):
    grandparent = parent.parent
    grandparent.left = self
    self.parent = grandparent
    self.left = parent
    parent.parent = self
    parent.right = None
    parent.ll_rotation(self,grandparent)  
  
  def parent_red(self):
    parent = self.parent
    grandparent = parent.parent
    uncle = None
    if grandparent.left is not None:
      if grandparent.left == parent:
        uncle = grandparent.right
      else:
        uncle = grandparent.left
    
    if uncle is not None:
      if uncle.color == 'R':
        parent.color = 'B'
        uncle.color = 'B'
        if grandparent!=Node.root:
          grandparent.recolor()
          parent.check_all()
        return
    # uncle black
    if grandparent.left is not None:
      if parent.left is not None:
        if grandparent.left == parent and parent.left == self:
          self.ll_rotation(parent,grandparent)
          return
      if parent.right is not None:
        if grandparent.left == parent and parent.right == self:
          self.lr_rotation(parent)
          return
    
    if grandparent.right is not None:
      if parent.left is not None:
        if grandparent.right == parent and parent.left == self:
          self.rl_rotation(parent)
          return
      if parent.right is not None:
        if grandparent.right == parent and parent.right == self:
          self.rr_rotation(parent,grandparent)
          return
  
  def check_all(self):
    if self == Node.root:
      self.color='B'
      return
    if self.color == 'R':
      if self.parent.color == 'R':
        self.parent_red()
      else:
        return
  
  def insert(self,element,parent=None):
    if self.color=='':
      self.value=element
      self.color='B'
      self.parent = parent
      return
    
    elif self.value < element:
      if self.right is None:
        self.right = Node()
        self.right.value=element
        self.right.color='R'
        self.right.parent = self
        self.right.check_all()
        return
      self.right.insert(element,self)
      
    elif self.value > element:
      if self.left is None:
        self.left = Node()
        self.left.value=element
        self.left.color='R'
        self.left.parent = self
        self.left.check_all()
        return
      self.left.insert(element,self)

start=Node()
Node.root = start
elements = [int(item) for item in input("Enter elements to be inserted: ").split()]

for el in elements:
  start.insert(el)
  start=Node.root

print(start.inorderTraversal(start))

# 10 18 7 15 16 30 25 40 60  
