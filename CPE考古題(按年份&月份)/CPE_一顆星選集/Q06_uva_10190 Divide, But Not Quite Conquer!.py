while True:
	n, m = map(int, input().split())
	if n == 0 or m == 0 or n == 1 or m == 1:
		print("Boring!")
	
	else:
		ans = [n]
		status = True
		
		while n > 1:
			if n % m == 0:
				n //= m
				ans.append(n)
			else:
				status = False
				break
		
		if status:
			print(*ans)
		
		else:
			print("Boring!")	
# version 1

while True:
	target, k = map(int, input().split())
	
	if target == 0 or k == 0 or target == 1 or k == 1:
		print("Boring!")
		
	else:
		ans = [target]
		
		while target % k == 0:
			ans.append(target // k)
			target //= k
		
		if target == 1:
			print(*ans)
		else:
			print("Boring!")

# 2026.05.19 二刷
