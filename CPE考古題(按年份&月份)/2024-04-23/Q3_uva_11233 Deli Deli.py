L, N = map(int, input().split())
irregular = {} # 用來存放不規則的dict

for _ in range(L): # 先處理不規則的，key用單數型，value為複數型
	single, plural = input().split()
	irregular[single] = plural
	 
for i in range(N):
	target = input()
	if target in irregular: # 如果target屬於不規則，則print出irregular[target]
		print(irregular[target])
	
	else: # 處理常規型的
		if target[-1] == "y" and target[-2] not in "aeiou": # 如果是子音+y則去y加ies
			print(target[:-1] + "ies")
			
		elif target[-1] in "osx": # 如果是o、s、x結尾其中之一，則直接加es
			print(target+"es")
			
		elif target[-2:] == "ch" or target[-2:] == "sh": # 如果是ch或sh結尾，則直接加es
			print(target+"es")
			
		else: # 其他直接加s
			print(target+"s")
