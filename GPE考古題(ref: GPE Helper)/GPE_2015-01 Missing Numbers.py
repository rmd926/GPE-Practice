while True:
    try:
        M, N = map(int, input().split())
    except:
        break

    last_sum = sum(map(int, input().split()))

    for _ in range(M - 1):
        cur_sum = sum(map(int, input().split()))

        print(last_sum - cur_sum)

        last_sum = cur_sum
