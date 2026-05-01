import sys

while True:
    try:
        n, m = map(int, sys.stdin.readline().split())
    except:
        break

    if n == 0 and m == 0:
        break

    Jack = []
    Jill = []

    for _ in range(n):
        Jack.append(int(sys.stdin.readline()))
    
    for _ in range(m):
        Jill.append(int(sys.stdin.readline()))
    
    ptr_Jack, ptr_Jill = 0, 0
    count = 0

    while ptr_Jack < n and ptr_Jill < m:
        if Jack[ptr_Jack] == Jill[ptr_Jill]:
            count += 1
            ptr_Jack += 1
            ptr_Jill += 1
        elif Jack[ptr_Jack] < Jill[ptr_Jill]:
            ptr_Jack += 1
        else:
            ptr_Jill += 1
    
    print(count)
