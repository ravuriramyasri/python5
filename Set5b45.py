def countd(n):
	h=0
	while(n!=0):
		n//=10
		h+=1
	print(h)
def main():
	try:
		n=int(input())
		countd(n)
	except:
		print('invalid')
main()
