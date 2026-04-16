def swap_times(target):
    n = len(target)
    count = 0
    temp = list(target)
    for i in range(n):
        for j in range(n-i-1):
            if ord(temp[j]) > ord(temp[j+1]):
                temp[j], temp[j+1] = temp[j+1], temp[j]
                count += 1
    
    return count

tc = int(input())
for t in range(tc):
    try:
        space = input()
        n, m = map(int, input().split())
    except:
        break

    lookup = []
    for _ in range(m):
        target = input()
        lookup.append((target, swap_times(target)))
    
    lookup.sort(key = lambda x: x[1])
    
    for word in lookup:
        print(word[0])
    
    if t != tc - 1:
        print()
