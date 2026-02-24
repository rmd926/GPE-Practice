def factor_sum(n: int):
	factor_sum = 0
	for i in range(1, int(n//2)+1):
		if n % i == 0:
			factor_sum += i
	return factor_sum

print("PERFECTION OUTPUT")

while True:
	target = int(input())
	ans = ""
	if target == 0:
		break
	
	if factor_sum(target) < target:
		ans = "DEFICIENT"
		
	elif factor_sum(target) > target:
		ans = "ABUNDANT"
		
	else:
		ans = "PERFECT"
	print(f"{target:5d}  {ans}")
	
print("END OF OUTPUT")
