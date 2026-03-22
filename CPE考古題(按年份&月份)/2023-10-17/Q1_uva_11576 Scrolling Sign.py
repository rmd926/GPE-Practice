tc = int(input())
for _ in range(tc):
	k, w = map(int, input().split())
	output = input()
	total = k
	
	for _ in range(1, w):
		sign = input()
		overlap = 0
		for i in range(k):
			if output[i:] == sign[:k-i]:
				overlap = k-i
				break
			
		total += k - overlap
		output = sign
			
	print(total)
