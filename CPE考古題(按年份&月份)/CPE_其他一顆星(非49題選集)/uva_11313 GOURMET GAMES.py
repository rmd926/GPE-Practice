tc = int(input())
for _ in range(tc):
	n, m = map(int, input().split())
	count = 0

	while n >= m:
		count += n // m
		n = n // m + n % m
	
	if n != 1:
		print("cannot do this")
	else:
		print(count)
