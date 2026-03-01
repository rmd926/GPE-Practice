while True:
	target = int(input())
	ans = target
	
	while target >= 3:
		temp = (target // 3)
		ans += temp
		remain = target % 3
		target = temp + remain
	
	if target == 2:
		ans += 1
	
	print(ans)
