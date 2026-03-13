tc = int(input())
for t in range(tc):
	size = int(list(input().split())[-1])
	M = [[int(x) for x in input().split()] for _ in range(size)]
	status = True
	
	for i in range(size):
		for j in range(size):
			n1 = M[i][j]
			n2 = M[size-i-1][size-j-1]
			
			if n1 < 0 or n2 < 0 or n1 != n2:
				status = False
	
	print(f"Test #{t+1}: Symmetric.") if status else print(f"Test #{t+1}: Non-symmetric.")
