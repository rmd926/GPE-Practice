tc = 1
while True:
	n = int(input())
	target = list(map(int, input().split()))
	
	status = True
	seq = []
	for i in range(1, n):
		if target != sorted(target) or 0 in target:
			status = False
			break
			
		else:
			if abs(target[i]-target[i-1]) not in seq:
				seq.append(abs(target[i]-target[i-1]))
			else:
				status = False
				break
				
	if status:
		print(f"Case #{tc}: It is a B2-Sequence.")
	else:
		print(f"Case #{tc}: It is not a B2-Sequence.")
	
	tc += 1
	print()
	space = input()
	
# 2026.05.22 二刷 要留意格式
