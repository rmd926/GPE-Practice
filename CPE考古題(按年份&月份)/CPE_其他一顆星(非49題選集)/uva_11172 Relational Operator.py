# 這啥碗糕==
tc = int(input())
for _ in range(tc):
	a, b = map(int, input().split())
	if a > b:
		print(">")
	elif a < b:
		print("<")
	else:
		print("=")
