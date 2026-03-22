while True:
	N = int(input())
	if N == 0:
		break
	k = 0
	
	while N >= 0:
		k += 1
		N -= k
	
	print(f"{-N} {k}")
