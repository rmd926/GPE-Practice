while True:
	a, b = map(int, input().split())
	if a == 0 and b == 0:
		break
	
	Alice = list(map(int, input().split()))
	Betty = list(map(int, input().split()))
	
	rest_Alice = list(set(Alice) - set(Betty))
	rest_Betty = list(set(Betty) - set(Alice))
	
	print(min(len(rest_Alice), len(rest_Betty)))
