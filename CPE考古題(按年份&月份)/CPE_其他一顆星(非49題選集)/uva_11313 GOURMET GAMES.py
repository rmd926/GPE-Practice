tc = int(input())
for _ in range(tc):
    try:
        n, m = map(int, input().split())
    except:
        break
    
    ans = 0
    while n >= m:
        temp = n // m
        remain = n % m
        ans += temp
        n = temp + remain
    
    if n == 1:
        print(ans)
    else:
        print("cannot do this")

# 2026.05.25 二刷
