def factor_sum(num):
    ans = 0
    for i in range(1, num+1):
        if num % i == 0:
            ans += i
    return ans

tc = 1
while True:
    try:
        n = int(input())
    except:
        break

    if n == 0:
        break

    ans = []
    status = False
    for num in range(n, 0, -1):
        if factor_sum(num) == n:
            status = True
            break
        else:
            continue
    
    if status:
        print(f"Case {tc}: {num}")
    else:
        print(f"Case {tc}: -1")

    tc += 1

# 2026.05.26 二刷
