lookup = {}
while True:
	try:
        # 字典和查詢中間的空白行，若無輸入則break
		line = input()
		if not line:
			break
        
		word1, word2 = line.split()
		lookup[word2] = word1
	except:
		break

while True:
	try:
		target = input()
	except:
		break
	
	if target not in lookup:
		print("eh")
	else:
		print(lookup[target])
