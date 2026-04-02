mod = 131071
while True:
	try:
		line = input()
	except:
		break
	
	if "#" in line:
		target = line[:-1]
		num = int(target, 2)
		
		if num % mod == 0:
			print("YES")
			
		else:
			print("NO")
