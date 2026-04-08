tc = int(input())
print("Lumberjacks:")
for _ in range(tc):
    try:
        target = list(map(int, input().split()))
    except:
        break
    
    if target == sorted(target) or target == sorted(target)[::-1]:
        print("Ordered")
    else:
        print("Unordered")
