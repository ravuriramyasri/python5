a,b=map(int,raw_input().split())
for i in range(a+1,b):
     if i>1:
          for v in range(2,i):
               if i%v==0:
                    break
          else:
               print i,
