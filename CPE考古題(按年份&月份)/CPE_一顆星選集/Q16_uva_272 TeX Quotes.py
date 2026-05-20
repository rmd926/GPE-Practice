count = 0
while True:
	target = input()
	ans = ""
	
	for ch in target:
		if ch == '"':
			count += 1
			
			if count % 2 == 1:
				ans += "``"
			else:
				ans += "''"
		else:
			ans += ch
	
	print(ans)
# 2026.05.20 二刷 要留意count初始化的位置
