while True:
	L, N = map(int, input().split())
	lookup = {}
	for _ in range(L):
		singular, plural = map(str, input().split())
		lookup[singular] = plural
	
	for _ in range(N):
		target = input()
		
		if target in lookup:
			print(lookup[target])
			
		else:
			if target[-1] == "o" or target[-1] == "s" or target[-2:] == "ch" or target[-2:] == "sh" or target[-1] == "x":
				print(target+"es")
				
			elif target[-2] not in "aeiou" and target[-1] == "y":
				print(target[:-1]+"ies")
				
			else:
				print(target+"s")
