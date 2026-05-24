def sol(target):
	total = 0
	for ch in target:
		if "A" <= ch <= "Z":
			total += ord(ch) - ord("A") + 1
		elif "a" <= ch <= "z":
			total += ord(ch) - ord("a") + 1
	while total >= 10:
		temp = 0
		for ch in str(total):
			temp += int(ch)
		total = temp
		
	return total
	
while True:
	try:
		s1 = input()
		s2 = input()
	except:
		break
	
	n1 = sol(s1)
	n2 = sol(s2)
	
	if n1 > n2:
		n1, n2 = n2, n1
	
	if n2 == 0:
		print("0.00 %")
	else:
		print(f"{(100 * n1 / n2):.2f} %")
# 2026.05.25 二刷 細節要注意尤其是分母為0
