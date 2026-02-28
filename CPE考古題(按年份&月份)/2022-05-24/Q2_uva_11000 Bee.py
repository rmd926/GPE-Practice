while True:
	target = int(input())
	if target == -1:
		break
	male, female = 0, 1 # 初始一母
	
	# female -> self + 1m (每個母會生1公+自己)
	# male-> 1m + 1f (每個公會生1公一母，但自己gg)
    
	for i in range(target):
		temp = female
		female = male + 1
		male += temp
	
	print(male, female + male)
'''
0 1
1 1
2 2 
4 3
7 5
12 8
'''
