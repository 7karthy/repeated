z=int(input('enter'))
a=[]
for i in range(z):
  b=input("enter the value")
  a.append(b)
for i in a:
  count=a.count(i)
  if count==1:
    print(i)
  else:
      continue
