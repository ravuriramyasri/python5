sum=0
num=int(raw_input())
temp=num
while temp > 0:
	digit=temp % 10
	sum +=digit ** 3
	temp //=10
  if num == sum:
        print("yes")
  else:
	print("no")
