tc = int(input())
for i in range(tc):
	print(f"Case #{i+1}:")
	url_dict = {}
	
	for j in range(10):
		target = input().split()
		url = target[0]
		score = int(target[1])
		url_dict[url] = score
		
		max_score = max(url_dict.values())
		
	for key, value in url_dict.items():
		if value == max_score:
			print(key)