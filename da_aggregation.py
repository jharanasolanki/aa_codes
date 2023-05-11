count=0
totalcost=0
items=0
capacity=1
pow=0
f = open('da_test.py','r')
for line in f:
  if line.find('da')!=-1 or line.find('for')!=-1:
    if line.find('push_back(')!=-1 and line.find('push_back(self')==-1:
      if items<capacity:
        items+=1
        cost = 1
      else:
          capacity+=2**pow
          items+=1
          cost = 1 + 2**pow
          pow+=1
      totalcost+=cost
      count+=1
      print(f'table size: {capacity} cost: ',cost)
    elif line.find('for')!=-1:
        n=int(line[line.find('(')+1:line.find(')')])
        print(n)
        for i in range(n):
          if items<capacity:
            items+=1
            cost = 1
          else:
              capacity+=2**pow
              items+=1
              cost = 1 + 2**pow
              pow+=1
          totalcost+=cost
          count+=1
          print(f'table size: {capacity} cost: ',cost)
        f.readline()
        
      
print('totalcost: ',totalcost)