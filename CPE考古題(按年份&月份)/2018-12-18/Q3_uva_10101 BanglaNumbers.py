def bangla(num):
	result = ""
	if num >= 10000000:
		result += f"{bangla(num // 10000000)} kuti "
		num %= 10000000
		
	if num >= 100000:
		result += f"{bangla(num // 100000)} lakh "
		num %= 100000
	
	if num >= 1000:
		result += f"{bangla(num // 1000)} hajar "
		num %= 1000
	
	if num >= 100:
		result += f"{bangla(num // 100)} shata "
		num %= 100
	
	if num != 0:
		result += str(num)
	
	return result
	
tc = 1
while True:
	target = int(input())
	if target == 0:
		print(f"{tc:>4}. 0")
		
	else:
		ans = " ".join(bangla(target).split())
		print(f"{tc:>4}. {ans}")
		
	tc += 1
