f = open('stack_test.py','r')
totalcost=0
count=0
items=0
for line in f:
  if line.find('Stack')!=-1 or line.find('for')!=-1:
    if line.find('push(')!=-1 and line.find('push(self')==-1:
      totalcost+=1
      items+=1
      count+=1
    elif line.find('multipop(')!=-1 and line.find('multipop(self')==-1:
      n=int(line[line.find('(')+1:line.find(')')])
      n=min(n,items)
      totalcost+=n
      count+=n
      items-=n
    elif line.find('pop(')!=-1 and line.find('pop(self')==-1:
      totalcost+=1
      count+=1
      items-=1
    elif line.find('for')!=-1:
      n=int(line[line.find('(')+1:line.find(')')])
      totalcost+=n
      count+=n
      l=f.readline()
      if l.find('push(')!=-1:
        items+=n
      else:
        items-=n

print('total cost: ',totalcost)      
print('total lines: ',count)
print('amortized analysis: ',(totalcost/count))