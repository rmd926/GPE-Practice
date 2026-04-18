tc = int(input())
for _ in range(tc):
    try:
        space = input()
        index = list(map(eval, input().split()))
        target = list(map(eval, input().split()))
    except:
        break

    lookup = {}

    for i in range(len(target)):
        lookup[target[i]] = index[i]
    
    for key, value in sorted(lookup.items(), key = lambda x: x[1]):
        print(key)
