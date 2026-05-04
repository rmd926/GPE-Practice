while True:
	try:
		n = int(input())
	except:
		break
	
	print(3*((n+1)*(n+1)//2 - 3))
