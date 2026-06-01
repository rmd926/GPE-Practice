def sol(s: str):
	n = len(s)
	res = [0] * n
	j = 0
	
	for i in range(1, n):
		while j > 0 and s[i] != s[j]:
			j = res[j-1]
		
		if s[i] == s[j]:
			j += 1
			
		res[i] = j
		
	return res

while True:
	try:
		target = input()
	except:
		break

	rev = target[::-1]
	temp = rev + "#" + target
	
	res = sol(temp)
	length = res[-1]
	
	ans = target + rev[length:]
	print(ans)
