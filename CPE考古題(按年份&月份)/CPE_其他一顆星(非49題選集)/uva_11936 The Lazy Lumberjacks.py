tc = int(input())
for _ in range(tc):
    try:
        target = list(map(int, input().split()))
    except:
        break
    
    target.sort()

    if target[0] + target[1] > target[2]:
        print("OK")
    else:
        print("Wrong!!")
