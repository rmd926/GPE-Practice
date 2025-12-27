def factor_sum(num):
	factor_sum = 0
	for i in range(1, num//2 + 1):
		if num % i == 0:
			factor_sum += i
	return factor_sum
	
print("PERFECTION OUTPUT")

while True:
	num = int(input())
	if num == 0:
		break
	if factor_sum(num) > num:
		status = "ABUNDANT"
		#print(f"{num:5d}  ABUNDANT")
	elif factor_sum(num) == num:
		status = "PERFECT"
		#print(f"{num:5d}  PERFECT")
	else:
		status = "DEFICIENT"
		#print(f"{num:5d}  DEFICIENT")
	print(f"{num:5d}  {status}")
	
print("END OF OUTPUT")