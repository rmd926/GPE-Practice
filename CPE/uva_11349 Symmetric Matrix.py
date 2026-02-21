tc = int(input())

for t in range(tc):
	n = int(input().split()[-1])
	M = [[int(num) for num in input().split()] for _ in range(n)]
	status = True
	
	for i in range(n):
		for j in range(n):
			n1 = M[i][j]
			n2 = M[n-i-1][n-j-1]
			
			if n1 != n2 or n1 < 0 or n2 < 0:
				status = False
				break
	
	if status:
		print(f"Test #{t+1}: Symmetric.")
	else:
		print(f"Test #{t+1}: Non-symmetric.")
        