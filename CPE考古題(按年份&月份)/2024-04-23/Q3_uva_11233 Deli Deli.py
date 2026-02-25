L, N = map(int, input().split())
irregular = {}

for _ in range(L):
	single, plural = input().split()
	irregular[single] = plural
	 
for i in range(N):
	target = input()
	if target in irregular:
		print(irregular[target])
	
	else:
		if target[-1] == "y" and target[-2] not in "aeiou":
			print(target[:-1] + "ies")
			
		elif target[-1] in "osx":
			print(target+"es")
			
		elif target[-2:] == "ch" or target[-2:] == "sh":
			print(target+"es")
			
		else:
			print(target+"s")
