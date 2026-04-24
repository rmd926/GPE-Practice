tc = int(input())
for _ in range(tc):
    a, b, c = map(int,input().split())
    cur = a + b
    ans = 0
    while cur >= c:
        temp = cur // c
        remain = cur % c
        
        ans += temp
        cur = temp + remain
    print(ans)
