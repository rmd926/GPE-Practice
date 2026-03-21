while True:
	nums = list(map(int, input().split()))
	
	for i in range(0, len(nums) - 1, 2):
	    n = nums[i]
	    k = nums[i + 1]
	    ans = n
	
	    while n >= k:
	        
	        remain = n % k
	        ans += n//k
	        n = n//k + remain
	        
	    print(ans)
