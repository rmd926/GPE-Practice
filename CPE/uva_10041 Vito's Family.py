def solution(length, vito):
	length = len(vito)
	vito = sorted(vito)
	mid = vito[length // 2]
	ans = 0
	
	for i in vito:
		ans += abs(i-mid)
	return ans
	
tc = int(input())
for i in range(tc):
	target = list(map(int,input().split()))
	print(solution(target[0],target[1:]))