'''
本題先要判斷該輸入字串是否為回文，判斷的邏輯要分兩種:
1. 若該字串長度為偶數，則檢查前半與後半是否為reverse的關係
2. 若該字串長度為奇數，則檢查最中間的Index以前還有最中間的Index以後是否為reverse的關係

檢查完畢後，接著要試著把非回文的target補上一些東西讓整個輸出也會是回文，因此做以下事情:
1. 用一個for loop去遍歷
2. 把target和要遍歷的翻轉字串取slice並且逐一嘗試，只要送入判斷回文的function並且回傳True即可打印出來
p.s 若target一開始就是回文那就直接打印

'''

def is_palindromes(target):
	if len(target) % 2 == 0:
		if target[0: len(target) // 2] == target[len(target) // 2:][::-1]:
			return True
		else:
			return False
			
	else:
		if target[0: len(target) // 2] == target[len(target) // 2 + 1:][::-1]:
			return True
		else:
			return False

while True:
	target = input()
	reversed_target = target[::-1]
	ans = ""
	
	if is_palindromes(target):
		ans = target
	else:
		for i in range(len(target)):
			temp = target + reversed_target[i:]
			if is_palindromes(temp):
				ans = temp
	print(ans)