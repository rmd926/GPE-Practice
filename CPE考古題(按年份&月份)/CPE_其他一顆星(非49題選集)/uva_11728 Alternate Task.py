def factor_sum(n):
    ans = 0
    for i in range(1, n+1):
        if n % i == 0:
            ans += i
    return ans

while True:
    try:
        target = int(input())
    except:
        break

    if target == 0:
        break
    ans_list = []

    for num in range(1, target+1):
        if factor_sum(num) == target:
            ans_list.append(num)
        else:
            continue
        
    if ans_list:
        print(max(ans_list))
    else:
        print(-1)
