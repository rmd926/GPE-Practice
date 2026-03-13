while True:
	h1, m1, h2, m2 = map(int, input().split())
	if h1 == h2 == m1 == m2 == 0:
		break
	ans = 0
	
	if h1 < h2:
		ans = (h2-h1) * 60 + (m2-m1)
		
	elif h1 >= h2:
		ans = (h2-h1+24) * 60 + (m2-m1)
	
	print(ans%1440)
