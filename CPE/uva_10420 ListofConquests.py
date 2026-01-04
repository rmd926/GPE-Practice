tc = int(input())
lookup = {} # 用於存放出現過的國家與對應的次數
for i in range(tc):
	target = input().split()
	country = target[0]
	
	if country not in lookup:
		lookup[country] = 1
	else:
		lookup[country] += 1
		
for k,v in sorted(lookup.items()): # 按照value由大到小 將國家 次數排列輸出
	print(k,v)
	
'''
for country in sorted(lookup):
    print(country,lookup[country])
'''


