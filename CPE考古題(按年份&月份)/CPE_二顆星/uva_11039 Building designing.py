tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(int(input()))

    arr.sort(key=abs) # 按照絕對值大小去排序

    ans = 1 # 初始樓高 = 1
    last = arr[0]

    for i in range(1, n):
        if arr[i] * last < 0: # 如果第i個和當前上一層為正負互斥，則把長度+1，並且把上一層更新成當前這層
            ans += 1
            last = arr[i]

    print(ans)
