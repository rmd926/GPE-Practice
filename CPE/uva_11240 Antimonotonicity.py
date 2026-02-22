tc = int(input())
for _ in range(tc):
	target = list(map(int, input().split()))[1:]
	length = 1
	for i in range(1, len(target)):
		if (length % 2 == 1 and target[i] < target[i-1]) or (length % 2 == 0 and target[i] > target[i-1]):
			length += 1
			
	print(length)