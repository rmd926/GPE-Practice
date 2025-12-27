import sys
current = []
dictionary = set() # deal with duplicated words

for line in sys.stdin:
	for char in line:
		if ('a' <= char <= 'z') or ('A' <= char <= 'Z'): # if not in a-z or A-Z => split
			current.append(char.lower()) # lower output
			
		else:
			if current:
				dictionary.add("".join(current))
				current = []

if current:
	dictionary.add("".join(current))
	
for word in sorted(dictionary):
	print(word)