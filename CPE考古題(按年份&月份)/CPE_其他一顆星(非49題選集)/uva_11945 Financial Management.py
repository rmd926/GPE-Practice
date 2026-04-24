tc = int(input())
for t in range(tc):
    temp = 0
    for _ in range(12):
        target = float(input())
        temp += target
    
    ans = temp / 12
    print(f"{t+1} ${ans:,.2f}")
