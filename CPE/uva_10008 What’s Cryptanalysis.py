count = {}
tc = int(input())

for i in range(tc):
	line = input()
	for char in line:
		if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
			char = char.upper()
			if char in count:
				count[char] += 1
			else:
				count[char] = 1
    			
items = sorted(count.items(), key=lambda kv: (-kv[1], kv[0]))

for char, freq in items:
    print(char, freq)
			