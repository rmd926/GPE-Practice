while True:
	target = input()
	temp = []
	
	for char in target:
		if char.isdigit():
			temp.append(int(char))
			
		elif char.isupper():
			temp.append(ord(char) - ord("A") + 10)
		
		elif char.islower():
			temp.append(ord(char) - ord("a") + 36)
	
	ans = float("inf")
	r = max(temp) + 1
	
	for i in range(max(2, r), 63):
		if sum(temp) % (i-1) == 0:
			ans = i
			break
	
	if ans != float("inf"):
		print(ans)

	else:
		print("such number is impossible!")
