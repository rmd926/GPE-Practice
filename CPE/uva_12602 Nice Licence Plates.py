'''
input: AAA-0123；輸入固定格式為前三碼英文字，後四碼阿拉伯數字，其中A-Z代表數字為: 0-25
簡單說，本題就是: ?*26^2 + ?*26^1 + ?*26^0 - 後四碼數字 <= 100的判斷
'''
tc = int(input())

for _ in range(tc):
	target = input()
	letter_sum = 0
	num_sum = int(target[4:])
	
	for i in range(0,3):
		letter_sum += (int(ord(target[i]))-65) * 26 ** (2-i)
			
	if abs(letter_sum - num_sum) <= 100:
		print("nice")
	else:
		print("not nice")