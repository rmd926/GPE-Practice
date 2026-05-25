lookup = {}
while True:
	try:
		line = input().lower()
	except:
		break
	
	word = ""
	for ch in line:
		if ch.isalpha():
			word += ch
		else:
			if word != "":
				if word in lookup:
					lookup[word] += 1
				else:
					lookup[word] = 1
				
				word = ""
	
	if word != "":
		if word in lookup:
			lookup[word] += 1
		else:
			lookup[word] = 1
	
for key, value in sorted(lookup.items()):
	print(key)

# 2026.05.25 二刷 line 21要注意
