tc = int(input())
for t in range(tc):
	size = int(input().split()[-1])
	M = [[int(x) for x in input().split()] for _ in range(size)]
	status = True
	
	for i in range(size):
		for j in range(size):
			x1 = M[i][j]
			x2 = M[size-i-1][size-j-1]
			
			if x1 < 0 or x2 < 0 or x1 != x2:
				status = False
				break
			else:
				continue
	
	if status:
		print(f"Test #{t+1}: Symmetric.")
	else:
		print(f"Test #{t+1}: Non-symmetric.")

# 2026.05.23 二刷，注意initial M的時候，語法要記起來
