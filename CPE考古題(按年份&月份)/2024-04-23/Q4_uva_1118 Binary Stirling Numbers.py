tc = int(input())
for _ in range(tc):
	try:
		line = input().strip()
		if not line:
			line = input().strip()
		n,m = map(int,line.split())
		result = ((n-m)&((m-1)//2) == 0)
		print(int(result))
	except EOFError:
		break
