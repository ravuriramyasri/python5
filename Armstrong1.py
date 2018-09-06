a,b=map(int,raw_input().split())
def arms(a):
	b=a%10
	c=a/10
	d=c%10
	e=c/10
	x=b**3+d**3+e**3
	if(x==a):
		print(num)
for num in range(a,b+1):
	y=arms(num)
