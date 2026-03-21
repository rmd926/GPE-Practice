tc = 1
while True:
	target = input()
	print(f"Case {tc}:")
	
	query = int(input())
	for _ in range(query):
		a, b = map(int, input().split())
		low, high = min(a, b), max(a, b)
		temp = 0
		
		for ch in target[low: high+1]:
			temp += int(ch)
		
		if temp == 0 or temp == high - low + 1:
			print("Yes")
		else:
			print("No")
		
	tc += 1
