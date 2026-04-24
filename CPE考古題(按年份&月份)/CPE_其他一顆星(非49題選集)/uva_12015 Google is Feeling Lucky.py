tc = int(input())
for t in range(tc):
    lookup = {}
    for _ in range(10):
        link, score = map(str, input().split())
        lookup[link] = int(score)
    
    max_score = max(lookup.values())
    print(f"Case #{t+1}:")

    for key, value in lookup.items():
        if value == max_score:
            print(key)
