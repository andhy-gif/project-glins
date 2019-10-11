f=open('data3.txt')
l=f.readlines()
data=[]
a=[]
for i in l:
  data.append(i.rstrip().split(' '))

for i in range(len(data)):
  if i - (i+1) == 0 :
    print('tidak')
  else:
    print('ya')
    
