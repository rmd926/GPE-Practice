while True:
	n = int(input())
	if n == 0:
		break
	else:
		print(int(n*(n+1)*(2*n+1) / 6))