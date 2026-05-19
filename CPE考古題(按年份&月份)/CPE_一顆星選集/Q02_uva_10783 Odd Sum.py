tc = int(input())
for t in range(tc):
	lower = int(input())
	upper = int(input())
	ans = 0
	
	if lower % 2 == 0:
		lower += 1
	
	for num in range(lower, upper+1, 2):
		ans += num
		
	print(f"Case {t+1}: {ans}")
# 2026.05.19 二刷
