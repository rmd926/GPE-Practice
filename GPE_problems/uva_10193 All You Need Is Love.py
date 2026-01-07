'''
本題先把輸入通通先用2進制去包，接著使用輾轉相除法並且使用while loop檢查
當輾轉相除到後面 y被整除且x>1的時候: All you need is love!；反之則: Love is not all you need!
'''

tc = int(input())
for i in range(tc):
	x = int(input(),2)
	y = int(input(),2)
	
	while y > 0:
		x, y = y, x%y
		
	if x > 1 and y == 0:
		print(f"Pair #{i+1}: All you need is love!")
	
	else:
		print(f"Pair #{i+1}: Love is not all you need!")