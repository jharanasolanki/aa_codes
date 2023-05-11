class Node:
  def __init__(self,x=0,y=0,left=None,right=None):
    self.x=x
    self.y=y
    self.left=left
    self.right=right
    
  def inorderTraversal(self,root):
    res=[]
    if root:
      res = res + self.inorderTraversal(root.left)
      res.append([root.x,root.y])
      res = res + self.inorderTraversal(root.right)
    return res
  
  def insert(self,x,y,start='x'):
    if self.x == 0 and self.y ==0:
      self.x=x
      self.y=y
    else:
      if start == 'x':
        if x>self.x:
          if self.right is None:
            self.right = Node()
          self.right.insert(x,y,'y')
        else:
          if self.left is None:
            self.left = Node()
          self.left.insert(x,y,'y')
      else:
        if y>self.y:
          if self.right is None:
            self.right = Node()
          self.right.insert(x,y,'x')
        else:
          if self.left is None:
            self.left = Node()
          self.left.insert(x,y,'x')
          
inputs=[[6,2],[7,1],[2,9],[3,6],[4,8],[8,4],[5,3],[1,5],[9,5]]          
start=Node()
for el in inputs:
  start.insert(el[0],el[1])
print(start.inorderTraversal(start))