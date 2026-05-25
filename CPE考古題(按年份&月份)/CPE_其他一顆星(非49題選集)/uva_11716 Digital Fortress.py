tc = int(input())
for _ in range(tc):
    try:
        target = input()
    except:
        break

    n = len(target)

    root = int(n ** 0.5)
    if root ** 2 != n:
        print("INVALID")
        continue
    
    temp = []
    ans = ""
    for i in range(0, n - root + 1, root):
        temp.append(target[i: i+root+1])
    
    for i in range(root):
        for j in range(root):
            ans += temp[j][i]
    
    print(ans)

# 2026.05.26 二刷 注意細節\
