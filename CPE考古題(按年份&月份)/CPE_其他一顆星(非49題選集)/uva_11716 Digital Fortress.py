tc = int(input())
for _ in range(tc):
    try:
        target = input()
    except:
        break

    sqrt = int(len(target)**0.5)
    if len(target) !=  sqrt ** 2:
        print("INVALID")
        continue
    
    temp = []
    ans = ""
    
    for i in range(0, len(target) - sqrt + 1, sqrt):
        temp.append(target[i:i+sqrt])
    
    for i in range(len(temp)):
        for j in range(len(temp)):
            ans += temp[j][i]
    
    print(ans)
