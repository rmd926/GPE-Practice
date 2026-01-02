tc = int(input())
for i in range(tc):
	e,f,c = map(int, input().split())
	current = e+f
	ans = 0
	
	while current >= c:
		temp = current // c
		rest = current % c
		current = temp + rest
		ans += temp
	print(ans)
	
'''
(n + (n-b)/(a-b)*b)

input()
while 1:
	e,f,c=map(int,input().split())
	print((e+f-1)//(c-1))

'''