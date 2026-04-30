while True:
    try:
        n = int(input())
        target = list(map(int, input().split()))
    except:
        break

    Q = int(input())
    Q_list = list(map(int, input().split()))

    for num in Q_list:
        # 找比 num 小的最大值
        left, right = 0, n - 1
        lower = "X"

        while left <= right:
            mid = (left + right) // 2

            if target[mid] < num:
                lower = target[mid]
                left = mid + 1
            else:
                right = mid - 1

        # 找比 num 大的最小值
        left, right = 0, n - 1
        upper = "X"

        while left <= right:
            mid = (left + right) // 2

            if target[mid] > num:
                upper = target[mid]
                right = mid - 1
            else:
                left = mid + 1

        print(lower, upper)
