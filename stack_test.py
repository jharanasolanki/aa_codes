class Stack:
  el=[]
  def __init__(self) -> None:
    pass
  
  def push(self,n):
    self.el.append(n)
  
  def pop(self):
    self.el.pop()
  
Stack.push(10)
Stack.push(20)
Stack.push(30)
Stack.pop()

for i in range(20):
  Stack.push(10)
  
Stack.multipop(10)

