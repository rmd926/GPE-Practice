while True:
	N = int(input())
	if N < 0:
		break
	else:
		print(1 + N*(N+1)//2)