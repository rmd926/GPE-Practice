while True:
	try:
		G, target = map(str, input().split())
	except:
		break
	
	if G == "0":
		break
		
	n = len(target)
	G = int(G)
	group = len(target) // G
	
	ans = ""
	for i in range(0, n+1, group):
		ans += target[i: i+group][::-1]
	
	print(ans)

# 2026.05.25 二刷
