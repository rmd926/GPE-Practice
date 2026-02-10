import itertools

lookup = {}
all_letters = "abcdefghijklmnopqrstuvwxyz"
idx = 0

for i in range(0,6):
	for j in itertools.combinations(all_letters, i):
		lookup[("").join(j)] = idx
		idx += 1
		
while True:
	try:
		target = input()
		if lookup.get(target):
			print(lookup.get(target))
		else:
			print(0)
	except:
		break
	
