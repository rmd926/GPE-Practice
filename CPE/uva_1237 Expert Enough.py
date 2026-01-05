tc = int(input())

for t in range(tc):
	D = int(input())
	database = {}
	for i in range(D):
		brand, low, high = input().split()
		database[brand] = int(low), int(high)
		
	Q = int(input())
	for j in range(Q):
		price = int(input())
		count = 0
		for key, value in database.items():
			if value[0] <= price <= value[1]:
				ans = key
				count += 1
		if count == 1:
			print(ans)
		else:
			print("UNDETERMINED")
			
	# 測資輸出和下一個測資輸出之間要空行，但是最後一筆測資輸出後不用空行	
	if t != (tc - 1):
		print()