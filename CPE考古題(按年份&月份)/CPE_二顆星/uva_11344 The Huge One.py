tc = int(input())
for _ in range(tc):
    target = input()
    seq = list(map(int, input().split()))
    status = True
    
    for num in seq[1:]:
        if int(target) % num == 0:
            continue
        else:
            status = False
            break
    
    if status:
        print(f"{target} - Wonderful.")
    else:
        print(f"{target} - Simple.")
