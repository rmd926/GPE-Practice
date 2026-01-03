while True:
	num, target = input().split()
	num = int(num)
	if num == 0:
		break
		
	group_len = len(target) // num
	ans = ''
	for i in range(0, len(target), group_len):
		ans += ''.join((target[i:i+group_len])[::-1])
	print(ans)
