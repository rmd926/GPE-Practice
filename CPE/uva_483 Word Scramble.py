while True:
	target = input().split()
	print(" ".join(word[::-1] for word in target))