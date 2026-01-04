N = int(input())
slogan_pairs = {}

for _ in range(N):
	s1 = input()
	s2 = input()
	slogan_pairs[s1] = s2
	
Q = int(input())
for _ in range(Q):
	target = input()
	print(slogan_pairs[target])