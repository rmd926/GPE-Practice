import itertools

all_letters = "abcdefghijklmnopqrstuvwxyz"
lookup = {}
index = 0
for i in range(0, 6):
	for j in itertools.combinations(all_letters, i):
		lookup["".join(j)] = index
		index += 1

while True:	
	target = input()
	if target in lookup:
		print(lookup[target])
	else:
		print(0)
	
