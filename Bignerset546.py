def countd(g):
	print(g+1)
def main():
	try:
		g=int(input())
		countd(g)
	except:
		print('invalid')
main()
