while True:
	target = int(input())
	if target == 0:
		break
	
	count = 0
	ans = bin(target)[2:]
	
	for digit in str(ans):
		if digit == "1":
			count += 1
	print(f"The parity of {ans} is {count} (mod 2).")
# 2026.05.19 二刷
