# amortized cost = actual cost + diff in potential
# potential = no of elements in stack

totalcost=0
items =0
f=open('stack_test.py','r')
for line in f:
  if line.find('Stack')!=-1 or line.find('for')!=-1:
    if line.find('push(')!=-1 and line.find('push(self')==-1:
      cost = 1 + items+1 - items
      print('cost: ',cost)
      totalcost += cost
      items+=1
    elif line.find('multipop(')!=-1 and line.find('multipop(self')==-1:
      n=int(line[line.find('(')+1:line.find(')')])
      n=min(items,n)
      cost = n + items-n - items
      print('cost: ',cost)
      totalcost += cost
      items-=n
    elif line.find('pop(')!=-1 and line.find('pop(self')==-1:
      cost = 1 + items-1 - items
      print('cost: ',cost)
      totalcost += cost
      items-=1
    elif line.find('for')!=-1:
      n=int(line[line.find('(')+1:line.find(')')])
      l=f.readline()
      if l.find('push')!=-1:
        cost = n + items+n - items
        print('cost: ',cost)
        totalcost += cost
        items+=n
      elif l.find('pop')!=-1:
        cost = n + items-n - items
        print('cost: ',cost)
        totalcost += cost
        items-=n
        
      
print('totalcost: ',totalcost)