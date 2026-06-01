def digit_sum(n: int):
	total = 0
	while n > 0:
		total += n % 10
		n //= 10
	
	return total

def is_smith(n):
	Digit_sum = digit_sum(n)
	factor_count = 0
	factor_digit_sum = 0
	
	div = 2
	while div * div <= n:
		while n % div == 0:
			factor_count += 1
			factor_digit_sum += digit_sum(div)
			n //= div

		if div == 2:
			div = 3
			
		else:
			div += 2
			
	if n > 1:
		factor_count += 1
		factor_digit_sum += digit_sum(n)
		
	if factor_count == 1:
		return False
			
	return Digit_sum == factor_digit_sum
		
tc = int(input())
for _ in range(tc):
	try:
		n = int(input())
	except:
		break
	
	target = n + 1
	while True:
		if is_smith(target):
			print(target)
			break
		
		target += 1
