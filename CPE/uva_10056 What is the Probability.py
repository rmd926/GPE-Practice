def solution(n,p,target):
	if p == 0:
		return 0.000
	q = 1-p
	return f"{p*(q**(target-1)/(1-q**n)):.4f}"

tc = int(input())
for i in range(tc):
	n, p, target = input().split()
	print(solution(int(n),float(p),int(target)))