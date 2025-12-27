def cal_length(num: int) -> int:
    length = 1
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        length += 1
    return length

while True:
    try:
        i, j = map(int, input().split())
        ans = 0
        for num in range(min(i, j), max(i, j) + 1):
            ans = max(ans, cal_length(num))
        print(i, j, ans)
    except:
        break
