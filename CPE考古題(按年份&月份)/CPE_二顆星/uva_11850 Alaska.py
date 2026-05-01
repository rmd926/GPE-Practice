import sys

while True:
    try:
        n = int(input())
    except:
        break
    
    if n == 0:
        break

    target = []
    status = True
    for _ in range(n):
        k = int(input())
        target.append(k)
    
    target.sort()
    if target[0] > 200:
        status = False

    for i in range(1, n):
        if abs(target[i] - target[i-1]) > 200:
            status = False
            break
        else:
            continue
        
    if 2 * (1422 - target[-1]) > 200:
        status = False

    print("POSSIBLE") if status else print("IMPOSSIBLE")
