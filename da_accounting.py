totalcost=0
balance=0
items=0
capacity=1
pow=1
f = open('da_test.py','r')
for line in f:
  if line.find('da')!=-1 or line.find('for')!=-1:
    if line.find('push_back(')!=-1 and line.find('push_back(self')==-1:
      if items<capacity:
        items+=1
        totalcost+=3
        balance+=2
      else:
          capacity=2*capacity
          balance-=items
          items+=1
          balance+=2
          pow+=1
      print(f'items: {items} table size: {capacity} balance: ',balance)
    
    elif line.find('for')!=-1:
      n=int(line[line.find('(')+1:line.find(')')])
      for i in range(n):
        if items<capacity:
          items+=1
          totalcost+=3
          balance+=2
        else:
            capacity=2*capacity
            balance-=items
            items+=1
            balance+=2
            pow+=1
        print(f'table size: {capacity} balance: ',balance)