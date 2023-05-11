class Node:
  def __init__(self,x=0,y=0,left=None,right=None, parent=None):
    self.x = x
    self.y = y
    self.left = left
    self.right = right
    self.parent = parent
    
  def inorderTraversal(self,root):
    res=[]
    if root:
      res = res + self.inorderTraversal(root.left)
      res.append([root.x,root.y])
      res = res + self.inorderTraversal(root.right)
    return res
  
  def insert(self,x,y,parent):
    self.x=x
    self.y=y
    self.parent=parent
    
  # start : 0 = x 1 = y
  def sort_find(self,elements,start):
    n = len(elements)
    for i in range(n-1):
      for j in range(n-i-1):
        if elements[j][start] > elements[j+1][start]:
          elements[j], elements[j+1] = elements[j+1], elements[j]
          
    middle = int((n-1)/2)
    
    if n==2:
      self.insert(elements[0][0],elements[0][1],self)
      self.right=Node()
      self.right.insert(elements[1][0],elements[1][1],self)
      return
    if middle == 0:
      self.insert(elements[middle][0],elements[middle][1],self)
      return
    
    if start == 0:
      start = 1
    else:
      start = 0

    self.insert(elements[middle][0],elements[middle][1],self)
    self.left=Node()
    self.left.sort_find(elements[0:middle],start)
    self.right=Node()
    self.right.sort_find(elements[middle+1:n],start)
    
    
inputs=[[6,2],[7,1],[2,9],[3,6],[4,8],[8,4],[5,3],[1,5],[9,5]]  
# inputs=[[3,2],[5,8],[6,1],[9,0],[4,4],[1,1],[2,2],[8,7]]        
start=Node()
start.sort_find(inputs,0)
print(start.inorderTraversal(start))
    
    
      
      