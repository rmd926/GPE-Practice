while True: 
	try:
		n = int(input()) 
		nums = list(map(int,input().split()))
		count = 0 
		# bubble sort 
		for i in range(n): 
			for j in range(n-i-1):
				if nums[j] > nums[j+1]:
					nums[j], nums[j+1] = nums[j+1], nums[j] # swap
					count += 1 
		print("Minimum exchange operations :",count)
	except: 
		break