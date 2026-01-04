tc = int(input())
lookup = {}
for i in range(tc):
	target = input().split()
	country = target[0]
	
	if country not in lookup:
		lookup[country] = 1
	else:
		lookup[country] += 1
		
for k,v in sorted(lookup.items()):
	print(k,v)
	
'''
for country in sorted(lookup):
    print(country,lookup[country])
'''

