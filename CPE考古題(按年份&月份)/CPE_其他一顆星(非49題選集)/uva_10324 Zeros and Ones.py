tc = 1
while True:
	target = input()
	n = int(input())
	
	print(f"Case {tc}:")
	for _ in range(n):
		a, b = map(int, input().split())
		high, low = max(a,b), min(a,b)
		temp = 0
		
		for ch in target[low: high+1]:
			temp += int(ch)
		
		if temp == (high - low + 1) or temp == 0:
			print("Yes")
		else:
			print("No")

	tc += 1

# 2026.05.25 二刷
