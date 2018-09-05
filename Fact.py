N=int(raw_input())
if N==0:
        print("factorial of zero is 1")
else:
        fact=1
        for i in range(1,N+1):
                fact=fact*i
        print(fact)
