while True:
    num = int(input())
    if num == 0:
        break

    seen = set()
    random_num = num

    while random_num not in seen:
        seen.add(random_num)
        # XX2486XX // 100 -> XX2486 -> XX2486 % 10000 -> 2486
        random_num = ((random_num ** 2) // 100) % 10000

    print(len(seen)) # equal to numbers of different random numbers.