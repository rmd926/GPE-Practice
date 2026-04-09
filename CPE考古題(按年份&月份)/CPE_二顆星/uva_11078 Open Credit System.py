tc = int(input())
for _ in range(tc):
    try:
        n = int(input())
    except:
        break

    target = list(map(int, input().split()))
    max_diff = float('-inf')
    max_score = target[0]

    for i in range(1, n):
        max_diff = max(max_diff, max_score - target[i])
        max_score = max(max_score, target[i])
    
    print(max_diff)
