'''
test case 1:
第一個265是十進制；第二個是16進制
算1的數量的時候通通都先轉成二進制
'''

tc = int(input())
while True:
	N = int(input())
	X1 = N
	B1 = bin(X1)[2:]
	
	X2 = int(str(N),16)
	B2 = bin(X2)[2:]
	
	B1_count = 0
	B2_count = 0
	
	for i in B1:
		if i == "1":
			B1_count += 1
	for j in B2:
		if j == "1":
			B2_count += 1
	
	print(f"{B1_count} {B2_count}")