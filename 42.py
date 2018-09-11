a,b=map(str,raw_input().split())
count1=0
count2=0
for i in a:
      count1=count1+1
for j in b:
      count2=count2+1
if(count1<count2):
      print(b)
elif(count1==count2):
      print(" ")
else:
      print(a)
