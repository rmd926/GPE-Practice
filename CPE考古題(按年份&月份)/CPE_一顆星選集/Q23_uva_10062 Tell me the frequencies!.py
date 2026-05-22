tc = 0

while True:
	target = input()
	lookup = {}
	
	if tc > 0:
		print()
	tc += 1
	
	for ch in target:
		if ch not in lookup:
			lookup[ch] = 1
		else:
			lookup[ch] += 1
	
	for key, value in sorted(lookup.items(), key = lambda x: (x[1], -ord(x[0]))):
		print(ord(key), value)
# 2026.05.22 二刷 line: 17那邊記得要考慮次數相同時比較的第二條件，也就是按照ord由大到小排
