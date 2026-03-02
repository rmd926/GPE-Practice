def cal_length(num):
	length = 1
	while num != 1:
		if num % 2 == 0:
			num //= 2
		else:
			num = num * 3 + 1
		length += 1
		
	return length

while True:
	low, high = map(int, input().split())
	ans = 0
	
	for num in range(min(low, high), max(low, high)+1):
		ans = max(ans, cal_length(num))
	
	print(low, high, ans)
