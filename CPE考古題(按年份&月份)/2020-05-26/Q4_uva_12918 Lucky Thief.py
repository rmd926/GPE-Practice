tc = int(input())
for _ in range(tc):
	n, m = map(int, input().split())
	print((((m-1)+(m-n))*n)//2)
