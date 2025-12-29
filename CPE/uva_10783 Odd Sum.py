TC = int(input())

for tc in range(TC):
	low = int(input())
	high = int(input())
	ans = 0
	
	if low % 2 == 0:
		low += 1
		
	for i in range(low, high+1, 2):
		ans += i
	
	print(f"Case {tc+1}: {ans}")
	