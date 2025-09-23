while True:
	try:
		m = int(input())
		n = int(input())
	except:
		break
	
	print(round(n**(1/m)))