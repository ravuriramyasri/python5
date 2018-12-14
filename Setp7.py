j=raw_input().split()
k=" "
for i in range(0,len(j)):
	j[i]=j[i].capitalize()
c=j[0]
for i in range(1,len(j)):
	c=c+k+j[i]
print c
