while True:
	s, c1, c2, c3 = map(int, input().split())
	if s == c1 == c2 == c3 == 0:
		break
		
	ans = 1080
	ans += (s-c1) % 40 * 9 + (c2-c1) % 40 * 9 + (c2-c3) % 40 * 9
	
	print(ans)
