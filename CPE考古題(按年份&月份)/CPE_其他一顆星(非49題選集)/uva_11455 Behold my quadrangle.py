tc = int(input())
for _ in range(tc):
    try:
        target = list(map(int, input().split()))
    except:
        break
    target.sort()

    if target[3] >= target[0] + target[1] + target[2]:
        print("banana")
    
    elif len(set(target)) == 1:
        print("square")
    
    elif len(set(target)) == 2 and target[0] == target[1] and target[2] == target[3]:
        print("rectangle")
    
    else:
        print("quadrangle")
