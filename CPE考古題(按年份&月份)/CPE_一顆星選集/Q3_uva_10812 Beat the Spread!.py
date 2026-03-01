tc = int(input())
for _ in range(tc):
	a, b = map(int, input().split())
	
	if a < b or (a-b) % 2 != 0:
		print("impossible")
	
	else:
		print(f"{(a+b)//2} {(a-b)//2}")
