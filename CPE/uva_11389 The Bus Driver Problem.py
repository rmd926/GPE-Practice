'''
本題因為輸入未必從小排到大，因此要先把早晚班的距離先sort一次；又因為每位司機都是d為上限，若是sort後直接m[0] + n[0]，一定會有case會<d
因此，選其中一個反轉整個list，讓m[0]+n[0]可以比d大。當然，也可以直接不反轉=>morn_distance[i] + night_distance[n-i-1]
最後，因為考量某些case真的還是相加<d，cost特別要用一個max(a,0)去防止加上負值。
'''
while True:
	n, d, r = list(map(int, input().split()))
	if n == 0 and d == 0 and r == 0:
		break
	
	morn_length = sorted(list(map(int, input().split())))
	night_length = list(map(int, input().split()))
	
	night_length = sorted(night_length)[::-1]
	
	cost = 0
	for i in range(n):
		cost += max((morn_length[i] + night_length[i] - d) * r, 0)

	print(cost)
