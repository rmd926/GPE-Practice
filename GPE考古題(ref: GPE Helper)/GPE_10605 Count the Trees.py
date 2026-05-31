'''
My ans: 2026.06.01
'''
MAX = 600
fact = [1] * (MAX+1)
for i in range(1, MAX+1):
    fact[i] = fact[i-1] * i

while True:
    try:
        n = int(input())
    except:
        break

    if n == 0:
        break

    ans = fact[2*n] // (fact[n] * (n+1))
    print(ans)
  

'''
ref: 20200706	jlhung	v1.0 卡特蘭樹
'''

while True:
    n = int(input())
    
    if n == 0:
        break
    
    total = 1
    for i in range(n+2, 2*n+1):
        total *= i
    
    print(total)
