def cal_length(vito):
	vito = sorted(vito)
	mid = len(vito) // 2
	distance = 0
	for i in range(len(vito)):
		distance += abs(vito[i] - vito[mid])
		
	return distance

tc = int(input())
for _ in range(tc):
	target = list(map(int, input().split()))
	n = target[0]
	vito = target[1:]
	
	print(cal_length(vito))
