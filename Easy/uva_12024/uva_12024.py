def Factorial(n):
	f = 1
	for i in range(1, n+1):
		f *= i
	return f

def Derangement(n):
	'''
	Derangement(0) == 1 ; Derangement(1) == 0
	'''
	if n == 0:
		return 1
	if n == 1:
		return 0
	else:
	    return (n-1) * (Derangement(n-1) + Derangement(n-2))

TC = int(input())
for _ in range(TC):
    n = int(input())
    num = Derangement(n)
    den = Factorial(n)
    # print(str(Derangement(n)),'/',str(Factorial(n)))
    print(f"{num}/{den}")
