balance=0
totalcost=0
items=0
f=open('stack_test.py','r')
for line in f:
  if line.find('Stack')!=-1 or line.find('for')!=-1:
    if line.find('push(')!=-1 and line.find('push(self')==-1:
      items+=1
      balance+=1
      totalcost+=2
      print('amortized cost: 2 actual cost: 1 balance: ',balance)
    elif line.find('multipop(')!=-1 and line.find('multipop(self')==-1:
      n=int(line[line.find('(')+1:line.find(')')])
      n=min(items,n)
      items-=n
      balance-=n
      totalcost+=0
      print(f'amortized cost: 0 actual cost: {n} balance: ',balance)
    elif line.find('pop(')!=-1 and line.find('pop(self')==-1:
      items-=1
      balance-=1
      totalcost+=0
      print('amortized cost: 0 actual cost: 1 balance: ',balance)
    elif line.find('for')!=-1:
      n=int(line[line.find('(')+1:line.find(')')])
      l=f.readline()
      if l.find('push')!=-1:
        items+=n
        balance+=n
        totalcost+=2*n
        print(f'amortized cost: {2*n} actual cost: {n} balance: ',balance)
      elif l.find('pop')!=-1:
        items-=n
        balance-=n
        totalcost+=0
        print(f'amortized cost: 0 actual cost: {n} balance: ',balance)
        
print('totalcost: ',totalcost)