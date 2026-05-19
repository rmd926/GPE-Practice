while True:
	a, b = map(int, input().split())
	if a == b == 0:
		break
	
	carry = 0
	ans = 0
	
	while a > 0 or b > 0:
		if a % 10 + b % 10 + carry >= 10:
			carry = 1
			ans += 1
		else:
			carry = 0
		
		a //= 10
		b //= 10
	
	if ans == 0:
		print("No carry operation.")
		
	elif ans == 1:
		print("1 carry operation.")
		
	else:
		print(f"{ans} carry operations.")

# 2026.05.20 二刷
