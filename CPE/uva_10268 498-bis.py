while True:
	try:
		x = int(input())
		target = list(map(int,input().split()))
		sum = 0
		n = len(target) - 1
		for coefficient in target:
			sum += (n * coefficient) * x ** (n-1)
			n -= 1
    
		print(int(sum))
		
	except:
		break