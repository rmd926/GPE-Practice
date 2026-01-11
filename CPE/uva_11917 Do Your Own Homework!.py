tc = int(input())
for i in range(tc):
    N = int(input())
    lookup = {}

    for _ in range(N):
        sub, quota = map(str, input().split())
        lookup[sub] = int(quota)
    D = int(input())
    submit = input()

    if submit in lookup and lookup[submit] <= D:
        print(f"Case {i+1}: Yesss")

    elif submit in lookup and lookup[submit] > D and lookup[submit] - D <= 5:
        print(f"Case {i+1}: Late")
        
    else:
        print(f"Case {i+1}: Do your own homework!")
