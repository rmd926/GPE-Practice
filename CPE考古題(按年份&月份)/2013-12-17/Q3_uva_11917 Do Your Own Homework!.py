tc = int(input())
for t in range(tc):
	N = int(input())
	lookup = {}
	for _ in range(N):
		sub, cost = map(str, input().split())
		lookup[sub] = int(cost)
	quota = int(input())
	pend = input()
	
	if pend in lookup and lookup[pend] <= quota:
		print(f"Case {t+1}: Yesss")
	
	elif pend in lookup and lookup[pend] > quota and lookup[pend] <= quota + 5:
		print(f"Case {t+1}: Late")
	
	else:
		print(f"Case {t+1}: Do your own homework!")
