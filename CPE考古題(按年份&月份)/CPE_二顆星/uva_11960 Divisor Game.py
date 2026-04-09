MAX = 10 ** 6
table = [0] * (MAX+1)

for i in range(1, MAX+1):
    for j in range(i, MAX+1, i):
        table[j] += 1

tc = int(input())
for _ in range(tc):
    try:
        target = int(input())
    except:
        break

    ans = []
    max_num = max(table[0: target+1])

    for i in range(1, target+1):
        if table[i] == max_num:
            ans.append(i)
    
    print(max(ans))
