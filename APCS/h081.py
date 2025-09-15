# https://zerojudge.tw/ShowProblem?problemid=h081
n, d = map(int, input().split())
target = [int(x) for x in input().split()]
Keep = True

profit = 0
buy_point = target[0]
sale_point = target[0] 

for i in range(1,n):
	if Keep: 
		if target[i] >= buy_point + d:
			profit += target[i]- buy_point
			sale_point = target[i]
			Keep = False

	else: # Keep != True
		if target[i] <= sale_point - d:
			buy_point = target[i]
			Keep = True
			
print(profit)
