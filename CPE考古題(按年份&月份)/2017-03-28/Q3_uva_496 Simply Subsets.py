while True:
	A = set(map(int, input().split()))
	B = set(map(int, input().split()))
	
	if A == B:
		print("A equals B")
		
	elif A & B == set():
		print("A and B are disjoint")
	
	elif A & B == B:
		print("B is a proper subset of A")
	
	elif A & B == A:
		print("A is a proper subset of B")
	
	else:
		print("I'm confused!")
