'''
	避免從太小的數字開始搜尋，所以從目標值-n位數*9開始找。
	另外，因為有些測資是小於10的，例如3之類的，會出現負數。
	所以起始點使用max(0,target - 9*n)
'''
tc = int(input())
for _ in range(tc):
	target = int(input())
	ans = []
	
	for num in range(max(0, target-9*len(str(target))), target):
		digit_sum = 0
		
		for i in str(num):
			digit_sum += int(i)
		
		if num + digit_sum == target:
			ans.append(num)
			
	if len(ans) != 0:
		print(min(ans))
	else:
		print("0")