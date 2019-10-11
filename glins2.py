f=open('teks2.txt')
l=f.readlines()
data=[]
aku=[]
a=''
for i in l:
  data.append(i.rstrip().split(' '))

for i in range(len(data)):
  for j in data[i]:
    for k in range(len(j)-1,-1,-1):
      aku.append(j[k])
for i in aku:
  a+=i
print(a)
