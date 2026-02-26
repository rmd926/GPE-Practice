while True:
	a, b = map(int, input().split())
	if a == 0 and b == 0:
		break
	carry = 0
	ans = 0
	
	while a > 0 and b > 0:
		if a % 10 + b % 10 + carry >= 10: # 判斷是否超過10，若有把carry設為1，並且把次數 += 1
			carry = 1
			ans += 1
		else: # 若沒有超過，則把carry設0
			carry = 0
        
		# 不論有無carry，都要把a、b都 //= 10，再丟回while a > 0 and b > 0:去判斷
		a //= 10
		b //= 10
	
	if ans == 0:
		print("No carry operation.")
		
	elif ans == 1:
		print("1 carry operation.")
		
	else:
		print(f"{ans} carry operations.")
