'''
while True: 
    a, b = map(int, input().split()) 
    while a < b: 
        b -= a 
        a += 1 
    print(a)
'''
'''
上面方法會TLE，所以要用公式解QQ
'''
import math

while True:
	a, b = map(int, input().split())
	
	D = 1 - 4*a + 4 * (a**2) + 8 * b
	n = (-1 + math.sqrt(D)) / 2
	ans = math.ceil(n)
	print(ans)