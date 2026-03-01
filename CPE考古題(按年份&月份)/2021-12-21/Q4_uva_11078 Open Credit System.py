'''
這題不能用two pointers會吃TLE，只能使用線性掃描O(n)
'''
tc = int(input())
for _ in range(tc):
	n = int(input())
	target = list(map(int, input().split()))

	ans = float("-inf")
	max_value = target[0] # 把第一個數字先設max_value
	
	for i in range(1, n):
		ans = max(ans, max_value - target[i]) # 檢查當前最大值去減掉target[i]並且和ans取max
		max_value = max(max_value, target[i]) # max_value也要和target[i]更新最大值
	
	print(ans)


'''
tc = int(input())
for _ in range(tc):
	n = int(input())
	target = list(map(int, input().split()))
    value = []
    # left, right = 0, n-1
    for i in range(n):
    	for j in range(n-1, i, -1):
    		#if target[i] - target[j] > max_value:
    		value.append(target[i] - target[j])

    print(max(value))
'''
