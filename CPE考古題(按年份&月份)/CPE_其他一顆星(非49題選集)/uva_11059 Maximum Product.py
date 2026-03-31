tc = 1
while True:
	line = input()
	if line == " ":
		continue
	
	n = int(line)
	target = list(map(int, input().split()))
	ans = 0
	
	for i in range(n):
		temp = target[i]
		for j in range(i+1, n):
			temp *= target[j]
			if temp > ans:
				ans = temp
	
	print(f"Case #{tc}: The maximum product is {ans}.")
	print()
	
	tc += 1
