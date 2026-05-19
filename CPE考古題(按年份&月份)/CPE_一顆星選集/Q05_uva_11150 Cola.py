while True:
	target = int(input())
	ans = target
	
	while target >= 3:
		temp = target // 3
		remain = target % 3
		ans += temp
		target = temp + remain
	
	if target == 2:
		ans += 1
	
	print(ans)

# 2026.05.19 二刷
