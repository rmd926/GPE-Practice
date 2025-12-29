while True:
	num = int(input())
	if num == 0:
		break
	print(num * (num+1) * (2 * num + 1) // 6)