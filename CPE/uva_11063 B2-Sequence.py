'''
本題輸入輸出有點麻煩，一堆空行需要注意的 (測資和測資之間有空行、輸出時候也有空行)
條件判斷式除了需要考慮target list裡面的元素是否可以由該list內任意兩個元素相加獲得之外，還要考慮:
(1) target list內的所有元素需要由小到大排列，只要不是從小到大排列就是False
(2) target list內的所有元素不能夠有0，只要有0這個值，也是False
'''

tc = 1
while True:
	length = int(input())
	print(f"Case #{tc}: ",end = "")
	status = True
	sequence = []
	target = list(map(int, input().split()))
	for i in range(length-1):
		for j in range(i+1, length):
			if target != sorted(target) or 0 in target:
				status = False
				break
			
			else:
				if target[i] + target[j] in sequence:
					status = False
					break
				else:
					sequence.append(target[i] + target[j])
	if status:
		print("It is a B2-Sequence.")
	else:
		print("It is not a B2-Sequence.")
		
	print()
	tc += 1
	space = input()

