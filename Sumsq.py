num=int(raw_input())
a=0
while(num!=0):
	temp=num%10
	a=a+(temp*temp)
	num=num//10
print a
