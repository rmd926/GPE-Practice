tc = int(input())

for _ in range(tc):
	target = int(input())
	ans = ""
	
	if target < 10:
		print(target)
		continue
		
	for num in range(9, 1, -1):
		while target % num == 0:
			ans += str(num)
			target //= num
	
	if target == 1:
		print("".join(sorted(ans)))
	
	else:	
		print(-1)
