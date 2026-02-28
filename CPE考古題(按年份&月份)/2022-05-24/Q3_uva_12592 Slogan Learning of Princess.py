tc = int(input())
pair = {}
for _ in range(tc):
	s1 = input()
	s2 = input()
	pair[s1] = s2

Q = int(input())
for _ in range(Q):
	target = input()
	print(pair[target])
