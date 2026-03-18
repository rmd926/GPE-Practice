tc = int(input())
while True:
	N = int(input())
	X1 = N
	B1 = bin(X1)[2:]
	
	X2 = int(str(N),16)
	B2 = bin(X2)[2:]
	
	B1_count = 0
	B2_count = 0
	
	for ch in B1:
		if ch == "1":
			B1_count += 1
			
	for ch in B2:
		if ch == "1":
			B2_count += 1
	
	print(f"{B1_count} {B2_count}")
