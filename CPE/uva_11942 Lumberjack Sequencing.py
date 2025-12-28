import numpy as np
tc = int(input())
print("Lumberjacks:")

for i in range(tc):
	num_seq = list(map(int, input().split()))
	if num_seq == sorted(num_seq) or num_seq == sorted(num_seq)[::-1]:
		print("Ordered")
		i += 1
	else:
		print("Unordered")
		i += 1