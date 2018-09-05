lower=int(raw-input())
upper=int(raw_input())
for num i in range(lower,upper):
     if num>1:
         for i in range(2,num):
              if(num % i)==0:
                 break
         else:
              print(num) 
