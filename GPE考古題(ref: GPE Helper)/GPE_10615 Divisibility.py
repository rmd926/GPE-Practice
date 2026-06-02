tc = int(input())
for _ in range(tc):
    try:
        n, k = map(int, input().split())
    except:
        break

    target = list(map(int, input().split()))
    cur = [target[0] % k]

    for i in range(1, n):
        temp = []
        cur_num = target[i] % k

        for num in cur:
            plus = (num + cur_num) % k
            minus = (num - cur_num) % k

            if plus not in temp:
                temp.append(plus)
            
            if minus not in temp:
                temp.append(minus)

        cur = temp

    if 0 in cur:
        print("Divisible")
    else:
        print("Not divisible")
