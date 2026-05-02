import sys
tc = int(input())
for t in range(tc):

    n = int(sys.stdin.readline())
    gain = list(map(int, sys.stdin.readline().split()))
    cost = list(map(int, sys.stdin.readline().split()))

    cur_oil = 0
    total_oil = 0
    diff = 0
    start = 0

    for i in range(n):
        diff = gain[i] - cost[i]
        cur_oil += diff
        total_oil += diff

        if cur_oil < 0:
            start = i + 1
            cur_oil = 0
    
    if total_oil >= 0 and start < n:
        print(f"Case {t+1}: Possible from station {start + 1}")
    else:
        print(f"Case {t+1}: Not possible")
