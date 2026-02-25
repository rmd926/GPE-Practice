def cal_length(n, vito):
	mid = n // 2
	vito = sorted(vito)
	distance = 0
	for i in range(len(vito)):
		distance += abs(vito[mid] - vito[i])

	return distance

tc = int(input())
for _ in range(tc):
	target = list(map(int, input().split()))
	n = int(target[0])
	vito = target[1:]
	
	print(cal_length(n, vito))
