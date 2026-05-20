while True:
	target = input()
	if target == "0":
		break
	
	while int(target) >= 10:
		temp = 0
		for ch in target:
			temp += int(ch)
		target = str(temp)
		
	print(target)
# 2026.05.20 二刷
