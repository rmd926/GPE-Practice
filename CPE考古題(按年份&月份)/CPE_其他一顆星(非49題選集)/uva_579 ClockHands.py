while True:
	h, m = input().split(":")
	h, m = int(h), int(m)
	if h == 0 and m == 0:
		break
	
	h_degree = (h % 12) * 30 + 0.5 * m
	m_degree = m * 6
	ans = abs(h_degree - m_degree)
	
	if ans > 180:
		print(f"{360-ans:.3f}")
	else:
		print(f"{ans:.3f}")
